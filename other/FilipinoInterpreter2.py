from FilipinoCodeVisitor import FilipinoCodeVisitor
from FilipinoCodeParser import FilipinoCodeParser
from symbol_table import SymbolTable


class FilipinoInterpreter(FilipinoCodeVisitor):
    def __init__(self):
        super().__init__()
        self.global_scope = SymbolTable()
    
    

    #--- Variable Declaration ---
    def visitVardecl_statement(self, ctx: FilipinoCodeParser.Vardecl_statementContext):
        data_type = ctx.data_type().getText()
        identifiers = [id_.getText() for id_ in ctx.identifier_list().IDENTIFIER()]
        for var in identifiers:
            if self.global_scope.initial_resolve(var) is not None:
                print(f"[Semantic Error] Variable '{var}' already declared.")
            else:
                self.global_scope.define(var, 0)
        return None

    # --- Assignment ---
    def visitAssignment_statement(self, ctx: FilipinoCodeParser.Assignment_statementContext):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        if self.global_scope.resolve(name) is None:
            print(f"[Runtime Error] Variable '{name}' not declared.")
        else:
            self.global_scope.assign(name, value)
        return None

    # --- Print (yawit) ---
    def visitPrint_statement(self, ctx: FilipinoCodeParser.Print_statementContext):
        values = [self.visit(expr) for expr in ctx.expression()]
        print(*values)
        return None

    # --- Expression Entry ---
    def visitExpression(self, ctx: FilipinoCodeParser.ExpressionContext):
        return self.visit(ctx.bool_expr())

    # --- Boolean Expressions ---
    def visitBool_expr(self, ctx: FilipinoCodeParser.Bool_exprContext):
        terms = ctx.bool_term()
        if len(terms) == 1:
            return self.visit(terms[0])

        result = self.visit(terms[0])
        for i in range(1, len(terms)):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(terms[i])
            if op in ("uban", "&&"):
                result = result and right
            elif op in ("maskinUnsa", "||"):
                result = result or right
        return result

    def visitBool_term(self, ctx: FilipinoCodeParser.Bool_termContext):
        if ctx.NOT():
            return not self.visit(ctx.relational_expr())
        return self.visit(ctx.relational_expr())

    # --- Relational Expressions ---
    def visitRelational_expr(self, ctx: FilipinoCodeParser.Relational_exprContext):
        ariths = ctx.arith_expr()
        if len(ariths) == 1:
            return self.visit(ariths[0])

        left = self.visit(ariths[0])
        right = self.visit(ariths[1])
        op = ctx.getChild(1).getText()

        if op == "parehasLods":
            return left == right
        elif op == "diParehasLods":
            return left != right
        elif op == "masGamay":
            return left < right
        elif op == "masDako":
            return left > right
        elif op == "saktoGamay":
            return left <= right
        elif op == "saktoDako":
            return left >= right

        return False

    # --- Arithmetic Expressions ---
    def visitArith_expr(self, ctx: FilipinoCodeParser.Arith_exprContext):
        terms = ctx.arith_term()
        result = self.visit(terms[0])
        for i in range(1, len(terms)):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(terms[i])
            if op == "dagdag":
                result += right
            elif op == "bawas":
                result -= right
        return result

    def visitArith_term(self, ctx: FilipinoCodeParser.Arith_termContext):
        factors = ctx.arith_factor()
        result = self.visit(factors[0])
        for i in range(1, len(factors)):
            op = ctx.getChild(2 * i - 1).getText()
            right = self.visit(factors[i])
            if op == "dobolDobol":
                result *= right
            elif op == "hati":
                result /= right
            elif op == "sobra":
                result %= right
        return result

    def visitArith_factor(self, ctx: FilipinoCodeParser.Arith_factorContext):
        # Handle parentheses and values
        if ctx.LPAREN():
            return self.visit(ctx.expression())
        if ctx.value():
            return self.visit(ctx.value())
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            value = self.global_scope.resolve(name)
            if value is None:
                print(f"[Runtime Error] Variable '{name}' not defined.")
            return value
        return 0

    # --- Value Literals ---
    def visitValue(self, ctx: FilipinoCodeParser.ValueContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.CHAR():
            return ctx.CHAR().getText().strip("'")
        elif ctx.BOOLEAN_LITERAL():
            return ctx.BOOLEAN_LITERAL().getText() == "meron"
        elif ctx.NULL_LITERAL():
            return None
        return 0
    
    
    # --- Program entry ---
    def visitProgram(self, ctx: FilipinoCodeParser.ProgramContext):
        # Visit all children (use list, consts, functions, main)
        for child in ctx.getChildren():
            self.visit(child)
        return None