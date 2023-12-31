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


    # Visit a parse tree produced by pandaQParser#comp_text.
    def visitComp_text(self, ctx:pandaQParser.Comp_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_num.
    def visitComp_num(self, ctx:pandaQParser.Comp_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_text_not.
    def visitComp_text_not(self, ctx:pandaQParser.Comp_text_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_num_not.
    def visitComp_num_not(self, ctx:pandaQParser.Comp_num_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#taula.
    def visitTaula(self, ctx:pandaQParser.TaulaContext):
        return self.visitChildren(ctx)



del pandaQParser