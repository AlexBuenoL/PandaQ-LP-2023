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
        4,1,18,91,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,2,42,9,2,
        3,2,44,8,2,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,61,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,69,8,4,10,4,12,
        4,72,9,4,1,5,1,5,1,5,5,5,77,8,5,10,5,12,5,80,9,5,1,6,1,6,1,6,1,6,
        1,6,3,6,87,8,6,1,7,1,7,1,7,0,1,8,8,0,2,4,6,8,10,12,14,0,2,2,0,5,
        5,8,8,1,0,9,10,94,0,16,1,0,0,0,2,32,1,0,0,0,4,43,1,0,0,0,6,50,1,
        0,0,0,8,60,1,0,0,0,10,73,1,0,0,0,12,86,1,0,0,0,14,88,1,0,0,0,16,
        17,3,2,1,0,17,1,1,0,0,0,18,19,5,1,0,0,19,20,3,4,2,0,20,21,5,2,0,
        0,21,22,3,14,7,0,22,23,5,3,0,0,23,33,1,0,0,0,24,25,5,1,0,0,25,26,
        3,4,2,0,26,27,5,2,0,0,27,28,3,14,7,0,28,29,5,4,0,0,29,30,3,10,5,
        0,30,31,5,3,0,0,31,33,1,0,0,0,32,18,1,0,0,0,32,24,1,0,0,0,33,3,1,
        0,0,0,34,44,5,5,0,0,35,40,3,6,3,0,36,37,5,6,0,0,37,39,3,6,3,0,38,
        36,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,44,1,0,0,
        0,42,40,1,0,0,0,43,34,1,0,0,0,43,35,1,0,0,0,44,5,1,0,0,0,45,46,3,
        8,4,0,46,47,5,7,0,0,47,48,5,15,0,0,48,51,1,0,0,0,49,51,5,15,0,0,
        50,45,1,0,0,0,50,49,1,0,0,0,51,7,1,0,0,0,52,53,6,4,-1,0,53,54,5,
        11,0,0,54,55,3,8,4,0,55,56,5,12,0,0,56,61,1,0,0,0,57,61,5,16,0,0,
        58,61,5,17,0,0,59,61,5,15,0,0,60,52,1,0,0,0,60,57,1,0,0,0,60,58,
        1,0,0,0,60,59,1,0,0,0,61,70,1,0,0,0,62,63,10,6,0,0,63,64,7,0,0,0,
        64,69,3,8,4,7,65,66,10,5,0,0,66,67,7,1,0,0,67,69,3,8,4,6,68,62,1,
        0,0,0,68,65,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,
        9,1,0,0,0,72,70,1,0,0,0,73,78,3,12,6,0,74,75,5,6,0,0,75,77,3,12,
        6,0,76,74,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,11,
        1,0,0,0,80,78,1,0,0,0,81,87,5,15,0,0,82,83,5,15,0,0,83,87,5,13,0,
        0,84,85,5,15,0,0,85,87,5,14,0,0,86,81,1,0,0,0,86,82,1,0,0,0,86,84,
        1,0,0,0,87,13,1,0,0,0,88,89,5,15,0,0,89,15,1,0,0,0,9,32,40,43,50,
        60,68,70,78,86
    ]

class pandaQParser ( Parser ):

    grammarFileName = "pandaQ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "';'", "'order by'", 
                     "'*'", "','", "' as '", "'/'", "'+'", "'-'", "'('", 
                     "')'", "'asc'", "'desc'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "NUM", 
                      "DECIMAL", "WS" ]

    RULE_root = 0
    RULE_query = 1
    RULE_camps = 2
    RULE_col = 3
    RULE_expr = 4
    RULE_order = 5
    RULE_camp_order = 6
    RULE_taula = 7

    ruleNames =  [ "root", "query", "camps", "col", "expr", "order", "camp_order", 
                   "taula" ]

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
    ID=15
    NUM=16
    DECIMAL=17
    WS=18

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
            self.state = 16
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



    def query(self):

        localctx = pandaQParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_query)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.SelectNormalContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(pandaQParser.T__0)
                self.state = 19
                self.camps()
                self.state = 20
                self.match(pandaQParser.T__1)
                self.state = 21
                self.taula()
                self.state = 22
                self.match(pandaQParser.T__2)
                pass

            elif la_ == 2:
                localctx = pandaQParser.SelectOrderContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(pandaQParser.T__0)
                self.state = 25
                self.camps()
                self.state = 26
                self.match(pandaQParser.T__1)
                self.state = 27
                self.taula()
                self.state = 28
                self.match(pandaQParser.T__3)
                self.state = 29
                self.order()
                self.state = 30
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
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(pandaQParser.T__4)
                pass
            elif token in [11, 15, 16, 17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.col()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==6:
                    self.state = 36
                    self.match(pandaQParser.T__5)
                    self.state = 37
                    self.col()
                    self.state = 42
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
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.CampCalculatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.expr(0)
                self.state = 46
                self.match(pandaQParser.T__6)
                self.state = 47
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.CampContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 49
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
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.state = 53
                self.match(pandaQParser.T__10)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(pandaQParser.T__11)
                pass
            elif token in [16]:
                self.state = 57
                self.match(pandaQParser.NUM)
                pass
            elif token in [17]:
                self.state = 58
                self.match(pandaQParser.DECIMAL)
                pass
            elif token in [15]:
                self.state = 59
                self.match(pandaQParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 68
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 62
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 63
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==8):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 64
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 65
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 66
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expr(6)
                        pass

             
                self.state = 72
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
            self.state = 73
            self.camp_order()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 74
                self.match(pandaQParser.T__5)
                self.state = 75
                self.camp_order()
                self.state = 80
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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = pandaQParser.AscContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                localctx = pandaQParser.AscContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 82
                self.match(pandaQParser.ID)

                self.state = 83
                self.match(pandaQParser.T__12)
                pass

            elif la_ == 3:
                localctx = pandaQParser.DescContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 84
                self.match(pandaQParser.ID)
                self.state = 85
                self.match(pandaQParser.T__13)
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
        self.enterRule(localctx, 14, self.RULE_taula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
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
         




