# Generated from FilipinoCode.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FilipinoCodeParser import FilipinoCodeParser
else:
    from FilipinoCodeParser import FilipinoCodeParser

# This class defines a complete listener for a parse tree produced by FilipinoCodeParser.
class FilipinoCodeListener(ParseTreeListener):

    # Enter a parse tree produced by FilipinoCodeParser#program.
    def enterProgram(self, ctx:FilipinoCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#program.
    def exitProgram(self, ctx:FilipinoCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#main_function.
    def enterMain_function(self, ctx:FilipinoCodeParser.Main_functionContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#main_function.
    def exitMain_function(self, ctx:FilipinoCodeParser.Main_functionContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#function_content.
    def enterFunction_content(self, ctx:FilipinoCodeParser.Function_contentContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#function_content.
    def exitFunction_content(self, ctx:FilipinoCodeParser.Function_contentContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#statement.
    def enterStatement(self, ctx:FilipinoCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#statement.
    def exitStatement(self, ctx:FilipinoCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#break_statement.
    def enterBreak_statement(self, ctx:FilipinoCodeParser.Break_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#break_statement.
    def exitBreak_statement(self, ctx:FilipinoCodeParser.Break_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#continue_statement.
    def enterContinue_statement(self, ctx:FilipinoCodeParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#continue_statement.
    def exitContinue_statement(self, ctx:FilipinoCodeParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#assignment_statement.
    def enterAssignment_statement(self, ctx:FilipinoCodeParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#assignment_statement.
    def exitAssignment_statement(self, ctx:FilipinoCodeParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#funccall.
    def enterFunccall(self, ctx:FilipinoCodeParser.FunccallContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#funccall.
    def exitFunccall(self, ctx:FilipinoCodeParser.FunccallContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#funccall_stmt.
    def enterFunccall_stmt(self, ctx:FilipinoCodeParser.Funccall_stmtContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#funccall_stmt.
    def exitFunccall_stmt(self, ctx:FilipinoCodeParser.Funccall_stmtContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#expression.
    def enterExpression(self, ctx:FilipinoCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#expression.
    def exitExpression(self, ctx:FilipinoCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#bool_expr.
    def enterBool_expr(self, ctx:FilipinoCodeParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#bool_expr.
    def exitBool_expr(self, ctx:FilipinoCodeParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#bool_term.
    def enterBool_term(self, ctx:FilipinoCodeParser.Bool_termContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#bool_term.
    def exitBool_term(self, ctx:FilipinoCodeParser.Bool_termContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#relational_expr.
    def enterRelational_expr(self, ctx:FilipinoCodeParser.Relational_exprContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#relational_expr.
    def exitRelational_expr(self, ctx:FilipinoCodeParser.Relational_exprContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#arith_expr.
    def enterArith_expr(self, ctx:FilipinoCodeParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#arith_expr.
    def exitArith_expr(self, ctx:FilipinoCodeParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#arith_term.
    def enterArith_term(self, ctx:FilipinoCodeParser.Arith_termContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#arith_term.
    def exitArith_term(self, ctx:FilipinoCodeParser.Arith_termContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#arith_factor.
    def enterArith_factor(self, ctx:FilipinoCodeParser.Arith_factorContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#arith_factor.
    def exitArith_factor(self, ctx:FilipinoCodeParser.Arith_factorContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#value.
    def enterValue(self, ctx:FilipinoCodeParser.ValueContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#value.
    def exitValue(self, ctx:FilipinoCodeParser.ValueContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#vardecl_statement.
    def enterVardecl_statement(self, ctx:FilipinoCodeParser.Vardecl_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#vardecl_statement.
    def exitVardecl_statement(self, ctx:FilipinoCodeParser.Vardecl_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#data_type.
    def enterData_type(self, ctx:FilipinoCodeParser.Data_typeContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#data_type.
    def exitData_type(self, ctx:FilipinoCodeParser.Data_typeContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#identifier_list.
    def enterIdentifier_list(self, ctx:FilipinoCodeParser.Identifier_listContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#identifier_list.
    def exitIdentifier_list(self, ctx:FilipinoCodeParser.Identifier_listContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#funcdecl_list.
    def enterFuncdecl_list(self, ctx:FilipinoCodeParser.Funcdecl_listContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#funcdecl_list.
    def exitFuncdecl_list(self, ctx:FilipinoCodeParser.Funcdecl_listContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#function_declaration.
    def enterFunction_declaration(self, ctx:FilipinoCodeParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#function_declaration.
    def exitFunction_declaration(self, ctx:FilipinoCodeParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#function_signature.
    def enterFunction_signature(self, ctx:FilipinoCodeParser.Function_signatureContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#function_signature.
    def exitFunction_signature(self, ctx:FilipinoCodeParser.Function_signatureContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#parameter_list.
    def enterParameter_list(self, ctx:FilipinoCodeParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#parameter_list.
    def exitParameter_list(self, ctx:FilipinoCodeParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#parameter.
    def enterParameter(self, ctx:FilipinoCodeParser.ParameterContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#parameter.
    def exitParameter(self, ctx:FilipinoCodeParser.ParameterContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#actual_parameter_list.
    def enterActual_parameter_list(self, ctx:FilipinoCodeParser.Actual_parameter_listContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#actual_parameter_list.
    def exitActual_parameter_list(self, ctx:FilipinoCodeParser.Actual_parameter_listContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#return_statement.
    def enterReturn_statement(self, ctx:FilipinoCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#return_statement.
    def exitReturn_statement(self, ctx:FilipinoCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#block.
    def enterBlock(self, ctx:FilipinoCodeParser.BlockContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#block.
    def exitBlock(self, ctx:FilipinoCodeParser.BlockContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#if_statement.
    def enterIf_statement(self, ctx:FilipinoCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#if_statement.
    def exitIf_statement(self, ctx:FilipinoCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#while_statement.
    def enterWhile_statement(self, ctx:FilipinoCodeParser.While_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#while_statement.
    def exitWhile_statement(self, ctx:FilipinoCodeParser.While_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#for_statement.
    def enterFor_statement(self, ctx:FilipinoCodeParser.For_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#for_statement.
    def exitFor_statement(self, ctx:FilipinoCodeParser.For_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#print_statement.
    def enterPrint_statement(self, ctx:FilipinoCodeParser.Print_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#print_statement.
    def exitPrint_statement(self, ctx:FilipinoCodeParser.Print_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#input_statement.
    def enterInput_statement(self, ctx:FilipinoCodeParser.Input_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#input_statement.
    def exitInput_statement(self, ctx:FilipinoCodeParser.Input_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#constdecl_list.
    def enterConstdecl_list(self, ctx:FilipinoCodeParser.Constdecl_listContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#constdecl_list.
    def exitConstdecl_list(self, ctx:FilipinoCodeParser.Constdecl_listContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#const_statement.
    def enterConst_statement(self, ctx:FilipinoCodeParser.Const_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#const_statement.
    def exitConst_statement(self, ctx:FilipinoCodeParser.Const_statementContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#use_list.
    def enterUse_list(self, ctx:FilipinoCodeParser.Use_listContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#use_list.
    def exitUse_list(self, ctx:FilipinoCodeParser.Use_listContext):
        pass


    # Enter a parse tree produced by FilipinoCodeParser#use_statement.
    def enterUse_statement(self, ctx:FilipinoCodeParser.Use_statementContext):
        pass

    # Exit a parse tree produced by FilipinoCodeParser#use_statement.
    def exitUse_statement(self, ctx:FilipinoCodeParser.Use_statementContext):
        pass



del FilipinoCodeParser