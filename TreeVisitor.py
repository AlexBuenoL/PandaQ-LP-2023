import streamlit as st
import pandas as pd
from pandaQParser import pandaQParser

from pandaQVisitor import pandaQVisitor

class TreeVisitor(pandaQVisitor):

  # atributs de la classe per poder accedir a les taules desde les funcions del visitor
  def __init__(self):
    self.data = None 
    self.new_data = None


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
      self.data = pd.read_csv(path_taula)

      # taula buida que sera la que es modificara amb els visitors i la que es mostrara
      self.new_data = pd.DataFrame()

      # es visiten els camps de la taula a consultar per obtenir la taula 
      # que es mostrara a 'new_data'
      self.visit(camps)

      st.write("Taula: " + nom_taula)
      st.write(self.new_data)
        
    except FileNotFoundError:
      st.error("No s'ha trobat l'arxiu csv a la carpeta /data")


  def visitTaula(self, ctx):
    return ctx.ID().getText()
  

  def visitCamps(self, ctx):
    if ctx.getText() == '*':        # si es vol consultar tota la taula, la taula que es mostra es tota
        self.new_data = self.data
    else:
      for col in ctx.col():         # si no, es visiten les diferents columnes a consultar -> campCalculat o camp
        self.visit(col)
           
    
  def visitCampCalculat(self, ctx):
    [expr, As, id] = list(ctx.getChildren())
    expr_res = self.visit(expr)     # s'obte la expressio de la nova columna calculada
    new_col = ctx.ID().getText()    # s'obte el nom de la nova columna
    self.new_data[new_col] = self.eval_expr(expr_res) # es crea la nova columna de new_data amb el nom escollit i amb els valors calculats
     

  def visitCamp(self, ctx):    
    id = ctx.ID().getText()
    self.new_data[id] = self.data[id]  # com es un camp normal, simplement es copia la columna de la taula original a la nova


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


  def eval_expr(self, expr):
    try:
      variables = {col: self.data[col] for col in self.data.columns}

      result = pd.eval(expr, engine='python', local_dict=variables)

      if isinstance(result, pd.DataFrame):
        result = result.reset_index(drop=True)

      return result

    except Exception as e:
      st.error(f"Error al evaluar la expresión: {str(e)}")
      return pd.Series(dtype='object')
