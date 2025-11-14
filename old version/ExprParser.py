# Generated from ExprParser.g4 by ANTLR 4.13.2
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
        4,1,53,233,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,1,0,5,0,40,8,0,
        10,0,12,0,43,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,3,1,60,8,1,1,1,1,1,1,1,1,1,1,1,3,1,67,8,1,1,2,1,2,1,
        2,1,2,1,2,3,2,74,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        3,4,87,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,99,8,6,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,116,
        8,8,10,8,12,8,119,9,8,1,8,1,8,3,8,123,8,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,3,10,136,8,10,1,10,1,10,3,10,140,8,10,
        1,10,1,10,3,10,144,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,
        153,8,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,161,8,12,1,12,1,12,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,3,13,182,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,5,13,196,8,13,10,13,12,13,199,9,13,1,
        14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,5,16,211,8,16,10,
        16,12,16,214,9,16,1,17,1,17,1,17,5,17,219,8,17,10,17,12,17,222,9,
        17,1,18,1,18,5,18,226,8,18,10,18,12,18,229,9,18,1,18,1,18,1,18,0,
        1,26,19,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,0,6,
        1,0,18,19,1,0,20,22,1,0,24,29,1,0,32,33,1,0,12,15,2,0,16,17,45,48,
        252,0,41,1,0,0,0,2,66,1,0,0,0,4,68,1,0,0,0,6,77,1,0,0,0,8,86,1,0,
        0,0,10,90,1,0,0,0,12,94,1,0,0,0,14,100,1,0,0,0,16,104,1,0,0,0,18,
        124,1,0,0,0,20,130,1,0,0,0,22,148,1,0,0,0,24,157,1,0,0,0,26,181,
        1,0,0,0,28,200,1,0,0,0,30,202,1,0,0,0,32,204,1,0,0,0,34,215,1,0,
        0,0,36,223,1,0,0,0,38,40,3,2,1,0,39,38,1,0,0,0,40,43,1,0,0,0,41,
        39,1,0,0,0,41,42,1,0,0,0,42,44,1,0,0,0,43,41,1,0,0,0,44,45,5,0,0,
        1,45,1,1,0,0,0,46,67,3,4,2,0,47,67,3,6,3,0,48,67,3,8,4,0,49,67,3,
        14,7,0,50,67,3,16,8,0,51,67,3,18,9,0,52,67,3,20,10,0,53,67,3,22,
        11,0,54,55,3,24,12,0,55,56,5,39,0,0,56,67,1,0,0,0,57,59,5,7,0,0,
        58,60,3,26,13,0,59,58,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,67,
        5,39,0,0,62,63,5,9,0,0,63,67,5,39,0,0,64,65,5,10,0,0,65,67,5,39,
        0,0,66,46,1,0,0,0,66,47,1,0,0,0,66,48,1,0,0,0,66,49,1,0,0,0,66,50,
        1,0,0,0,66,51,1,0,0,0,66,52,1,0,0,0,66,53,1,0,0,0,66,54,1,0,0,0,
        66,57,1,0,0,0,66,62,1,0,0,0,66,64,1,0,0,0,67,3,1,0,0,0,68,69,5,8,
        0,0,69,70,3,28,14,0,70,73,5,49,0,0,71,72,5,23,0,0,72,74,3,26,13,
        0,73,71,1,0,0,0,73,74,1,0,0,0,74,75,1,0,0,0,75,76,5,39,0,0,76,5,
        1,0,0,0,77,78,5,49,0,0,78,79,5,23,0,0,79,80,3,26,13,0,80,81,5,39,
        0,0,81,7,1,0,0,0,82,83,5,49,0,0,83,87,5,30,0,0,84,85,5,49,0,0,85,
        87,5,31,0,0,86,82,1,0,0,0,86,84,1,0,0,0,87,88,1,0,0,0,88,89,5,39,
        0,0,89,9,1,0,0,0,90,91,5,49,0,0,91,92,5,23,0,0,92,93,3,26,13,0,93,
        11,1,0,0,0,94,95,3,28,14,0,95,98,5,49,0,0,96,97,5,23,0,0,97,99,3,
        26,13,0,98,96,1,0,0,0,98,99,1,0,0,0,99,13,1,0,0,0,100,101,5,44,0,
        0,101,102,3,26,13,0,102,103,5,39,0,0,103,15,1,0,0,0,104,105,5,1,
        0,0,105,106,5,35,0,0,106,107,3,26,13,0,107,108,5,36,0,0,108,117,
        3,36,18,0,109,110,5,3,0,0,110,111,5,35,0,0,111,112,3,26,13,0,112,
        113,5,36,0,0,113,114,3,36,18,0,114,116,1,0,0,0,115,109,1,0,0,0,116,
        119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,122,1,0,0,0,119,
        117,1,0,0,0,120,121,5,2,0,0,121,123,3,36,18,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,17,1,0,0,0,124,125,5,4,0,0,125,126,5,35,0,0,126,
        127,3,26,13,0,127,128,5,36,0,0,128,129,3,36,18,0,129,19,1,0,0,0,
        130,131,5,5,0,0,131,135,5,35,0,0,132,136,3,4,2,0,133,136,3,12,6,
        0,134,136,3,10,5,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,
        0,135,136,1,0,0,0,136,137,1,0,0,0,137,139,5,39,0,0,138,140,3,26,
        13,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,143,5,39,
        0,0,142,144,3,26,13,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,1,
        0,0,0,145,146,5,36,0,0,146,147,3,36,18,0,147,21,1,0,0,0,148,149,
        5,6,0,0,149,150,5,49,0,0,150,152,5,35,0,0,151,153,3,32,16,0,152,
        151,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,155,5,36,0,0,155,
        156,3,36,18,0,156,23,1,0,0,0,157,158,5,49,0,0,158,160,5,35,0,0,159,
        161,3,34,17,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,
        163,5,36,0,0,163,25,1,0,0,0,164,165,6,13,-1,0,165,166,5,49,0,0,166,
        167,5,23,0,0,167,182,3,26,13,12,168,169,5,34,0,0,169,182,3,26,13,
        7,170,171,5,35,0,0,171,172,3,26,13,0,172,173,5,36,0,0,173,182,1,
        0,0,0,174,182,3,24,12,0,175,176,5,49,0,0,176,182,5,30,0,0,177,178,
        5,49,0,0,178,182,5,31,0,0,179,182,3,30,15,0,180,182,5,49,0,0,181,
        164,1,0,0,0,181,168,1,0,0,0,181,170,1,0,0,0,181,174,1,0,0,0,181,
        175,1,0,0,0,181,177,1,0,0,0,181,179,1,0,0,0,181,180,1,0,0,0,182,
        197,1,0,0,0,183,184,10,11,0,0,184,185,7,0,0,0,185,196,3,26,13,12,
        186,187,10,10,0,0,187,188,7,1,0,0,188,196,3,26,13,11,189,190,10,
        9,0,0,190,191,7,2,0,0,191,196,3,26,13,10,192,193,10,8,0,0,193,194,
        7,3,0,0,194,196,3,26,13,9,195,183,1,0,0,0,195,186,1,0,0,0,195,189,
        1,0,0,0,195,192,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,
        1,0,0,0,198,27,1,0,0,0,199,197,1,0,0,0,200,201,7,4,0,0,201,29,1,
        0,0,0,202,203,7,5,0,0,203,31,1,0,0,0,204,205,3,28,14,0,205,212,5,
        49,0,0,206,207,5,40,0,0,207,208,3,28,14,0,208,209,5,49,0,0,209,211,
        1,0,0,0,210,206,1,0,0,0,211,214,1,0,0,0,212,210,1,0,0,0,212,213,
        1,0,0,0,213,33,1,0,0,0,214,212,1,0,0,0,215,220,3,26,13,0,216,217,
        5,40,0,0,217,219,3,26,13,0,218,216,1,0,0,0,219,222,1,0,0,0,220,218,
        1,0,0,0,220,221,1,0,0,0,221,35,1,0,0,0,222,220,1,0,0,0,223,227,5,
        37,0,0,224,226,3,2,1,0,225,224,1,0,0,0,226,229,1,0,0,0,227,225,1,
        0,0,0,227,228,1,0,0,0,228,230,1,0,0,0,229,227,1,0,0,0,230,231,5,
        38,0,0,231,37,1,0,0,0,19,41,59,66,73,86,98,117,122,135,139,143,152,
        160,181,195,197,212,220,227
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ediwow'", "'edi'", "'ediAno'", "'weh'", 
                     "'sakalam'", "'buhat'", "'uwianNa'", "'lods'", "'charot'", 
                     "'padayon'", "'forever'", "'bilang'", "'dobols'", "'emoji'", 
                     "'tsismis'", "<INVALID>", "'waley'", "'dagdag'", "'bawas'", 
                     "'dobolDobol'", "'hati'", "'sobra'", "'etoNaLods'", 
                     "'parehasLods'", "'diParehasLods'", "'masGamay'", "'masDako'", 
                     "'saktoGamay'", "'saktoDako'", "'++'", "'--'", "<INVALID>", 
                     "<INVALID>", "'dili'", "'('", "')'", "'{'", "'}'", 
                     "';'", "','", "'&'", "'*'", "'ngutana'", "'yawit'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "ELSEIF", "WHILE", "FOR", 
                      "FUNCTION", "RETURN", "VAR", "BREAK", "CONTINUE", 
                      "CONST", "KW_INT", "KW_DOUBLE", "KW_CHAR", "KW_STRING", 
                      "BOOLEAN_LITERAL", "NULL_LITERAL", "PLUS", "MINUS", 
                      "MULT", "DIV", "MODULO", "ASSIGN", "EQ", "NEQ", "LT", 
                      "GT", "LEQ", "GEQ", "INCREMENT", "DECREMENT", "AND", 
                      "OR", "NOT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "SEMICOLON", "COMMA", "REFERENCE", "DEREFERENCE", 
                      "READ", "PRINT", "FLOAT", "INTEGER", "STRING", "CHAR", 
                      "IDENTIFIER", "LINE_COMMENT", "BLOCK_COMMENT", "WS", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_vardecl = 2
    RULE_assignment = 3
    RULE_incDecStmt = 4
    RULE_assignmentNoSemicolon = 5
    RULE_typedVarDecl = 6
    RULE_printStmt = 7
    RULE_ifStmt = 8
    RULE_whileStmt = 9
    RULE_forStmt = 10
    RULE_funcDecl = 11
    RULE_funcCall = 12
    RULE_expression = 13
    RULE_dataType = 14
    RULE_literal = 15
    RULE_paramList = 16
    RULE_argList = 17
    RULE_block = 18

    ruleNames =  [ "program", "statement", "vardecl", "assignment", "incDecStmt", 
                   "assignmentNoSemicolon", "typedVarDecl", "printStmt", 
                   "ifStmt", "whileStmt", "forStmt", "funcDecl", "funcCall", 
                   "expression", "dataType", "literal", "paramList", "argList", 
                   "block" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    ELSEIF=3
    WHILE=4
    FOR=5
    FUNCTION=6
    RETURN=7
    VAR=8
    BREAK=9
    CONTINUE=10
    CONST=11
    KW_INT=12
    KW_DOUBLE=13
    KW_CHAR=14
    KW_STRING=15
    BOOLEAN_LITERAL=16
    NULL_LITERAL=17
    PLUS=18
    MINUS=19
    MULT=20
    DIV=21
    MODULO=22
    ASSIGN=23
    EQ=24
    NEQ=25
    LT=26
    GT=27
    LEQ=28
    GEQ=29
    INCREMENT=30
    DECREMENT=31
    AND=32
    OR=33
    NOT=34
    LPAREN=35
    RPAREN=36
    LBRACE=37
    RBRACE=38
    SEMICOLON=39
    COMMA=40
    REFERENCE=41
    DEREFERENCE=42
    READ=43
    PRINT=44
    FLOAT=45
    INTEGER=46
    STRING=47
    CHAR=48
    IDENTIFIER=49
    LINE_COMMENT=50
    BLOCK_COMMENT=51
    WS=52
    ERROR_CHAR=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 580542139467762) != 0):
                self.state = 38
                self.statement()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 44
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(ExprParser.VardeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(ExprParser.IncDecStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(ExprParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(ExprParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(ExprParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(ExprParser.ForStmtContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(ExprParser.FuncDeclContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(ExprParser.FuncCallContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def BREAK(self):
            return self.getToken(ExprParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(ExprParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 66
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.incDecStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.printStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.ifStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.whileStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.forStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.funcDecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.funcCall()
                self.state = 55
                self.match(ExprParser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 57
                self.match(ExprParser.RETURN)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1090767074557952) != 0):
                    self.state = 58
                    self.expression(0)


                self.state = 61
                self.match(ExprParser.SEMICOLON)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 62
                self.match(ExprParser.BREAK)
                self.state = 63
                self.match(ExprParser.SEMICOLON)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 64
                self.match(ExprParser.CONTINUE)
                self.state = 65
                self.match(ExprParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ExprParser.VAR, 0)

        def dataType(self):
            return self.getTypedRuleContext(ExprParser.DataTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)




    def vardecl(self):

        localctx = ExprParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ExprParser.VAR)
            self.state = 69
            self.dataType()
            self.state = 70
            self.match(ExprParser.IDENTIFIER)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 71
                self.match(ExprParser.ASSIGN)
                self.state = 72
                self.expression(0)


            self.state = 75
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ExprParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(ExprParser.IDENTIFIER)
            self.state = 78
            self.match(ExprParser.ASSIGN)
            self.state = 79
            self.expression(0)
            self.state = 80
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def INCREMENT(self):
            return self.getToken(ExprParser.INCREMENT, 0)

        def DECREMENT(self):
            return self.getToken(ExprParser.DECREMENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_incDecStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncDecStmt" ):
                listener.enterIncDecStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncDecStmt" ):
                listener.exitIncDecStmt(self)




    def incDecStmt(self):

        localctx = ExprParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_incDecStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 82
                self.match(ExprParser.IDENTIFIER)
                self.state = 83
                self.match(ExprParser.INCREMENT)
                pass

            elif la_ == 2:
                self.state = 84
                self.match(ExprParser.IDENTIFIER)
                self.state = 85
                self.match(ExprParser.DECREMENT)
                pass


            self.state = 88
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentNoSemicolonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_assignmentNoSemicolon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentNoSemicolon" ):
                listener.enterAssignmentNoSemicolon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentNoSemicolon" ):
                listener.exitAssignmentNoSemicolon(self)




    def assignmentNoSemicolon(self):

        localctx = ExprParser.AssignmentNoSemicolonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignmentNoSemicolon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(ExprParser.IDENTIFIER)
            self.state = 91
            self.match(ExprParser.ASSIGN)
            self.state = 92
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self):
            return self.getTypedRuleContext(ExprParser.DataTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_typedVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedVarDecl" ):
                listener.enterTypedVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedVarDecl" ):
                listener.exitTypedVarDecl(self)




    def typedVarDecl(self):

        localctx = ExprParser.TypedVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_typedVarDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.dataType()
            self.state = 95
            self.match(ExprParser.IDENTIFIER)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 96
                self.match(ExprParser.ASSIGN)
                self.state = 97
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(ExprParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)




    def printStmt(self):

        localctx = ExprParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ExprParser.PRINT)
            self.state = 101
            self.expression(0)
            self.state = 102
            self.match(ExprParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.BlockContext)
            else:
                return self.getTypedRuleContext(ExprParser.BlockContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ELSEIF)
            else:
                return self.getToken(ExprParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)




    def ifStmt(self):

        localctx = ExprParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(ExprParser.IF)
            self.state = 105
            self.match(ExprParser.LPAREN)
            self.state = 106
            self.expression(0)
            self.state = 107
            self.match(ExprParser.RPAREN)
            self.state = 108
            self.block()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 109
                self.match(ExprParser.ELSEIF)
                self.state = 110
                self.match(ExprParser.LPAREN)
                self.state = 111
                self.expression(0)
                self.state = 112
                self.match(ExprParser.RPAREN)
                self.state = 113
                self.block()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 120
                self.match(ExprParser.ELSE)
                self.state = 121
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = ExprParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ExprParser.WHILE)
            self.state = 125
            self.match(ExprParser.LPAREN)
            self.state = 126
            self.expression(0)
            self.state = 127
            self.match(ExprParser.RPAREN)
            self.state = 128
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMICOLON)
            else:
                return self.getToken(ExprParser.SEMICOLON, i)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(ExprParser.VardeclContext,0)


        def typedVarDecl(self):
            return self.getTypedRuleContext(ExprParser.TypedVarDeclContext,0)


        def assignmentNoSemicolon(self):
            return self.getTypedRuleContext(ExprParser.AssignmentNoSemicolonContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)




    def forStmt(self):

        localctx = ExprParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(ExprParser.FOR)
            self.state = 131
            self.match(ExprParser.LPAREN)
            self.state = 135
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.state = 132
                self.vardecl()
                pass
            elif token in [12, 13, 14, 15]:
                self.state = 133
                self.typedVarDecl()
                pass
            elif token in [49]:
                self.state = 134
                self.assignmentNoSemicolon()
                pass
            elif token in [39]:
                pass
            else:
                pass
            self.state = 137
            self.match(ExprParser.SEMICOLON)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1090767074557952) != 0):
                self.state = 138
                self.expression(0)


            self.state = 141
            self.match(ExprParser.SEMICOLON)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1090767074557952) != 0):
                self.state = 142
                self.expression(0)


            self.state = 145
            self.match(ExprParser.RPAREN)
            self.state = 146
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ExprParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(ExprParser.ParamListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)




    def funcDecl(self):

        localctx = ExprParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(ExprParser.FUNCTION)
            self.state = 149
            self.match(ExprParser.IDENTIFIER)
            self.state = 150
            self.match(ExprParser.LPAREN)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0):
                self.state = 151
                self.paramList()


            self.state = 154
            self.match(ExprParser.RPAREN)
            self.state = 155
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def argList(self):
            return self.getTypedRuleContext(ExprParser.ArgListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = ExprParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(ExprParser.IDENTIFIER)
            self.state = 158
            self.match(ExprParser.LPAREN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1090767074557952) != 0):
                self.state = 159
                self.argList()


            self.state = 162
            self.match(ExprParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def MULT(self):
            return self.getToken(ExprParser.MULT, 0)
        def DIV(self):
            return self.getToken(ExprParser.DIV, 0)
        def MODULO(self):
            return self.getToken(ExprParser.MODULO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)


    class CompareExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ExprParser.NEQ, 0)
        def LT(self):
            return self.getToken(ExprParser.LT, 0)
        def LEQ(self):
            return self.getToken(ExprParser.LEQ, 0)
        def GT(self):
            return self.getToken(ExprParser.GT, 0)
        def GEQ(self):
            return self.getToken(ExprParser.GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompareExpr" ):
                listener.enterCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompareExpr" ):
                listener.exitCompareExpr(self)


    class LogicExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(ExprParser.AND, 0)
        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicExpr" ):
                listener.enterLogicExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicExpr" ):
                listener.exitLogicExpr(self)


    class PostDecrementContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)
        def DECREMENT(self):
            return self.getToken(ExprParser.DECREMENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecrement" ):
                listener.enterPostDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecrement" ):
                listener.exitPostDecrement(self)


    class LiteralExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(ExprParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteralExpr" ):
                listener.enterLiteralExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteralExpr" ):
                listener.exitLiteralExpr(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)


    class PostIncrementContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)
        def INCREMENT(self):
            return self.getToken(ExprParser.INCREMENT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrement" ):
                listener.enterPostIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrement" ):
                listener.exitPostIncrement(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)


    class AssignExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(ExprParser.IDENTIFIER, 0)
        def ASSIGN(self):
            return self.getToken(ExprParser.ASSIGN, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)


    class FuncCallExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def funcCall(self):
            return self.getTypedRuleContext(ExprParser.FuncCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = ExprParser.AssignExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 165
                self.match(ExprParser.IDENTIFIER)
                self.state = 166
                self.match(ExprParser.ASSIGN)
                self.state = 167
                self.expression(12)
                pass

            elif la_ == 2:
                localctx = ExprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 168
                self.match(ExprParser.NOT)
                self.state = 169
                self.expression(7)
                pass

            elif la_ == 3:
                localctx = ExprParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 170
                self.match(ExprParser.LPAREN)
                self.state = 171
                self.expression(0)
                self.state = 172
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 4:
                localctx = ExprParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 174
                self.funcCall()
                pass

            elif la_ == 5:
                localctx = ExprParser.PostIncrementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 175
                self.match(ExprParser.IDENTIFIER)
                self.state = 176
                self.match(ExprParser.INCREMENT)
                pass

            elif la_ == 6:
                localctx = ExprParser.PostDecrementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 177
                self.match(ExprParser.IDENTIFIER)
                self.state = 178
                self.match(ExprParser.DECREMENT)
                pass

            elif la_ == 7:
                localctx = ExprParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 179
                self.literal()
                pass

            elif la_ == 8:
                localctx = ExprParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 180
                self.match(ExprParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 195
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.AddSubExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 183
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 184
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 185
                        self.expression(12)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulDivExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 186
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 187
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 188
                        self.expression(11)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.CompareExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 189
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 190
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 191
                        self.expression(10)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.LogicExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 192
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 193
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 194
                        self.expression(9)
                        pass

             
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INT(self):
            return self.getToken(ExprParser.KW_INT, 0)

        def KW_DOUBLE(self):
            return self.getToken(ExprParser.KW_DOUBLE, 0)

        def KW_CHAR(self):
            return self.getToken(ExprParser.KW_CHAR, 0)

        def KW_STRING(self):
            return self.getToken(ExprParser.KW_STRING, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)




    def dataType(self):

        localctx = ExprParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(ExprParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(ExprParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(ExprParser.STRING, 0)

        def CHAR(self):
            return self.getToken(ExprParser.CHAR, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(ExprParser.BOOLEAN_LITERAL, 0)

        def NULL_LITERAL(self):
            return self.getToken(ExprParser.NULL_LITERAL, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = ExprParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 527765581529088) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataType(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.DataTypeContext)
            else:
                return self.getTypedRuleContext(ExprParser.DataTypeContext,i)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.IDENTIFIER)
            else:
                return self.getToken(ExprParser.IDENTIFIER, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)




    def paramList(self):

        localctx = ExprParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.dataType()
            self.state = 205
            self.match(ExprParser.IDENTIFIER)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 206
                self.match(ExprParser.COMMA)
                self.state = 207
                self.dataType()
                self.state = 208
                self.match(ExprParser.IDENTIFIER)
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)




    def argList(self):

        localctx = ExprParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.expression(0)
            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 216
                self.match(ExprParser.COMMA)
                self.state = 217
                self.expression(0)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(ExprParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(ExprParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(ExprParser.LBRACE)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 580542139467762) != 0):
                self.state = 224
                self.statement()
                self.state = 229
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 230
            self.match(ExprParser.RBRACE)
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
        self._predicates[13] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 8)
         




