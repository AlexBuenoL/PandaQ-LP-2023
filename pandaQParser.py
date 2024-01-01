# Generated from pandaQ.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,123,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,3,1,32,8,1,1,1,3,1,35,8,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,
        43,8,2,10,2,12,2,46,9,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,3,3,55,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,65,8,4,1,4,1,4,1,4,1,4,1,4,
        1,4,5,4,73,8,4,10,4,12,4,76,9,4,1,5,1,5,1,5,1,6,1,6,1,6,5,6,84,8,
        6,10,6,12,6,87,9,6,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,8,1,8,1,8,1,
        9,1,9,1,9,5,9,102,8,9,10,9,12,9,105,9,9,1,10,3,10,108,8,10,1,10,
        1,10,1,10,1,10,3,10,114,8,10,1,10,1,10,1,10,3,10,119,8,10,1,11,1,
        11,1,11,0,1,8,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,2,0,4,4,7,7,
        1,0,8,9,1,0,18,19,127,0,24,1,0,0,0,2,26,1,0,0,0,4,47,1,0,0,0,6,54,
        1,0,0,0,8,64,1,0,0,0,10,77,1,0,0,0,12,80,1,0,0,0,14,93,1,0,0,0,16,
        95,1,0,0,0,18,98,1,0,0,0,20,118,1,0,0,0,22,120,1,0,0,0,24,25,3,2,
        1,0,25,1,1,0,0,0,26,27,5,1,0,0,27,28,3,4,2,0,28,29,5,2,0,0,29,31,
        3,22,11,0,30,32,3,16,8,0,31,30,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,
        0,33,35,3,10,5,0,34,33,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,
        5,3,0,0,37,3,1,0,0,0,38,48,5,4,0,0,39,44,3,6,3,0,40,41,5,5,0,0,41,
        43,3,6,3,0,42,40,1,0,0,0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,
        0,45,48,1,0,0,0,46,44,1,0,0,0,47,38,1,0,0,0,47,39,1,0,0,0,48,5,1,
        0,0,0,49,50,3,8,4,0,50,51,5,6,0,0,51,52,5,20,0,0,52,55,1,0,0,0,53,
        55,5,20,0,0,54,49,1,0,0,0,54,53,1,0,0,0,55,7,1,0,0,0,56,57,6,4,-1,
        0,57,58,5,10,0,0,58,59,3,8,4,0,59,60,5,11,0,0,60,65,1,0,0,0,61,65,
        5,21,0,0,62,65,5,22,0,0,63,65,5,20,0,0,64,56,1,0,0,0,64,61,1,0,0,
        0,64,62,1,0,0,0,64,63,1,0,0,0,65,74,1,0,0,0,66,67,10,6,0,0,67,68,
        7,0,0,0,68,73,3,8,4,7,69,70,10,5,0,0,70,71,7,1,0,0,71,73,3,8,4,6,
        72,66,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,
        0,0,0,75,9,1,0,0,0,76,74,1,0,0,0,77,78,5,12,0,0,78,79,3,12,6,0,79,
        11,1,0,0,0,80,85,3,14,7,0,81,82,5,5,0,0,82,84,3,14,7,0,83,81,1,0,
        0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,13,1,0,0,0,87,85,
        1,0,0,0,88,94,5,20,0,0,89,90,5,20,0,0,90,94,5,13,0,0,91,92,5,20,
        0,0,92,94,5,14,0,0,93,88,1,0,0,0,93,89,1,0,0,0,93,91,1,0,0,0,94,
        15,1,0,0,0,95,96,5,15,0,0,96,97,3,18,9,0,97,17,1,0,0,0,98,103,3,
        20,10,0,99,100,5,16,0,0,100,102,3,20,10,0,101,99,1,0,0,0,102,105,
        1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,19,1,0,0,0,105,103,1,
        0,0,0,106,108,5,17,0,0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,
        0,0,0,109,110,5,20,0,0,110,111,7,2,0,0,111,119,5,20,0,0,112,114,
        5,17,0,0,113,112,1,0,0,0,113,114,1,0,0,0,114,115,1,0,0,0,115,116,
        5,20,0,0,116,117,7,2,0,0,117,119,5,21,0,0,118,107,1,0,0,0,118,113,
        1,0,0,0,119,21,1,0,0,0,120,121,5,20,0,0,121,23,1,0,0,0,14,31,34,
        44,47,54,64,72,74,85,93,103,107,113,118
    ]

