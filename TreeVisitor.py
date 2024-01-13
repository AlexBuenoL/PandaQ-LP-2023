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
    camps = ctx.camps()
    taula = ctx.taula()
    where = ctx.where()
    ord = ctx.orderBy()
    joins_list = ctx.join_info()

    # obtenir el nom i el path de la taula
    nom_taula = self.visit(taula)
    path_taula = "data/" + nom_taula + ".csv"

    try:
      # obtenir la taula
      self.data = pd.read_csv(path_taula)

      # abans de tractar els camps de la taula, es fa el merge de les taules
      # per poder accedir correctament als camps
      if joins_list is not None:
        for join in joins_list:
          self.visit(join)

      # taula buida per anar afegint columnes segons convingui a partir de l'entrada i la taula/es originals
      self.new_data = pd.DataFrame()

      # es visiten els camps de la taula a consultar per obtenir la taula 
      # que es mostrara a 'new_data'
      self.visit(camps)

      # si s'ha afegit el 'where' es visita per fer el filtratge
      if where is not None:
        self.visit(where)

      # si s'ha afegit el 'order by' es visita per ordenar les files
      if ord is not None:
        self.visit(ord)

      st.write("Taula: " + nom_taula)
      st.write(self.new_data)
        
    except FileNotFoundError:
      st.error("No s'ha trobat l'arxiu csv a la carpeta /data")

  
  def visitJoin_info(self, ctx):

    # obtenir la segona taula
    nom_taula2 = self.visit(ctx.taula())
    path_taula2 = "data/" + nom_taula2 + ".csv"
    taula2 = pd.read_csv(path_taula2)

    # obtenir el nom de les columnes de l'inner join
    nom_camp1, nom_camp2 = ctx.ID()[0].getText(), ctx.ID()[1].getText()

    # es fa el inner join utilitzant 'merge' de Pandas
    self.data = pd.merge(self.data, taula2, how='inner', left_on=nom_camp1, right_on=nom_camp2)
  

  def visitCamps(self, ctx):
    if ctx.getText() == '*':        # si es vol consultar tota la taula, la taula que es mostra es la taula original directament
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
  

  def visitOrderBy(self, ctx):
    self.visit(ctx.order())

  
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


  def visitWhere(self, ctx):
    self.visit(ctx.conds_where())
  

  def visitConds_where(self, ctx):
    for condition in ctx.cond():
      self.visit(condition)
  

  # Comparacio del 'where' amb textos
  def visitComp_text(self, ctx):
    childs = list(ctx.getChildren())

    # determinar si hi ha negacio
    if len(childs) == 3:
      neg = False
      [param1, op, param2] = childs
    elif len(childs) == 4:
      neg = True
      [_, param1, op, param2] = childs

    # obtencio dels parametres de la condicio de filtratge del where
    nom_col = param1.getText()
    valor = param2.getText()

    # si hi ha negacio, es filtra amb l'operador complementari
    if neg:
      if op.getText() == '<':
        self.new_data = self.new_data.loc[self.data[nom_col] >= valor]
        
      elif op.getText() == '=':
        self.new_data = self.new_data.loc[self.data[nom_col] != valor]
    
    # si no hi ha negacio, es filtra amb l'operador original
    else:
      if op.getText() == '<':
        self.new_data = self.new_data.loc[self.data[nom_col] < valor]
        
      elif op.getText() == '=':
        self.new_data = self.new_data.loc[self.data[nom_col] == valor]


  # Comparacio del 'where' amb numeros 
  def visitComp_num(self, ctx):
    childs = list(ctx.getChildren())

    # determinar si hi ha negacio
    if len(childs) == 3:
      neg = False
      [param1, op, param2] = childs
    elif len(childs) == 4:
      neg = True
      [_, param1, op, param2] = childs

    # obtencio dels parametres de la condicio de filtratge del where
    nom_col = param1.getText()
    valor = int(param2.getText())

    # si hi ha negacio, es filtra amb l'operador complementari
    if neg:
      if op.getText() == '<':
        self.new_data = self.new_data.loc[self.data[nom_col] >= valor]
        
      elif op.getText() == '=':
        self.new_data = self.new_data.loc[self.data[nom_col] != valor]
    
    # si no hi ha negacio, es filtra amb l'operador original
    else:
      if op.getText() == '<':
        self.new_data = self.new_data.loc[self.data[nom_col] < valor]
        
      elif op.getText() == '=':
        self.new_data = self.new_data.loc[self.data[nom_col] == valor]

  
  def visitTaula(self, ctx):
    return ctx.ID().getText()


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
