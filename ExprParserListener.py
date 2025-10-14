# Generated from ExprParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#vardecl.
    def enterVardecl(self, ctx:ExprParser.VardeclContext):
        pass

    # Exit a parse tree produced by ExprParser#vardecl.
    def exitVardecl(self, ctx:ExprParser.VardeclContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#incDecStmt.
    def enterIncDecStmt(self, ctx:ExprParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#incDecStmt.
    def exitIncDecStmt(self, ctx:ExprParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#assignmentNoSemicolon.
    def enterAssignmentNoSemicolon(self, ctx:ExprParser.AssignmentNoSemicolonContext):
        pass

    # Exit a parse tree produced by ExprParser#assignmentNoSemicolon.
    def exitAssignmentNoSemicolon(self, ctx:ExprParser.AssignmentNoSemicolonContext):
        pass


    # Enter a parse tree produced by ExprParser#typedVarDecl.
    def enterTypedVarDecl(self, ctx:ExprParser.TypedVarDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#typedVarDecl.
    def exitTypedVarDecl(self, ctx:ExprParser.TypedVarDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#printStmt.
    def enterPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#printStmt.
    def exitPrintStmt(self, ctx:ExprParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#ifStmt.
    def enterIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#ifStmt.
    def exitIfStmt(self, ctx:ExprParser.IfStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStmt.
    def enterWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStmt.
    def exitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#forStmt.
    def enterForStmt(self, ctx:ExprParser.ForStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#forStmt.
    def exitForStmt(self, ctx:ExprParser.ForStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#funcDecl.
    def enterFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#funcDecl.
    def exitFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#funcCall.
    def enterFuncCall(self, ctx:ExprParser.FuncCallContext):
        pass

    # Exit a parse tree produced by ExprParser#funcCall.
    def exitFuncCall(self, ctx:ExprParser.FuncCallContext):
        pass


    # Enter a parse tree produced by ExprParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by ExprParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:ExprParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by ExprParser#IdExpr.
    def enterIdExpr(self, ctx:ExprParser.IdExprContext):
        pass

    # Exit a parse tree produced by ExprParser#IdExpr.
    def exitIdExpr(self, ctx:ExprParser.IdExprContext):
        pass


    # Enter a parse tree produced by ExprParser#CompareExpr.
    def enterCompareExpr(self, ctx:ExprParser.CompareExprContext):
        pass

    # Exit a parse tree produced by ExprParser#CompareExpr.
    def exitCompareExpr(self, ctx:ExprParser.CompareExprContext):
        pass


    # Enter a parse tree produced by ExprParser#LogicExpr.
    def enterLogicExpr(self, ctx:ExprParser.LogicExprContext):
        pass

    # Exit a parse tree produced by ExprParser#LogicExpr.
    def exitLogicExpr(self, ctx:ExprParser.LogicExprContext):
        pass


    # Enter a parse tree produced by ExprParser#PostDecrement.
    def enterPostDecrement(self, ctx:ExprParser.PostDecrementContext):
        pass

    # Exit a parse tree produced by ExprParser#PostDecrement.
    def exitPostDecrement(self, ctx:ExprParser.PostDecrementContext):
        pass


    # Enter a parse tree produced by ExprParser#LiteralExpr.
    def enterLiteralExpr(self, ctx:ExprParser.LiteralExprContext):
        pass

    # Exit a parse tree produced by ExprParser#LiteralExpr.
    def exitLiteralExpr(self, ctx:ExprParser.LiteralExprContext):
        pass


    # Enter a parse tree produced by ExprParser#NotExpr.
    def enterNotExpr(self, ctx:ExprParser.NotExprContext):
        pass

    # Exit a parse tree produced by ExprParser#NotExpr.
    def exitNotExpr(self, ctx:ExprParser.NotExprContext):
        pass


    # Enter a parse tree produced by ExprParser#PostIncrement.
    def enterPostIncrement(self, ctx:ExprParser.PostIncrementContext):
        pass

    # Exit a parse tree produced by ExprParser#PostIncrement.
    def exitPostIncrement(self, ctx:ExprParser.PostIncrementContext):
        pass


    # Enter a parse tree produced by ExprParser#ParenExpr.
    def enterParenExpr(self, ctx:ExprParser.ParenExprContext):
        pass

    # Exit a parse tree produced by ExprParser#ParenExpr.
    def exitParenExpr(self, ctx:ExprParser.ParenExprContext):
        pass


    # Enter a parse tree produced by ExprParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by ExprParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:ExprParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by ExprParser#AssignExpr.
    def enterAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass

    # Exit a parse tree produced by ExprParser#AssignExpr.
    def exitAssignExpr(self, ctx:ExprParser.AssignExprContext):
        pass


    # Enter a parse tree produced by ExprParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:ExprParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by ExprParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:ExprParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by ExprParser#dataType.
    def enterDataType(self, ctx:ExprParser.DataTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#dataType.
    def exitDataType(self, ctx:ExprParser.DataTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#literal.
    def enterLiteral(self, ctx:ExprParser.LiteralContext):
        pass

    # Exit a parse tree produced by ExprParser#literal.
    def exitLiteral(self, ctx:ExprParser.LiteralContext):
        pass


    # Enter a parse tree produced by ExprParser#paramList.
    def enterParamList(self, ctx:ExprParser.ParamListContext):
        pass

    # Exit a parse tree produced by ExprParser#paramList.
    def exitParamList(self, ctx:ExprParser.ParamListContext):
        pass


    # Enter a parse tree produced by ExprParser#argList.
    def enterArgList(self, ctx:ExprParser.ArgListContext):
        pass

    # Exit a parse tree produced by ExprParser#argList.
    def exitArgList(self, ctx:ExprParser.ArgListContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass



del ExprParser