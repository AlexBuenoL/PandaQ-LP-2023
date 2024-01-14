import streamlit as st
from antlr4 import *

from TreeVisitor import TreeVisitor
from pandaQLexer import pandaQLexer
from pandaQParser import pandaQParser

#SCRIPT PER LLEGIR LES CONSULTES DES DE STREAMLIT

st.title('PandaQ - LP 2023')

query = st.text_area("Consulta SQL:", height=110)
  
if st.button("Executa"):
    lexer = pandaQLexer(InputStream(query))
    token_stream = CommonTokenStream(lexer)
    parser = pandaQParser(token_stream)
    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() == 0:
        visitor = TreeVisitor()
        visitor.visit(tree)
    else:
        st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
        st.write(tree.toStringTree(recog=parser))



