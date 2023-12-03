import streamlit as st
from TreeVisitor import TreeVisitor

from pandaQLexer import pandaQLexer
from pandaQParser import pandaQParser

from antlr4 import *


#SCRIPT PER LLEGIR LES CONSULTES DES DE STREAMLIT

st.title('PandaQ - LP 2023')

query = st.text_input("Consulta SQL:")
  
if st.button("Executa"):
  lexer = pandaQLexer(InputStream(query))
  token_stream = CommonTokenStream(lexer)
  parser = pandaQParser(token_stream)
  tree = parser.root()

  if parser.getNumberOfSyntaxErrors() == 0:
      visitor = TreeVisitor()
      visitor.visit(tree)
  else:
    print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    print(tree.toStringTree(recog=parser))



