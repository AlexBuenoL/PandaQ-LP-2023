# Generated from pandaQ.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,39,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,5,2,28,8,2,
        10,2,12,2,31,9,2,1,3,4,3,34,8,3,11,3,12,3,35,1,3,1,3,0,0,4,1,1,3,
        2,5,3,7,4,1,0,3,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,
        122,3,0,9,10,13,13,32,32,40,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,
        0,7,1,0,0,0,1,9,1,0,0,0,3,23,1,0,0,0,5,25,1,0,0,0,7,33,1,0,0,0,9,
        10,5,115,0,0,10,11,5,101,0,0,11,12,5,108,0,0,12,13,5,101,0,0,13,
        14,5,99,0,0,14,15,5,116,0,0,15,16,5,32,0,0,16,17,5,42,0,0,17,18,
        5,32,0,0,18,19,5,102,0,0,19,20,5,114,0,0,20,21,5,111,0,0,21,22,5,
        109,0,0,22,2,1,0,0,0,23,24,5,59,0,0,24,4,1,0,0,0,25,29,7,0,0,0,26,
        28,7,1,0,0,27,26,1,0,0,0,28,31,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,
        0,30,6,1,0,0,0,31,29,1,0,0,0,32,34,7,2,0,0,33,32,1,0,0,0,34,35,1,
        0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,6,3,0,0,38,
        8,1,0,0,0,3,0,29,35,1,6,0,0
    ]

class pandaQLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    TABLE = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'select * from'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "TABLE", "WS" ]

    ruleNames = [ "T__0", "T__1", "TABLE", "WS" ]

    grammarFileName = "pandaQ.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


