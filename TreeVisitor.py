import streamlit as st
import pandas as pd
from pandaQParser import pandaQParser

from pandaQVisitor import pandaQVisitor

class TreeVisitor(pandaQVisitor):

  def __init__(self):
    # taula (o fusio de taules si es fan 'inner joins') original
    self.data = None       

    # quan ja s'han fet els inner joins, filtratges i ordenacions de la taula 'data', 
    # s'omple 'new_data' amb les columnes seleccionades per l'usuari
    self.new_data = None    

    # taula on es guarda la columna de la subconsulta en cas que hi hagi
    self.taulaSQ = None 

    # diccionari de taules de simbols guardades per l'usuari
    if 'taules_simbols' not in st.session_state:
      st.session_state.taules_simbols = {}
    
    # indica si hi ha hagut algun error
    self.error = False


  def visitRoot(self, ctx):
    [op, fin] = list(ctx.getChildren())
    self.visit(op)

  
  def visitAssig(self, ctx):
    nom_Tsimbols = ctx.ID().getText()
    self.visit(ctx.query())
    st.session_state.taules_simbols[nom_Tsimbols] = self.new_data # es guarda el resultat de la query a les taules de simbols
    st.info("Resultat de la consulta guardat en " + nom_Tsimbols)
  

  def visitPlot(self, ctx):
    data_plot = self.visit(ctx.taula())
    num_cols = data_plot.select_dtypes(include=['number']).columns
    if num_cols.empty:
      st.warning("No hi ha columnes numeriques disponibles per fer el plot.")
    else:
      st.line_chart(data_plot[num_cols])


  def visitQuery(self, ctx):
    # obtenir la taula de les .csv o de les taules de simbols guardades
    self.data = self.visit(ctx.taula())

    # es fusionen les taules en la taula 'data' en cas d'inner join(s)
    if ctx.join_info() is not None:
      for join in ctx.join_info():
        self.visit(join)

    # si s'ha afegit el 'where' es visita per fer el filtratge de la taula (o fusio de taules) 'data'
    if ctx.where() is not None:
      self.visit(ctx.where())

    # si s'ha afegit el 'order by' es visita per ordenar les files de la taula (o fusio de taules) 'data'
    if ctx.orderBy() is not None:
      self.visit(ctx.orderBy())
    
    # s'inicia amb la taula 'new_data' buida i es visiten els camps de la taula 'data' (o nous camps calculats)
    # que l'usuari vol consultar i es van afegint a la taula 'new_data'. Com que 'data' ja esta ordenada i filtrada,
    # el resultat de 'new_data' sera correcte perque es mantindra l'ordre i el filtratge de 'data'
    self.new_data = pd.DataFrame()
    self.visit(ctx.camps())
    
    # si no hi ha hagut cap error, es mostra la taula
    if not self.error:
      st.write(self.new_data)

  
  def visitJoin_info(self, ctx):
    # obtenir la taula amb la que es fusionara 'data'
    taula2 = self.visit(ctx.taula())
  
    # obtenir el nom de les columnes amb les que es fa l'inner join
    nom_camp1, nom_camp2 = ctx.ID()[0].getText(), ctx.ID()[1].getText()

    # es fa el inner join utilitzant 'merge' de Pandas
    try:
      self.data = pd.merge(self.data, taula2, how='inner', left_on=nom_camp1, right_on=nom_camp2) 
    except KeyError:
      st.error("Error en l'inner join: no s'ha trobat una de les columnes especificades a l'inner join.")
      self.error = True
  

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

    # com es un camp normal, simplement es copia la columna de la taula original a la nova
    try:
      self.new_data[id] = self.data[id]  
    except KeyError:
      st.error("Error: no s'ha trobat la columna " + id + " a la taula consultada.")
      self.error = True


  def visitExpr(self, ctx):
    if ctx.getChildCount() == 3:
      [left, op, right] = list(ctx.getChildren())
      return f"{self.visit(left)} {op.getText()} {self.visit(right)}"
    elif ctx.getChildCount() == 1:
      return ctx.getText()
    else:
      return self.visit(ctx.expr())
  

  def visitOrderBy(self, ctx):
    order_info = [self.visit(camp) for camp in ctx.camp_order()] # es visiten les columnes a ordenar, obtenint el nom de la columna i si es asc o desc
    columns, ascendings = zip(*order_info) # s'obte una llista amb les columnes a ordenar i un altra amb el tipus d'ordenacio (asc o desc)
    try:
      self.data.sort_values(by=list(columns), ascending=list(ascendings), inplace=True) # s'ordena la taula
    except KeyError:
      st.error("Error en la ordenació: no s'ha trobat a la taula alguna de les columnes a ordenar.")
      self.error = True


  # si es posa 'asc' o no es posa res anira a aquest visitor per ordenar ascendentment la columna 
  def visitAsc(self, ctx):
    nom_col = ctx.ID().getText()
    return nom_col, True


  # si es posa 'desc' anira a aquest visitor per ordenar descendentment
  def visitDesc(self, ctx):
    nom_col = ctx.ID().getText()
    return nom_col, False


  def visitWhere(self, ctx):
    for condition in ctx.cond():
      self.visit(condition)
  

  # comparacio del 'where' amb valor numeric sense negacio
  def visitComp_num(self, ctx):
    [param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = int(param2.getText())

    try:
      if op.getText() == '<':
        self.data = self.data.loc[self.data[nom_col] < valor]
        
      elif op.getText() == '=':
        self.data = self.data.loc[self.data[nom_col] == valor]

    except KeyError:
      st.error("Error en el where: no s'ha trobat la columna especificada en el where en la taula.")
      self.error = True

  
  # comparacio del 'where' amb valor numeric i amb negacio
  def visitComp_num_neg(self, ctx):
    [_, param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = int(param2.getText())

    try:
      if op.getText() == '<':
        self.data = self.data.loc[self.data[nom_col] >= valor]
        
      elif op.getText() == '=':
        self.data = self.data.loc[self.data[nom_col] != valor]

    except KeyError:
      st.error("Error en el where: no s'ha trobat la columna especificada en el where en la taula.")
      self.error = True
  

  # comparacio del 'where' amb textos i sense negacio
  def visitComp_text(self, ctx):
    [param1, op, param2] = list(ctx.getChildren())

    nom_col = param1.getText()
    valor = param2.getText()

    try:
      if op.getText() == '<':
        self.data = self.data.loc[self.data[nom_col] < valor]
        
      elif op.getText() == '=':
        self.data = self.data.loc[self.data[nom_col] == valor]

    except KeyError:
      st.error("Error en el where: no s'ha trobat la columna especificada en el where en la taula.")
      self.error = True
  

  # comparacio del 'where' amb textos i amb negacio
  def visitComp_text_neg(self, ctx):
    [_, param1, op, param2] = list(ctx.getChildren())

    # obtencio dels parametres de la condicio de filtratge del where
    nom_col = param1.getText()
    valor = param2.getText()

    try:
      if op.getText() == '<':
        self.data = self.data.loc[self.data[nom_col] >= valor]
        
      elif op.getText() == '=':
        self.data = self.data.loc[self.data[nom_col] != valor]

    except KeyError:
      st.error("Error en el where: no s'ha trobat la columna especificada en el where en la taula.")
      self.error = True
    
  
  # cas de comparacio del 'where' amb una subconsulta
  def visitCompSQ(self, ctx):
    col = ctx.ID().getText()

    try:
      res_subconsulta = self.visit(ctx.subquery()) # es visita la subconsulta
      self.data = self.data.loc[self.data[col].isin(res_subconsulta)] # es filtra segons el resultat de la subconsulta
    except KeyError:
      st.error("Error en el where: no s'ha trobat la columna especificada en el where en la taula.")
      self.error = True


  # retorna la columna resultant de la subconsulta
  def visitSubquery(self, ctx):
    self.taulaSQ = self.visit(ctx.taula()) 
    col = ctx.ID().getText()

    try:
      if ctx.whereSQ() is not None:
        self.visit(ctx.whereSQ())
      return self.taulaSQ[col] 
    except KeyError:
      st.error("Error en la subconsulta: no s'ha trobat la columna especificada en la subconsulta a la taula.")
      self.error = True


  # els visitors del 'where' de la subconsulta fan el mateix que els del select normal pero amb la taula de la subquery
  def visitWhereSQ(self, ctx):
    for cond in ctx.condSQ():
      self.visit(cond)


  def visitComp_numSQ(self, ctx):
    [col, operacio, val] = list(ctx.getChildren())

    col = col.getText()
    val = int(val.getText())
    op = operacio.getText()

    try:
      if op == '<':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] < val]
      elif op == '=':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] == val]
    except KeyError:
      st.error("Error en la subconsulta: no s'ha trobat la columna especificada en el where de la subconsulta.")
      self.error = True
  

  def visitComp_numSQ_neg(self, ctx):
    [_, col, operacio, val] = list(ctx.getChildren())

    col = col.getText()
    val = int(val.getText())
    op = operacio.getText()

    try:
      if op == '<':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] >= val]
      elif op == '=':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] != val]
    except KeyError:
      st.error("Error en la subconsulta: no s'ha trobat la columna especificada en el where de la subconsulta.")
      self.error = True


  def visitComp_textSQ(self, ctx):
    [col, operacio, val] = list(ctx.getChildren())

    col = col.getText()
    val = val.getText()
    op = operacio.getText()

    try:
      if op == '<':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] < val]
      elif op == '=':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] == val]
    except KeyError:
      st.error("Error en la subconsulta: no s'ha trobat la columna especificada en el where de la subconsulta.")
      self.error = True
  

  def visitComp_textSQ_neg(self, ctx):
    [_, col, operacio, val] = list(ctx.getChildren())

    col = col.getText()
    val = val.getText()
    op = operacio.getText()

    try:
      if op == '<':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] >= val]
      elif op == '=':
        self.taulaSQ = self.taulaSQ.loc[self.taulaSQ[col] != val]
    except KeyError:
      st.error("Error en la subconsulta: no s'ha trobat la columna especificada en el where de la subconsulta.")
      self.error = True
    

  def visitTaula(self, ctx):
    # obtenir el nom de la taula
    nom_taula = ctx.ID().getText()

    # si el nom de la taula es el de una taula de simbols guardada
    if nom_taula in st.session_state.taules_simbols:
      return st.session_state.taules_simbols[nom_taula]

    # si el nom de la taula es un .csv
    else:
      try:
        path_taula = "data/" + nom_taula + ".csv"
        return pd.read_csv(path_taula)
      except FileNotFoundError:
        st.error("No s'ha trobat la taula ni a la carpeta /data ni a les taules guardades.")
        self.error = True


  def visitID(self, ctx):
    return ctx.getText()


  # funcio que utilitza la funcio 'eval' de Pandas per evaluar la expressio
  def eval_expr(self, expr):
    try:
      variables = {col: self.data[col] for col in self.data.columns}

      result = pd.eval(expr, engine='python', local_dict=variables)

      if isinstance(result, pd.DataFrame):
        result = result.reset_index(drop=True)

      return result

    except Exception as e:
      st.error(f"Error al evaluar la expresio del camp calculat: {str(e)}")
      self.error = True
      return pd.Series(dtype='object')
