# Generated from FilipinoCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FilipinoCodeParser import FilipinoCodeParser
else:
    from FilipinoCodeParser import FilipinoCodeParser

# This class defines a complete generic visitor for a parse tree produced by FilipinoCodeParser.

class FilipinoCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FilipinoCodeParser#program.
    def visitProgram(self, ctx:FilipinoCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#module.
    def visitModule(self, ctx:FilipinoCodeParser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#main_function.
    def visitMain_function(self, ctx:FilipinoCodeParser.Main_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#function_content.
    def visitFunction_content(self, ctx:FilipinoCodeParser.Function_contentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#statement.
    def visitStatement(self, ctx:FilipinoCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#deposit_statement.
    def visitDeposit_statement(self, ctx:FilipinoCodeParser.Deposit_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#withdraw_statement.
    def visitWithdraw_statement(self, ctx:FilipinoCodeParser.Withdraw_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#show_balance_statement.
    def visitShow_balance_statement(self, ctx:FilipinoCodeParser.Show_balance_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#transfer_statement.
    def visitTransfer_statement(self, ctx:FilipinoCodeParser.Transfer_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#interest_statement.
    def visitInterest_statement(self, ctx:FilipinoCodeParser.Interest_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#break_statement.
    def visitBreak_statement(self, ctx:FilipinoCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:FilipinoCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#assignment_statement.
    def visitAssignment_statement(self, ctx:FilipinoCodeParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#expression.
    def visitExpression(self, ctx:FilipinoCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#bool_expr.
    def visitBool_expr(self, ctx:FilipinoCodeParser.Bool_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#bool_term.
    def visitBool_term(self, ctx:FilipinoCodeParser.Bool_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#relational_expr.
    def visitRelational_expr(self, ctx:FilipinoCodeParser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#arith_expr.
    def visitArith_expr(self, ctx:FilipinoCodeParser.Arith_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#arith_term.
    def visitArith_term(self, ctx:FilipinoCodeParser.Arith_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#arith_factor.
    def visitArith_factor(self, ctx:FilipinoCodeParser.Arith_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#value.
    def visitValue(self, ctx:FilipinoCodeParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#vardecl_statement.
    def visitVardecl_statement(self, ctx:FilipinoCodeParser.Vardecl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#data_type.
    def visitData_type(self, ctx:FilipinoCodeParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#identifier_list.
    def visitIdentifier_list(self, ctx:FilipinoCodeParser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#funcdecl_list.
    def visitFuncdecl_list(self, ctx:FilipinoCodeParser.Funcdecl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#function_declaration.
    def visitFunction_declaration(self, ctx:FilipinoCodeParser.Function_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#function_signature.
    def visitFunction_signature(self, ctx:FilipinoCodeParser.Function_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#funccall.
    def visitFunccall(self, ctx:FilipinoCodeParser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#funccall_stmt.
    def visitFunccall_stmt(self, ctx:FilipinoCodeParser.Funccall_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#parameter_list.
    def visitParameter_list(self, ctx:FilipinoCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#parameter.
    def visitParameter(self, ctx:FilipinoCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#actual_parameter_list.
    def visitActual_parameter_list(self, ctx:FilipinoCodeParser.Actual_parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#return_statement.
    def visitReturn_statement(self, ctx:FilipinoCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#block.
    def visitBlock(self, ctx:FilipinoCodeParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#if_statement.
    def visitIf_statement(self, ctx:FilipinoCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#while_statement.
    def visitWhile_statement(self, ctx:FilipinoCodeParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#for_statement.
    def visitFor_statement(self, ctx:FilipinoCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#print_statement.
    def visitPrint_statement(self, ctx:FilipinoCodeParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#input_statement.
    def visitInput_statement(self, ctx:FilipinoCodeParser.Input_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#constdecl_list.
    def visitConstdecl_list(self, ctx:FilipinoCodeParser.Constdecl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#const_statement.
    def visitConst_statement(self, ctx:FilipinoCodeParser.Const_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#use_list.
    def visitUse_list(self, ctx:FilipinoCodeParser.Use_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FilipinoCodeParser#use_statement.
    def visitUse_statement(self, ctx:FilipinoCodeParser.Use_statementContext):
        return self.visitChildren(ctx)



del FilipinoCodeParser