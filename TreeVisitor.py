import streamlit as st
import pandas as pd
from pandaQParser import pandaQParser

from pandaQVisitor import pandaQVisitor

class TreeVisitor(pandaQVisitor):

  def visitRoot(self, ctx):
    [query] = list(ctx.getChildren())
    self.visit(query)


  def visitQuery(self, ctx):
    [select, camps, From, taula, fin] = list(ctx.getChildren())

    # obtenir el nom i el path de la taula
    nom_taula = self.visit(taula)
    path_taula = "data/" + nom_taula + ".csv"

    try:
      # obtenir la taula
      data = pd.read_csv(path_taula)

      # si les columnes seleccionades no son totes,
      # es filtra la taula
      cols = self.visit(camps)
      new_data = pd.DataFrame()

      if cols != '*':
        for col in cols:
          if "as" not in col:
            new_data[col] = data[col]
          else:
            # es una columna calculada
            [expr, new_col] = col.split(" as ")
            new_data[new_col] = self.eval_expr(expr, data)

      else:
        new_data = data

      st.write("Taula: " + nom_taula)
      st.write(new_data)
        
    except FileNotFoundError:
      st.error("No s'ha trobat l'arxiu csv a la carpeta /data")


  def visitTaula(self, ctx):
    return ctx.ID().getText()
  

  def visitCamps(self, ctx):
    if ctx.getText() == '*':
        return '*'
    else:
        return [self.visit(col) for col in ctx.col()]
    
  
  def visitCol(self, ctx):
    if ctx.getChildCount() == 1:
        return ctx.ID().getText()
    else:
        [expr, As, ID] = list(ctx.getChildren())
        return self.visit(expr) + " as " + ctx.ID().getText()


  def visitExpr(self, ctx):
    if ctx.getChildCount() == 3:
      [left, op, right] = list(ctx.getChildren())
      return f"{self.visit(left)} {op.getText()} {self.visit(right)}"
    elif ctx.getChildCount() == 1:
      return ctx.getText()
    else:
      return f"({self.visit(ctx.expr())})"
    
  
  def visitID (self, ctx):
    return ctx.getText()


  def eval_expr(self, expr, data):
    try:
        # Crear un diccionario con las variables disponibles en el DataFrame
        variables = {col: data[col] for col in data.columns}

        # Evaluar la expresión utilizando pandas.eval
        result = pd.eval(expr, engine='python', local_dict=variables)

        # Resetear el índice si es un DataFrame
        if isinstance(result, pd.DataFrame):
            result = result.reset_index(drop=True)

        return result

    except Exception as e:
        st.error(f"Error al evaluar la expresión: {str(e)}")
        return pd.Series(dtype='object')  # Devolver una Serie vacía en caso de error
