import streamlit as st
import pandas as pd

from pandaQVisitor import pandaQVisitor

class TreeVisitor(pandaQVisitor):

  def visitRoot(self, ctx):
    [query] = list(ctx.getChildren())
    self.visit(query)

  def visitQuery(self, ctx):
    [select, taula, fin] = list(ctx.getChildren())
    nom_taula = taula.getText()
    path_taula = "data/" + nom_taula + ".csv"

    try:
      # Es mostra la taula
      data = pd.read_csv(path_taula)
      st.write("Taula: " + nom_taula)
      st.write(data)
        
    except FileNotFoundError:
      st.error("No s'ha trobat l'arxiu csv a la carpeta /data")
