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
        4,1,23,131,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,45,
        8,1,1,2,1,2,1,2,1,2,5,2,51,8,2,10,2,12,2,54,9,2,3,2,56,8,2,1,3,1,
        3,1,3,1,3,1,3,3,3,63,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,73,
        8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,81,8,4,10,4,12,4,84,9,4,1,5,1,5,
        1,5,5,5,89,8,5,10,5,12,5,92,9,5,1,6,1,6,1,6,1,6,1,6,3,6,99,8,6,1,
        7,1,7,1,7,5,7,104,8,7,10,7,12,7,107,9,7,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,3,8,116,8,8,1,8,1,8,1,8,1,8,3,8,122,8,8,1,8,1,8,1,8,3,8,127,
        8,8,1,9,1,9,1,9,0,1,8,10,0,2,4,6,8,10,12,14,16,18,0,3,2,0,6,6,9,
        9,1,0,10,11,1,0,17,18,139,0,20,1,0,0,0,2,44,1,0,0,0,4,55,1,0,0,0,
        6,62,1,0,0,0,8,72,1,0,0,0,10,85,1,0,0,0,12,98,1,0,0,0,14,100,1,0,
        0,0,16,126,1,0,0,0,18,128,1,0,0,0,20,21,3,2,1,0,21,1,1,0,0,0,22,
        23,5,1,0,0,23,24,3,4,2,0,24,25,5,2,0,0,25,26,3,18,9,0,26,27,5,3,
        0,0,27,45,1,0,0,0,28,29,5,1,0,0,29,30,3,4,2,0,30,31,5,2,0,0,31,32,
        3,18,9,0,32,33,5,4,0,0,33,34,3,10,5,0,34,35,5,3,0,0,35,45,1,0,0,
        0,36,37,5,1,0,0,37,38,3,4,2,0,38,39,5,2,0,0,39,40,3,18,9,0,40,41,
        5,5,0,0,41,42,3,14,7,0,42,43,5,3,0,0,43,45,1,0,0,0,44,22,1,0,0,0,
        44,28,1,0,0,0,44,36,1,0,0,0,45,3,1,0,0,0,46,56,5,6,0,0,47,52,3,6,
        3,0,48,49,5,7,0,0,49,51,3,6,3,0,50,48,1,0,0,0,51,54,1,0,0,0,52,50,
        1,0,0,0,52,53,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,55,46,1,0,0,0,
        55,47,1,0,0,0,56,5,1,0,0,0,57,58,3,8,4,0,58,59,5,8,0,0,59,60,5,20,
        0,0,60,63,1,0,0,0,61,63,5,20,0,0,62,57,1,0,0,0,62,61,1,0,0,0,63,
        7,1,0,0,0,64,65,6,4,-1,0,65,66,5,12,0,0,66,67,3,8,4,0,67,68,5,13,
        0,0,68,73,1,0,0,0,69,73,5,21,0,0,70,73,5,22,0,0,71,73,5,20,0,0,72,
        64,1,0,0,0,72,69,1,0,0,0,72,70,1,0,0,0,72,71,1,0,0,0,73,82,1,0,0,
        0,74,75,10,6,0,0,75,76,7,0,0,0,76,81,3,8,4,7,77,78,10,5,0,0,78,79,
        7,1,0,0,79,81,3,8,4,6,80,74,1,0,0,0,80,77,1,0,0,0,81,84,1,0,0,0,
        82,80,1,0,0,0,82,83,1,0,0,0,83,9,1,0,0,0,84,82,1,0,0,0,85,90,3,12,
        6,0,86,87,5,7,0,0,87,89,3,12,6,0,88,86,1,0,0,0,89,92,1,0,0,0,90,
        88,1,0,0,0,90,91,1,0,0,0,91,11,1,0,0,0,92,90,1,0,0,0,93,99,5,20,
        0,0,94,95,5,20,0,0,95,99,5,14,0,0,96,97,5,20,0,0,97,99,5,15,0,0,
        98,93,1,0,0,0,98,94,1,0,0,0,98,96,1,0,0,0,99,13,1,0,0,0,100,105,
        3,16,8,0,101,102,5,16,0,0,102,104,3,16,8,0,103,101,1,0,0,0,104,107,
        1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,15,1,0,0,0,107,105,1,
        0,0,0,108,109,5,20,0,0,109,110,7,2,0,0,110,127,5,20,0,0,111,112,
        5,20,0,0,112,113,7,2,0,0,113,127,5,21,0,0,114,116,5,19,0,0,115,114,
        1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,118,5,20,0,0,118,119,
        7,2,0,0,119,127,5,20,0,0,120,122,5,19,0,0,121,120,1,0,0,0,121,122,
        1,0,0,0,122,123,1,0,0,0,123,124,5,20,0,0,124,125,7,2,0,0,125,127,
        5,21,0,0,126,108,1,0,0,0,126,111,1,0,0,0,126,115,1,0,0,0,126,121,
        1,0,0,0,127,17,1,0,0,0,128,129,5,20,0,0,129,19,1,0,0,0,13,44,52,
        55,62,72,80,82,90,98,105,115,121,126
    ]

