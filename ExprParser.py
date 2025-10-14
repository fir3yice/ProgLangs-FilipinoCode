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
        4,1,53,192,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,5,0,34,8,0,10,0,12,0,37,9,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,1,1,1,1,
        1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,2,3,2,67,8,2,1,2,1,2,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,5,5,91,8,5,10,5,12,5,94,9,5,1,5,1,5,3,5,98,8,5,1,6,1,
        6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        8,1,8,3,8,119,8,8,1,8,1,8,1,8,1,9,1,9,1,9,3,9,127,8,9,1,9,1,9,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,141,8,10,1,
        10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,5,10,155,
        8,10,10,10,12,10,158,9,10,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,5,13,170,8,13,10,13,12,13,173,9,13,1,14,1,14,1,14,5,14,
        178,8,14,10,14,12,14,181,9,14,1,15,1,15,5,15,185,8,15,10,15,12,15,
        188,9,15,1,15,1,15,1,15,0,1,20,16,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,0,6,1,0,18,19,1,0,20,22,1,0,24,29,1,0,32,33,1,0,12,15,
        2,0,16,17,45,48,203,0,35,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,70,
        1,0,0,0,8,75,1,0,0,0,10,79,1,0,0,0,12,99,1,0,0,0,14,105,1,0,0,0,
        16,114,1,0,0,0,18,123,1,0,0,0,20,140,1,0,0,0,22,159,1,0,0,0,24,161,
        1,0,0,0,26,163,1,0,0,0,28,174,1,0,0,0,30,182,1,0,0,0,32,34,3,2,1,
        0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,38,
        1,0,0,0,37,35,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,60,3,4,2,0,41,
        60,3,6,3,0,42,60,3,8,4,0,43,60,3,10,5,0,44,60,3,12,6,0,45,60,3,14,
        7,0,46,60,3,16,8,0,47,48,3,18,9,0,48,49,5,39,0,0,49,60,1,0,0,0,50,
        52,5,7,0,0,51,53,3,20,10,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,
        0,0,54,60,5,39,0,0,55,56,5,9,0,0,56,60,5,39,0,0,57,58,5,10,0,0,58,
        60,5,39,0,0,59,40,1,0,0,0,59,41,1,0,0,0,59,42,1,0,0,0,59,43,1,0,
        0,0,59,44,1,0,0,0,59,45,1,0,0,0,59,46,1,0,0,0,59,47,1,0,0,0,59,50,
        1,0,0,0,59,55,1,0,0,0,59,57,1,0,0,0,60,3,1,0,0,0,61,62,5,8,0,0,62,
        63,3,22,11,0,63,66,5,49,0,0,64,65,5,23,0,0,65,67,3,20,10,0,66,64,
        1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,39,0,0,69,5,1,0,0,0,
        70,71,5,49,0,0,71,72,5,23,0,0,72,73,3,20,10,0,73,74,5,39,0,0,74,
        7,1,0,0,0,75,76,5,44,0,0,76,77,3,20,10,0,77,78,5,39,0,0,78,9,1,0,
        0,0,79,80,5,1,0,0,80,81,5,35,0,0,81,82,3,20,10,0,82,83,5,36,0,0,
        83,92,3,30,15,0,84,85,5,3,0,0,85,86,5,35,0,0,86,87,3,20,10,0,87,
        88,5,36,0,0,88,89,3,30,15,0,89,91,1,0,0,0,90,84,1,0,0,0,91,94,1,
        0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,97,1,0,0,0,94,92,1,0,0,0,95,
        96,5,2,0,0,96,98,3,30,15,0,97,95,1,0,0,0,97,98,1,0,0,0,98,11,1,0,
        0,0,99,100,5,4,0,0,100,101,5,35,0,0,101,102,3,20,10,0,102,103,5,
        36,0,0,103,104,3,30,15,0,104,13,1,0,0,0,105,106,5,5,0,0,106,107,
        5,35,0,0,107,108,3,6,3,0,108,109,3,20,10,0,109,110,5,39,0,0,110,
        111,3,20,10,0,111,112,5,36,0,0,112,113,3,30,15,0,113,15,1,0,0,0,
        114,115,5,6,0,0,115,116,5,49,0,0,116,118,5,35,0,0,117,119,3,26,13,
        0,118,117,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,36,0,
        0,121,122,3,30,15,0,122,17,1,0,0,0,123,124,5,49,0,0,124,126,5,35,
        0,0,125,127,3,28,14,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,
        0,0,0,128,129,5,36,0,0,129,19,1,0,0,0,130,131,6,10,-1,0,131,132,
        5,34,0,0,132,141,3,20,10,5,133,134,5,35,0,0,134,135,3,20,10,0,135,
        136,5,36,0,0,136,141,1,0,0,0,137,141,3,18,9,0,138,141,3,24,12,0,
        139,141,5,49,0,0,140,130,1,0,0,0,140,133,1,0,0,0,140,137,1,0,0,0,
        140,138,1,0,0,0,140,139,1,0,0,0,141,156,1,0,0,0,142,143,10,9,0,0,
        143,144,7,0,0,0,144,155,3,20,10,10,145,146,10,8,0,0,146,147,7,1,
        0,0,147,155,3,20,10,9,148,149,10,7,0,0,149,150,7,2,0,0,150,155,3,
        20,10,8,151,152,10,6,0,0,152,153,7,3,0,0,153,155,3,20,10,7,154,142,
        1,0,0,0,154,145,1,0,0,0,154,148,1,0,0,0,154,151,1,0,0,0,155,158,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,21,1,0,0,0,158,156,1,
        0,0,0,159,160,7,4,0,0,160,23,1,0,0,0,161,162,7,5,0,0,162,25,1,0,
        0,0,163,164,3,22,11,0,164,171,5,49,0,0,165,166,5,40,0,0,166,167,
        3,22,11,0,167,168,5,49,0,0,168,170,1,0,0,0,169,165,1,0,0,0,170,173,
        1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,27,1,0,0,0,173,171,1,
        0,0,0,174,179,3,20,10,0,175,176,5,40,0,0,176,178,3,20,10,0,177,175,
        1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,180,29,1,
        0,0,0,181,179,1,0,0,0,182,186,5,37,0,0,183,185,3,2,1,0,184,183,1,
        0,0,0,185,188,1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,189,1,
        0,0,0,188,186,1,0,0,0,189,190,5,38,0,0,190,31,1,0,0,0,14,35,52,59,
        66,92,97,118,126,140,154,156,171,179,186
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
    RULE_printStmt = 4
    RULE_ifStmt = 5
    RULE_whileStmt = 6
    RULE_forStmt = 7
    RULE_funcDecl = 8
    RULE_funcCall = 9
    RULE_expression = 10
    RULE_dataType = 11
    RULE_literal = 12
    RULE_paramList = 13
    RULE_argList = 14
    RULE_block = 15

    ruleNames =  [ "program", "statement", "vardecl", "assignment", "printStmt", 
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
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 580542139467762) != 0):
                self.state = 32
                self.statement()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 42
                self.printStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.ifStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.whileStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 45
                self.forStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.funcDecl()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 47
                self.funcCall()
                self.state = 48
                self.match(ExprParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 50
                self.match(ExprParser.RETURN)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1090767074557952) != 0):
                    self.state = 51
                    self.expression(0)


                self.state = 54
                self.match(ExprParser.SEMICOLON)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 55
                self.match(ExprParser.BREAK)
                self.state = 56
                self.match(ExprParser.SEMICOLON)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 57
                self.match(ExprParser.CONTINUE)
                self.state = 58
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
            self.state = 61
            self.match(ExprParser.VAR)
            self.state = 62
            self.dataType()
            self.state = 63
            self.match(ExprParser.IDENTIFIER)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 64
                self.match(ExprParser.ASSIGN)
                self.state = 65
                self.expression(0)


            self.state = 68
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
            self.state = 70
            self.match(ExprParser.IDENTIFIER)
            self.state = 71
            self.match(ExprParser.ASSIGN)
            self.state = 72
            self.expression(0)
            self.state = 73
            self.match(ExprParser.SEMICOLON)
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
        self.enterRule(localctx, 8, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ExprParser.PRINT)
            self.state = 76
            self.expression(0)
            self.state = 77
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
        self.enterRule(localctx, 10, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(ExprParser.IF)
            self.state = 80
            self.match(ExprParser.LPAREN)
            self.state = 81
            self.expression(0)
            self.state = 82
            self.match(ExprParser.RPAREN)
            self.state = 83
            self.block()
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 84
                self.match(ExprParser.ELSEIF)
                self.state = 85
                self.match(ExprParser.LPAREN)
                self.state = 86
                self.expression(0)
                self.state = 87
                self.match(ExprParser.RPAREN)
                self.state = 88
                self.block()
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 95
                self.match(ExprParser.ELSE)
                self.state = 96
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
        self.enterRule(localctx, 12, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ExprParser.WHILE)
            self.state = 100
            self.match(ExprParser.LPAREN)
            self.state = 101
            self.expression(0)
            self.state = 102
            self.match(ExprParser.RPAREN)
            self.state = 103
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

        def assignment(self):
            return self.getTypedRuleContext(ExprParser.AssignmentContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExpressionContext,i)


        def SEMICOLON(self):
            return self.getToken(ExprParser.SEMICOLON, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


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
        self.enterRule(localctx, 14, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ExprParser.FOR)
            self.state = 106
            self.match(ExprParser.LPAREN)
            self.state = 107
            self.assignment()
            self.state = 108
            self.expression(0)
            self.state = 109
            self.match(ExprParser.SEMICOLON)
            self.state = 110
            self.expression(0)
            self.state = 111
            self.match(ExprParser.RPAREN)
            self.state = 112
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
        self.enterRule(localctx, 16, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ExprParser.FUNCTION)
            self.state = 115
            self.match(ExprParser.IDENTIFIER)
            self.state = 116
            self.match(ExprParser.LPAREN)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0):
                self.state = 117
                self.paramList()


            self.state = 120
            self.match(ExprParser.RPAREN)
            self.state = 121
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
        self.enterRule(localctx, 18, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ExprParser.IDENTIFIER)
            self.state = 124
            self.match(ExprParser.LPAREN)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1090767074557952) != 0):
                self.state = 125
                self.argList()


            self.state = 128
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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                localctx = ExprParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 131
                self.match(ExprParser.NOT)
                self.state = 132
                self.expression(5)
                pass

            elif la_ == 2:
                localctx = ExprParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(ExprParser.LPAREN)
                self.state = 134
                self.expression(0)
                self.state = 135
                self.match(ExprParser.RPAREN)
                pass

            elif la_ == 3:
                localctx = ExprParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.funcCall()
                pass

            elif la_ == 4:
                localctx = ExprParser.LiteralExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.literal()
                pass

            elif la_ == 5:
                localctx = ExprParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.match(ExprParser.IDENTIFIER)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 154
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.AddSubExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 143
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 144
                        self.expression(10)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.MulDivExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 145
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 146
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 147
                        self.expression(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.CompareExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 149
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        self.expression(8)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.LogicExprContext(self, ExprParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 152
                        _la = self._input.LA(1)
                        if not(_la==32 or _la==33):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 153
                        self.expression(7)
                        pass

             
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
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
        self.enterRule(localctx, 24, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
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
        self.enterRule(localctx, 26, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.dataType()
            self.state = 164
            self.match(ExprParser.IDENTIFIER)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 165
                self.match(ExprParser.COMMA)
                self.state = 166
                self.dataType()
                self.state = 167
                self.match(ExprParser.IDENTIFIER)
                self.state = 173
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
        self.enterRule(localctx, 28, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.expression(0)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 175
                self.match(ExprParser.COMMA)
                self.state = 176
                self.expression(0)
                self.state = 181
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
        self.enterRule(localctx, 30, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(ExprParser.LBRACE)
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 580542139467762) != 0):
                self.state = 183
                self.statement()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 189
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
        self._predicates[10] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




