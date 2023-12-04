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
        4,0,7,47,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,
        3,1,3,1,4,1,4,1,5,1,5,5,5,36,8,5,10,5,12,5,39,9,5,1,6,4,6,42,8,6,
        11,6,12,6,43,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,3,3,
        0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,
        32,32,48,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
        0,0,0,11,1,0,0,0,0,13,1,0,0,0,1,15,1,0,0,0,3,22,1,0,0,0,5,27,1,0,
        0,0,7,29,1,0,0,0,9,31,1,0,0,0,11,33,1,0,0,0,13,41,1,0,0,0,15,16,
        5,115,0,0,16,17,5,101,0,0,17,18,5,108,0,0,18,19,5,101,0,0,19,20,
        5,99,0,0,20,21,5,116,0,0,21,2,1,0,0,0,22,23,5,102,0,0,23,24,5,114,
        0,0,24,25,5,111,0,0,25,26,5,109,0,0,26,4,1,0,0,0,27,28,5,59,0,0,
        28,6,1,0,0,0,29,30,5,42,0,0,30,8,1,0,0,0,31,32,5,44,0,0,32,10,1,
        0,0,0,33,37,7,0,0,0,34,36,7,1,0,0,35,34,1,0,0,0,36,39,1,0,0,0,37,
        35,1,0,0,0,37,38,1,0,0,0,38,12,1,0,0,0,39,37,1,0,0,0,40,42,7,2,0,
        0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,45,
        1,0,0,0,45,46,6,6,0,0,46,14,1,0,0,0,3,0,37,43,1,6,0,0
    ]

class pandaQLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    ID = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'select'", "'from'", "';'", "'*'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "ID", "WS" ]

    grammarFileName = "pandaQ.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


