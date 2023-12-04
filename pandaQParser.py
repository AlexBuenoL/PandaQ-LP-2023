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
        4,1,7,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,3,2,21,8,2,1,3,1,3,1,3,5,3,26,8,3,10,3,12,
        3,29,9,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,29,0,10,1,0,0,0,2,12,1,
        0,0,0,4,20,1,0,0,0,6,22,1,0,0,0,8,30,1,0,0,0,10,11,3,2,1,0,11,1,
        1,0,0,0,12,13,5,1,0,0,13,14,3,4,2,0,14,15,5,2,0,0,15,16,3,8,4,0,
        16,17,5,3,0,0,17,3,1,0,0,0,18,21,5,4,0,0,19,21,3,6,3,0,20,18,1,0,
        0,0,20,19,1,0,0,0,21,5,1,0,0,0,22,27,5,6,0,0,23,24,5,5,0,0,24,26,
        5,6,0,0,25,23,1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,
        28,7,1,0,0,0,29,27,1,0,0,0,30,31,5,6,0,0,31,9,1,0,0,0,2,20,27
    ]

class pandaQParser ( Parser ):

    grammarFileName = "pandaQ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select'", "'from'", "';'", "'*'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "WS" ]

    RULE_root = 0
    RULE_query = 1
    RULE_camps = 2
    RULE_cols = 3
    RULE_taula = 4

    ruleNames =  [ "root", "query", "camps", "cols", "taula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    WS=7

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
            self.state = 10
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
            self.state = 12
            self.match(pandaQParser.T__0)
            self.state = 13
            self.camps()
            self.state = 14
            self.match(pandaQParser.T__1)
            self.state = 15
            self.taula()
            self.state = 16
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

        def cols(self):
            return self.getTypedRuleContext(pandaQParser.ColsContext,0)


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
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.match(pandaQParser.T__3)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.cols()
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


    class ColsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(pandaQParser.ID)
            else:
                return self.getToken(pandaQParser.ID, i)

        def getRuleIndex(self):
            return pandaQParser.RULE_cols

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCols" ):
                return visitor.visitCols(self)
            else:
                return visitor.visitChildren(self)




    def cols(self):

        localctx = pandaQParser.ColsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_cols)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(pandaQParser.ID)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 23
                self.match(pandaQParser.T__4)
                self.state = 24
                self.match(pandaQParser.ID)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_taula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(pandaQParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





