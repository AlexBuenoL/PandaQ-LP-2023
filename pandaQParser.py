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
        4,1,14,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,5,2,25,8,2,10,2,12,2,28,
        9,2,3,2,30,8,2,1,3,1,3,1,3,1,3,1,3,3,3,37,8,3,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,3,4,46,8,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,54,8,4,10,4,12,
        4,57,9,4,1,5,1,5,1,5,0,1,8,6,0,2,4,6,8,10,0,2,2,0,4,4,7,7,1,0,8,
        9,61,0,12,1,0,0,0,2,14,1,0,0,0,4,29,1,0,0,0,6,36,1,0,0,0,8,45,1,
        0,0,0,10,58,1,0,0,0,12,13,3,2,1,0,13,1,1,0,0,0,14,15,5,1,0,0,15,
        16,3,4,2,0,16,17,5,2,0,0,17,18,3,10,5,0,18,19,5,3,0,0,19,3,1,0,0,
        0,20,30,5,4,0,0,21,26,3,6,3,0,22,23,5,5,0,0,23,25,3,6,3,0,24,22,
        1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,30,1,0,0,0,
        28,26,1,0,0,0,29,20,1,0,0,0,29,21,1,0,0,0,30,5,1,0,0,0,31,32,3,8,
        4,0,32,33,5,6,0,0,33,34,5,12,0,0,34,37,1,0,0,0,35,37,5,12,0,0,36,
        31,1,0,0,0,36,35,1,0,0,0,37,7,1,0,0,0,38,39,6,4,-1,0,39,40,5,10,
        0,0,40,41,3,8,4,0,41,42,5,11,0,0,42,46,1,0,0,0,43,46,5,13,0,0,44,
        46,5,12,0,0,45,38,1,0,0,0,45,43,1,0,0,0,45,44,1,0,0,0,46,55,1,0,
        0,0,47,48,10,5,0,0,48,49,7,0,0,0,49,54,3,8,4,6,50,51,10,4,0,0,51,
        52,7,1,0,0,52,54,3,8,4,5,53,47,1,0,0,0,53,50,1,0,0,0,54,57,1,0,0,
        0,55,53,1,0,0,0,55,56,1,0,0,0,56,9,1,0,0,0,57,55,1,0,0,0,58,59,5,
        12,0,0,59,11,1,0,0,0,6,26,29,36,45,53,55
    ]

class pandaQParser ( Parser ):

    grammarFileName = "pandaQ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "';'", "'*'", "','", 
                     "'as'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM", "WS" ]

    RULE_root = 0
    RULE_query = 1
    RULE_camps = 2
    RULE_col = 3
    RULE_expr = 4
    RULE_taula = 5

    ruleNames =  [ "root", "query", "camps", "col", "expr", "taula" ]

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
    ID=12
    NUM=13
    WS=14

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
            self.state = 12
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(pandaQParser.T__0)
            self.state = 15
            self.camps()
            self.state = 16
            self.match(pandaQParser.T__1)
            self.state = 17
            self.taula()
            self.state = 18
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
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(pandaQParser.T__3)
                pass
            elif token in [10, 12, 13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.col()
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==5:
                    self.state = 22
                    self.match(pandaQParser.T__4)
                    self.state = 23
                    self.col()
                    self.state = 28
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

        def expr(self):
            return self.getTypedRuleContext(pandaQParser.ExprContext,0)


        def ID(self):
            return self.getToken(pandaQParser.ID, 0)

        def getRuleIndex(self):
            return pandaQParser.RULE_col

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCol" ):
                return visitor.visitCol(self)
            else:
                return visitor.visitChildren(self)




    def col(self):

        localctx = pandaQParser.ColContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_col)
        try:
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(pandaQParser.T__5)
                self.state = 33
                self.match(pandaQParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
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
            self.state = 45
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.state = 39
                self.match(pandaQParser.T__9)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(pandaQParser.T__10)
                pass
            elif token in [13]:
                self.state = 43
                self.match(pandaQParser.NUM)
                pass
            elif token in [12]:
                self.state = 44
                self.match(pandaQParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 48
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = pandaQParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 50
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 51
                        _la = self._input.LA(1)
                        if not(_la==8 or _la==9):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 52
                        self.expr(5)
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 10, self.RULE_taula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




