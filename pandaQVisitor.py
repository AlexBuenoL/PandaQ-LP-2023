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


    # Visit a parse tree produced by pandaQParser#selectNormal.
    def visitSelectNormal(self, ctx:pandaQParser.SelectNormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selectOrder.
    def visitSelectOrder(self, ctx:pandaQParser.SelectOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selectWhere.
    def visitSelectWhere(self, ctx:pandaQParser.SelectWhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#camps.
    def visitCamps(self, ctx:pandaQParser.CampsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campCalculat.
    def visitCampCalculat(self, ctx:pandaQParser.CampCalculatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#camp.
    def visitCamp(self, ctx:pandaQParser.CampContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#expr.
    def visitExpr(self, ctx:pandaQParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#order.
    def visitOrder(self, ctx:pandaQParser.OrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#asc.
    def visitAsc(self, ctx:pandaQParser.AscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#desc.
    def visitDesc(self, ctx:pandaQParser.DescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#conds_where.
    def visitConds_where(self, ctx:pandaQParser.Conds_whereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#cond_normal.
    def visitCond_normal(self, ctx:pandaQParser.Cond_normalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#cond_negada.
    def visitCond_negada(self, ctx:pandaQParser.Cond_negadaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#taula.
    def visitTaula(self, ctx:pandaQParser.TaulaContext):
        return self.visitChildren(ctx)



del pandaQParser