import streamlit as st
from TreeVisitor import TreeVisitor

from pandaQLexer import pandaQLexer
from pandaQParser import pandaQParser

from antlr4 import *

# SCRIPT PER LLEGIR LES CONSULTES DES DE TERMINAL

st.title('PandaQ - LP 2023')

st.info("Escriu la consulta SQL a la terminal")

input_query = input('Introdueix la consulta SQL: ')

lexer = pandaQLexer(InputStream(input_query))
token_stream = CommonTokenStream(lexer)
parser = pandaQParser(token_stream)
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
    visitor = TreeVisitor()
    visitor.visit(tree)
else:
    st.write(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    st.write(tree.toStringTree(recog=parser))
