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


    # Visit a parse tree produced by pandaQParser#assig.
    def visitAssig(self, ctx:pandaQParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#plot.
    def visitPlot(self, ctx:pandaQParser.PlotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#query.
    def visitQuery(self, ctx:pandaQParser.QueryContext):
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


    # Visit a parse tree produced by pandaQParser#join_info.
    def visitJoin_info(self, ctx:pandaQParser.Join_infoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#expr.
    def visitExpr(self, ctx:pandaQParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#orderBy.
    def visitOrderBy(self, ctx:pandaQParser.OrderByContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#asc.
    def visitAsc(self, ctx:pandaQParser.AscContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#desc.
    def visitDesc(self, ctx:pandaQParser.DescContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#where.
    def visitWhere(self, ctx:pandaQParser.WhereContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_text.
    def visitComp_text(self, ctx:pandaQParser.Comp_textContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_num.
    def visitComp_num(self, ctx:pandaQParser.Comp_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#compSQ.
    def visitCompSQ(self, ctx:pandaQParser.CompSQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#subquery.
    def visitSubquery(self, ctx:pandaQParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#whereSQ.
    def visitWhereSQ(self, ctx:pandaQParser.WhereSQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_numSQ.
    def visitComp_numSQ(self, ctx:pandaQParser.Comp_numSQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#comp_textSQ.
    def visitComp_textSQ(self, ctx:pandaQParser.Comp_textSQContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#taula.
    def visitTaula(self, ctx:pandaQParser.TaulaContext):
        return self.visitChildren(ctx)



del pandaQParser