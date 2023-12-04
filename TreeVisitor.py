import streamlit as st
import pandas as pd

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
      if cols != '*':
        data = data[cols]

      st.write("Taula: " + nom_taula)
      st.write(data)
        
    except FileNotFoundError:
      st.error("No s'ha trobat l'arxiu csv a la carpeta /data")


  def visitTaula(self, ctx):
    return ctx.ID().getText()
  

  def visitCamps(self, ctx):
    if ctx.getText() == '*':
        return '*'
    else:
        return self.visit(ctx.cols())
    
  
  def visitCols(self, ctx):
    return [id.getText() for id in ctx.ID()]

