from FilipinoCodeVisitor import FilipinoCodeVisitor
from FilipinoCodeParser import FilipinoCodeParser
from symbol_table import SymbolTable

class FilipinoInterpreter(FilipinoCodeVisitor):
    def __init__(self):
        super().__init__()
        self.global_scope = SymbolTable()

    # --- Variable declaration ---
    def visitVardecl_statement(self, ctx: FilipinoCodeParser.Vardecl_statementContext):
        data_type = ctx.data_type().getText()
        identifiers = [id_.getText() for id_ in ctx.identifier_list().IDENTIFIER()]
        for var in identifiers:
            self.global_scope.define(var, None)
        return None

    # --- Assignment ---
    def visitAssignment_statement(self, ctx: FilipinoCodeParser.Assignment_statementContext):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())  # evaluate expression first
        self.global_scope.define(name, value)
        return None

    # --- Print (yawit) ---
    def visitPrint_statement(self, ctx: FilipinoCodeParser.Print_statementContext):
        values = [self.visit(expr) for expr in ctx.expression()]
        for v in values:
            print(v)
        return None

    # --- Expression evaluation ---
    def visitExpression(self, ctx: FilipinoCodeParser.ExpressionContext):
        # For now, delegate to arithmetic/boolean
        return self.visit(ctx.bool_expr())

    def visitArith_expr(self, ctx: FilipinoCodeParser.Arith_exprContext):
        # Simple recursive evaluation
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arith_term(0))
        left = self.visit(ctx.arith_expr())
        right = self.visit(ctx.arith_term())
        op = ctx.getChild(1).getText()
        if op == 'dagdag':
            return left + right
        elif op == 'bawas':
            return left - right

    def visitArith_term(self, ctx: FilipinoCodeParser.Arith_termContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arith_factor(0))
        left = self.visit(ctx.arith_term())
        right = self.visit(ctx.arith_factor())
        op = ctx.getChild(1).getText()
        if op == 'dobolDobol':
            return left * right
        elif op == 'hati':
            return left / right
        elif op == 'sobra':
            return left % right

    def visitArith_factor(self, ctx: FilipinoCodeParser.Arith_factorContext):
        text = ctx.getText()
        # Try to interpret numbers
        try:
            if '.' in text:
                return float(text)
            else:
                return int(text)
        except ValueError:
            # Variable reference
            return self.global_scope.resolve(text)

    # # --- Program entry ---
    # def visitProgram(self, ctx: FilipinoCodeParser.ProgramContext):
    #     # Visit all statements in order
    #     for child in ctx.getChildren():
    #         self.visit(child)
    #     return None
    
    #     # === Arithmetic ===
    # def visitAddExpr(self, ctx):
    #     left = self.visit(ctx.arith_expr(0))
    #     right = self.visit(ctx.mult_expr())
    #     return left + right

    # def visitSubExpr(self, ctx):
    #     left = self.visit(ctx.arith_expr(0))
    #     right = self.visit(ctx.mult_expr())
    #     return left - right

    # def visitMulExpr(self, ctx):
    #     left = self.visit(ctx.mult_expr(0))
    #     right = self.visit(ctx.unary_expr())
    #     return left * right

    # def visitDivExpr(self, ctx):
    #     left = self.visit(ctx.mult_expr(0))
    #     right = self.visit(ctx.unary_expr())
    #     return left / right

    # def visitModuloExpr(self, ctx):
    #     left = self.visit(ctx.mult_expr(0))
    #     right = self.visit(ctx.unary_expr())
    #     return left % right

    # # === Relational ===
    # def visitRelationalOpExpr(self, ctx):
    #     left = self.visit(ctx.arith_expr(0))
    #     right = self.visit(ctx.arith_expr(1))
    #     op = ctx.getChild(1).getText()

    #     if op == 'parehasLods': return left == right
    #     elif op == 'diParehasLods': return left != right
    #     elif op == 'masGamay': return left < right
    #     elif op == 'masDako': return left > right
    #     elif op == 'saktoGamay': return left <= right
    #     elif op == 'saktoDako': return left >= right

    # # === Boolean ===
    # def visitLogicalAndExpr(self, ctx):
    #     return self.visit(ctx.boolexpr(0)) and self.visit(ctx.not_expr())

    # def visitLogicalOrExpr(self, ctx):
    #     return self.visit(ctx.boolexpr(0)) or self.visit(ctx.not_expr())

    # def visitNotExpr(self, ctx):
    #     return not self.visit(ctx.not_expr())

    # # === Value or variable ===
    # def visitValueExpr(self, ctx):
    #     if ctx.INTEGER():
    #         return int(ctx.INTEGER().getText())
    #     elif ctx.FLOAT():
    #         return float(ctx.FLOAT().getText())
    #     elif ctx.STRING():
    #         return ctx.STRING().getText().strip('"')
    #     elif ctx.BOOLEAN_LITERAL():
    #         return True if ctx.BOOLEAN_LITERAL().getText() == "meron" else False
    #     elif ctx.NULL_LITERAL():
    #         return None
    #     else:
    #         return 0  # fallback

    # def visitIdExpr(self, ctx):
    #     name = ctx.IDENTIFIER().getText()
    #     value = self.global_scope.resolve(name)
    #     if value is None:
    #         print(f"[Runtime Error] Variable '{name}' not defined.")
    #     return value

