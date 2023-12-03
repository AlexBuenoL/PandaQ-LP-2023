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
        4,1,4,11,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,2,0,2,0,
        0,8,0,4,1,0,0,0,2,6,1,0,0,0,4,5,3,2,1,0,5,1,1,0,0,0,6,7,5,1,0,0,
        7,8,5,3,0,0,8,9,5,2,0,0,9,3,1,0,0,0,0
    ]

class pandaQParser ( Parser ):

    grammarFileName = "pandaQ.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'select * from'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "TABLE", "WS" ]

    RULE_root = 0
    RULE_query = 1

    ruleNames =  [ "root", "query" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    TABLE=3
    WS=4

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
            self.state = 4
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

        def TABLE(self):
            return self.getToken(pandaQParser.TABLE, 0)

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
            self.state = 6
            self.match(pandaQParser.T__0)
            self.state = 7
            self.match(pandaQParser.TABLE)
            self.state = 8
            self.match(pandaQParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





