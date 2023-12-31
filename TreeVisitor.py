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


  def visitSelectNormal(self, ctx):
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


  def visitSelectOrder(self, ctx):
    [select, camps, From, taula, OrderBy, order, fin] = list(ctx.getChildren())

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

      # visitor per ordenar la taula
      self.visit(order)

      st.write("Taula: " + nom_taula)
      st.write(self.new_data)
        
    except FileNotFoundError:
      st.error("No s'ha trobat l'arxiu csv a la carpeta /data")

  
  def visitSelectWhere(self, ctx):
    [select, camps, From, taula, Where, conds_where, fin] = list(ctx.getChildren())

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

      self.visit(conds_where)

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
    
  
  def visitOrder(self, ctx):
    order_info = [self.visit(camp) for camp in ctx.camp_order()] # es visiten les columnes a ordenar, obtenint el nom de la columna i (asc o desc)
    columns, ascendings = zip(*order_info) # s'obte una llista amb les columnes a ordenar i un altra amb el tipus d'ordenacio (asc o desc)

    self.new_data.sort_values(by=list(columns), ascending=list(ascendings), inplace=True) # s'ordena la taula


  # si es posa 'asc' o no es posa res anira a aquest visitor per ordenar ascendentment
  def visitAsc(self, ctx):
    return ctx.ID().getText(), True


  # si es posa 'desc' anira a aquest visitor per ordenar descendentment
  def visitDesc(self, ctx):
    return ctx.ID().getText(), False
  

  def visitConds_where(self, ctx):
    for condition in ctx.cond():
      self.visit(condition)
  

  # Comparacio del 'where' amb textos i sense not
  def visitComp_text(self, ctx):
    [param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = param2.getText()

    if op.getText() == '<':
      self.new_data = self.new_data.loc[self.new_data[nom_col] < valor]
      
    elif op.getText() == '=':
      self.new_data = self.new_data.loc[self.new_data[nom_col] == valor]


  # Comparacio del 'where' amb numeros i sense not
  def visitComp_num(self, ctx):
    [param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = int(param2.getText())

    if op.getText() == '<':
      self.new_data = self.new_data.loc[self.new_data[nom_col] < valor]
      
    elif op.getText() == '=':
      self.new_data = self.new_data.loc[self.new_data[nom_col] == valor]
  

  # Comparacio del 'where' amb textos i amb not
  def visitComp_text_not(self, ctx):
    [neg, param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = param2.getText()

    if op.getText() == '<':
      self.new_data = self.new_data.loc[self.new_data[nom_col] >= valor]
      
    elif op.getText() == '=':
      self.new_data = self.new_data.loc[self.new_data[nom_col] != valor]
  

  # Comparacio del 'where' amb numeros i amb not
  def visitComp_num_not(self, ctx):
    [neg, param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = int(param2.getText())

    if op.getText() == '<':
      self.new_data = self.new_data.loc[self.new_data[nom_col] >= valor]
      
    elif op.getText() == '=':
      self.new_data = self.new_data.loc[self.new_data[nom_col] != valor]


  def visitID(self, ctx):
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