class pandaQParser ( Parser ):

    grammarFileName = "pandaQ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "';'", "'order by'", 
                     "'where'", "'*'", "','", "' as '", "'/'", "'+'", "'-'", 
                     "'('", "')'", "'asc'", "'desc'", "'and'", "'<'", "'='", 
                     "'not'" ]

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
    RULE_order = 5
    RULE_camp_order = 6
    RULE_conds_where = 7
    RULE_cond = 8
    RULE_taula = 9

    ruleNames =  [ "root", "query", "camps", "col", "expr", "order", "camp_order", 
                   "conds_where", "cond", "taula" ]

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
            self.state = 20
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


        def getRuleIndex(self):
            return pandaQParser.RULE_query

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SelectNormalContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def camps(self):
            return self.getTypedRuleContext(pandaQParser.CampsContext,0)

        def taula(self):
            return self.getTypedRuleContext(pandaQParser.TaulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectNormal" ):
                return visitor.visitSelectNormal(self)
            else:
                return visitor.visitChildren(self)


    class SelectOrderContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def camps(self):
            return self.getTypedRuleContext(pandaQParser.CampsContext,0)

        def taula(self):
            return self.getTypedRuleContext(pandaQParser.TaulaContext,0)

        def order(self):
            return self.getTypedRuleContext(pandaQParser.OrderContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectOrder" ):
                return visitor.visitSelectOrder(self)
            else:
                return visitor.visitChildren(self)


    class SelectWhereContext(QueryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.QueryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def camps(self):
            return self.getTypedRuleContext(pandaQParser.CampsContext,0)

        def taula(self):
            return self.getTypedRuleContext(pandaQParser.TaulaContext,0)

        def conds_where(self):
            return self.getTypedRuleContext(pandaQParser.Conds_whereContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectWhere" ):
                return visitor.visitSelectWhere(self)
            else:
                return visitor.visitChildren(self)



    def query(self):

        localctx = pandaQParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.SelectNormalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(pandaQParser.T__0)
                self.state = 23
                self.camps()
                self.state = 24
                self.match(pandaQParser.T__1)
                self.state = 25
                self.taula()
                self.state = 26
                self.match(pandaQParser.T__2)
                pass

            elif la_ == 2:
                localctx = pandaQParser.SelectOrderContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(pandaQParser.T__0)
                self.state = 29
                self.camps()
                self.state = 30
                self.match(pandaQParser.T__1)
                self.state = 31
                self.taula()
                self.state = 32
                self.match(pandaQParser.T__3)
                self.state = 33
                self.order()
                self.state = 34
                self.match(pandaQParser.T__2)
                pass

            elif la_ == 3:
                localctx = pandaQParser.SelectWhereContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 36
                self.match(pandaQParser.T__0)
                self.state = 37
                self.camps()
                self.state = 38
                self.match(pandaQParser.T__1)
                self.state = 39
                self.taula()
                self.state = 40
                self.match(pandaQParser.T__4)
                self.state = 41
                self.conds_where()
                self.state = 42
                self.match(pandaQParser.T__2)
                pass


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
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.match(pandaQParser.T__5)
                pass
            elif token in [12, 20, 21, 22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.col()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 48
                    self.match(pandaQParser.T__6)
                    self.state = 49
                    self.col()
                    self.state = 54
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
            self.state = 62
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.CampCalculatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(pandaQParser.T__7)
                self.state = 59
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.CampContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
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
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 65
                self.match(pandaQParser.T__11)
                self.state = 66
                self.expr(0)
                self.state = 67
                self.match(pandaQParser.T__12)
                pass
            elif token in [21]:
                self.state = 69
                self.match(pandaQParser.NUM)
                pass
            elif token in [22]:
                self.state = 70
                self.match(pandaQParser.DECIMAL)
                pass
            elif token in [20]:
                self.state = 71
                self.match(pandaQParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 80
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 74
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 75
                        _la = self._input.LA(1)
                        if not(_la==6 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 76
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 78
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 79
                        self.expr(6)
                        pass

             
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 10, self.RULE_order)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.camp_order()
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 86
                self.match(pandaQParser.T__6)
                self.state = 87
                self.camp_order()
                self.state = 92
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
        self.enterRule(localctx, 12, self.RULE_camp_order)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.AscContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.AscContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(pandaQParser.ID)
                self.state = 95
                self.match(pandaQParser.T__13)
                pass

            elif la_ == 3:
                localctx = pandaQParser.DescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(pandaQParser.ID)
                self.state = 97
                self.match(pandaQParser.T__14)
                pass


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
        self.enterRule(localctx, 14, self.RULE_conds_where)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.cond()
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==16:
                self.state = 101
                self.match(pandaQParser.T__15)
                self.state = 102
                self.cond()
                self.state = 107
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


    class Comp_num_notContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(pandaQParser.ID, 0)
        def NUM(self):
            return self.getToken(pandaQParser.NUM, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_num_not" ):
                return visitor.visitComp_num_not(self)
            else:
                return visitor.visitChildren(self)


    class Comp_text_notContext(CondContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a pandaQParser.CondContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pandaQParser.ID)
            else:
                return self.getToken(pandaQParser.ID, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComp_text_not" ):
                return visitor.visitComp_text_not(self)
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
        self.enterRule(localctx, 16, self.RULE_cond)
        self._la = 0 # Token type
        try:
            self.state = 126
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.Comp_textContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(pandaQParser.ID)
                self.state = 109
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 110
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.Comp_numContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.match(pandaQParser.ID)
                self.state = 112
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 113
                self.match(pandaQParser.NUM)
                pass

            elif la_ == 3:
                localctx = pandaQParser.Comp_text_notContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 114
                    self.match(pandaQParser.T__18)


                self.state = 117
                self.match(pandaQParser.ID)
                self.state = 118
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 119
                self.match(pandaQParser.ID)
                pass

            elif la_ == 4:
                localctx = pandaQParser.Comp_num_notContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 120
                    self.match(pandaQParser.T__18)


                self.state = 123
                self.match(pandaQParser.ID)
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 125
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
        self.enterRule(localctx, 18, self.RULE_taula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
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
         




