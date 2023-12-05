# Generated from pandaQ.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pandaQParser import pandaQParser
else:
    from pandaQParser import pandaQParser

# This class defines a complete generic visitor for a parse tree produced by pandaQParser.

class pandaQVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pandaQParser#root.
    def visitRoot(self, ctx:pandaQParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#query.
    def visitQuery(self, ctx:pandaQParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#camps.
    def visitCamps(self, ctx:pandaQParser.CampsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#col.
    def visitCol(self, ctx:pandaQParser.ColContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#expr.
    def visitExpr(self, ctx:pandaQParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#taula.
    def visitTaula(self, ctx:pandaQParser.TaulaContext):
        return self.visitChildren(ctx)



del pandaQParser