class pandaQParser ( Parser ):

    grammarFileName = "pandaQ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "';'", "'*'", "','", 
                     "' as '", "'/'", "'+'", "'-'", "'('", "')'", "'order by'", 
                     "'asc'", "'desc'", "'where'", "'and'", "'not'", "'<'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM", "DECIMAL", "WS" ]

    RULE_root = 0
    RULE_query = 1
    RULE_camps = 2
    RULE_col = 3
    RULE_expr = 4
    RULE_orderBy = 5
    RULE_order = 6
    RULE_camp_order = 7
    RULE_where = 8
    RULE_conds_where = 9
    RULE_cond = 10
    RULE_taula = 11

    ruleNames =  [ "root", "query", "camps", "col", "expr", "orderBy", "order", 
                   "camp_order", "where", "conds_where", "cond", "taula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    ID=20
    NUM=21
    DECIMAL=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def query(self):
            return self.getTypedRuleContext(pandaQParser.QueryContext,0)


        def getRuleIndex(self):
            return pandaQParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = pandaQParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.query()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def camps(self):
            return self.getTypedRuleContext(pandaQParser.CampsContext,0)


        def taula(self):
            return self.getTypedRuleContext(pandaQParser.TaulaContext,0)


        def where(self):
            return self.getTypedRuleContext(pandaQParser.WhereContext,0)


        def orderBy(self):
            return self.getTypedRuleContext(pandaQParser.OrderByContext,0)


        def getRuleIndex(self):
            return pandaQParser.RULE_query

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuery" ):
                return visitor.visitQuery(self)
            else:
                return visitor.visitChildren(self)




    def query(self):

        localctx = pandaQParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(pandaQParser.T__0)
            self.state = 27
            self.camps()
            self.state = 28
            self.match(pandaQParser.T__1)
            self.state = 29
            self.taula()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 30
                self.where()


            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 33
                self.orderBy()


            self.state = 36
            self.match(pandaQParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pandaQParser.ColContext)
            else:
                return self.getTypedRuleContext(pandaQParser.ColContext,i)


        def getRuleIndex(self):
            return pandaQParser.RULE_camps

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCamps" ):
                return visitor.visitCamps(self)
            else:
                return visitor.visitChildren(self)




    def camps(self):

        localctx = pandaQParser.CampsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_camps)
        self._la = 0 # Token type
        try:
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(pandaQParser.T__3)
                pass
            elif token in [10, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.col()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 40
                    self.match(pandaQParser.T__4)
                    self.state = 41
                    self.col()
                    self.state = 46
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pandaQParser.RULE_col

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CampCalculatContext(ColContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.ColContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(pandaQParser.ExprContext,0)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCampCalculat" ):
                return visitor.visitCampCalculat(self)
            else:
                return visitor.visitChildren(self)


    class CampContext(ColContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.ColContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCamp" ):
                return visitor.visitCamp(self)
            else:
                return visitor.visitChildren(self)



    def col(self):

        localctx = pandaQParser.ColContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_col)
        try:
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.CampCalculatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(pandaQParser.T__5)
                self.state = 51
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.CampContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(pandaQParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pandaQParser.ExprContext)
            else:
                return self.getTypedRuleContext(pandaQParser.ExprContext,i)


        def NUM(self):
            return self.getToken(pandaQParser.NUM, 0)

        def DECIMAL(self):
            return self.getToken(pandaQParser.DECIMAL, 0)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def getRuleIndex(self):
            return pandaQParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = pandaQParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 57
                self.match(pandaQParser.T__9)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(pandaQParser.T__10)
                pass
            elif token in [21]:
                self.state = 61
                self.match(pandaQParser.NUM)
                pass
            elif token in [22]:
                self.state = 62
                self.match(pandaQParser.DECIMAL)
                pass
            elif token in [20]:
                self.state = 63
                self.match(pandaQParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 67
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 70
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expr(6)
                        pass

             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OrderByContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def order(self):
            return self.getTypedRuleContext(pandaQParser.OrderContext,0)


        def getRuleIndex(self):
            return pandaQParser.RULE_orderBy

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderBy" ):
                return visitor.visitOrderBy(self)
            else:
                return visitor.visitChildren(self)




    def orderBy(self):

        localctx = pandaQParser.OrderByContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_orderBy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(pandaQParser.T__11)
            self.state = 78
            self.order()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def camp_order(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pandaQParser.Camp_orderContext)
            else:
                return self.getTypedRuleContext(pandaQParser.Camp_orderContext,i)


        def getRuleIndex(self):
            return pandaQParser.RULE_order

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrder" ):
                return visitor.visitOrder(self)
            else:
                return visitor.visitChildren(self)




    def order(self):

        localctx = pandaQParser.OrderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_order)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.camp_order()
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 81
                self.match(pandaQParser.T__4)
                self.state = 82
                self.camp_order()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Camp_orderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pandaQParser.RULE_camp_order

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AscContext(Camp_orderContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.Camp_orderContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsc" ):
                return visitor.visitAsc(self)
            else:
                return visitor.visitChildren(self)


    class DescContext(Camp_orderContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.Camp_orderContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDesc" ):
                return visitor.visitDesc(self)
            else:
                return visitor.visitChildren(self)



    def camp_order(self):

        localctx = pandaQParser.Camp_orderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_camp_order)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.AscContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.AscContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.match(pandaQParser.ID)
                self.state = 90
                self.match(pandaQParser.T__12)
                pass

            elif la_ == 3:
                localctx = pandaQParser.DescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(pandaQParser.ID)
                self.state = 92
                self.match(pandaQParser.T__13)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conds_where(self):
            return self.getTypedRuleContext(pandaQParser.Conds_whereContext,0)


        def getRuleIndex(self):
            return pandaQParser.RULE_where

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhere" ):
                return visitor.visitWhere(self)
            else:
                return visitor.visitChildren(self)




    def where(self):

        localctx = pandaQParser.WhereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_where)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(pandaQParser.T__14)
            self.state = 96
            self.conds_where()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Conds_whereContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(pandaQParser.CondContext)
            else:
                return self.getTypedRuleContext(pandaQParser.CondContext,i)


        def getRuleIndex(self):
            return pandaQParser.RULE_conds_where

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConds_where" ):
                return visitor.visitConds_where(self)
            else:
                return visitor.visitChildren(self)




    def conds_where(self):

        localctx = pandaQParser.Conds_whereContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_conds_where)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.cond()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 99
                self.match(pandaQParser.T__15)
                self.state = 100
                self.cond()
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return pandaQParser.RULE_cond

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Comp_numContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)
        def NUM(self):
            return self.getToken(pandaQParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_num" ):
                return visitor.visitComp_num(self)
            else:
                return visitor.visitChildren(self)


    class Comp_textContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pandaQParser.ID)
            else:
                return self.getToken(pandaQParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_text" ):
                return visitor.visitComp_text(self)
            else:
                return visitor.visitChildren(self)



    def cond(self):

        localctx = pandaQParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.Comp_textContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 106
                    self.match(pandaQParser.T__16)


                self.state = 109
                self.match(pandaQParser.ID)
                self.state = 110
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 111
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.Comp_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 112
                    self.match(pandaQParser.T__16)


                self.state = 115
                self.match(pandaQParser.ID)
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.match(pandaQParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TaulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def getRuleIndex(self):
            return pandaQParser.RULE_taula

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTaula" ):
                return visitor.visitTaula(self)
            else:
                return visitor.visitChildren(self)




    def taula(self):

        localctx = pandaQParser.TaulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_taula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(pandaQParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




