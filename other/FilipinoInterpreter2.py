from FilipinoCodeVisitor import FilipinoCodeVisitor
from FilipinoCodeParser import FilipinoCodeParser
from symbol_table import SymbolTable
from account import Account


## TODO: functions and subroutines
## TODO: increment and decrement, += -= etc?
## TODO: uselists
## TODO: error handling improvements -- undefined statements

## TODO: Domain layer double check everything or add complexity idk

allowed_types = ["bilang", "dobols", "tsismis", "emoji", "account"]

# Visitor extends parsetree huh
# Interpreter class because re-writing things into regenerated visitors is not fun
class FilipinoInterpreter(FilipinoCodeVisitor):
    def __init__(self):
        super().__init__()
        self.global_scope = SymbolTable()
        self.functions = {}
    
    
    def default_value_for_type(self, dtype):
        if dtype == "bilang": return 0
        elif dtype == "dobols": return 0.0
        elif dtype == "tsismis": return ""
        elif dtype == "emoji": return '\0'
        else: return None

    def visitConst_statement(self, ctx: FilipinoCodeParser.Const_statementContext):
        dtype = ctx.data_type().getText()
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        if name in self.global_scope.symbols:
            raise NameError(f"[Semantic Error] Constant '{name}' already declared in this scope.")
        
        if dtype == "bilang":
            if isinstance(value, float):
                print(f"[Coercion] Converting float '{value}' to int for '{name}'")
                value = int(value)
            elif isinstance(value, str):
                raise TypeError(f"[Type Error] Cannot assign string to int variable '{name}'")
        elif dtype == "dobols":  # float
            if isinstance(value, int):
                print(f"[Coercion] Converting int '{value}' to float for '{name}'")
                value = float(value)
            elif isinstance(value, str):
                raise TypeError(f"[Type Error] Cannot assign string to float variable '{name}'")

        elif dtype == "tsismis":  # string
            if not isinstance(value, str):
                raise TypeError(f"[Type Error] Expected string for '{name}', got {type(value).__name__}")

        elif dtype == "emoji":  # char
            if not (isinstance(value, str) and len(value) == 1):
                raise TypeError(f"[Type Error] Expected single character for '{name}'")
            
        elif dtype == "account":
            raise TypeError(f"[Type Error] Account types cannot be made constant but '{name}' was declared as one.")
        
        else:
            raise TypeError(f"[Type Error] Datatype does not exist for '{name}'.")
            
        self.global_scope.define(name, dtype, value, is_const=True)
        return None


    #--- Variable Declaration ---
    def visitVardecl_statement(self, ctx: FilipinoCodeParser.Vardecl_statementContext):
        data_type = ctx.data_type().getText()
        identifiers = [id_.getText() for id_ in ctx.identifier_list().IDENTIFIER()]
        for name in identifiers:

            # check if it exists as a constant
            symbol = self.global_scope.initial_resolve(name)
            if symbol is not None and symbol.is_const: # i love lazy evaluation
                raise TypeError(f"[Semantic Error] Identifier '{name}' is already defined as a constant. Choose a different name.")
            if data_type not in allowed_types:
                raise TypeError(f"[Type Error] Datatype does not exist for {name}.")

            default_val = self.default_value_for_type(data_type)
            if data_type == "account":
                self.global_scope.define(name, data_type, Account(name), is_const=False)
            else:
                self.global_scope.define(name, data_type, default_val, is_const=False)
        return None

    # --- Assignment ---
    def visitAssignment_statement(self, ctx: FilipinoCodeParser.Assignment_statementContext):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())

        try:
            symbol = self.global_scope.resolve(name)
        except NameError:
            print(f"[Runtime Error] Variable '{name}' not declared.")
            return None
        
        if symbol.is_const:
            raise TypeError(f"[Semantic Error] Cannot reassign to constant '{name}'")

        declared_type = symbol.dtype
        if declared_type == "bilang":  # int
            if isinstance(value, float):
                print(f"[Coercion] Converting float '{value}' to int for '{name}'")
                value = int(value)
            elif isinstance(value, str):
                raise TypeError(f"[Type Error] Cannot assign string to int variable '{name}'")

        elif declared_type == "dobols":  # float
            if isinstance(value, int):
                print(f"[Coercion] Converting int '{value}' to float for '{name}'")
                value = float(value)
            elif isinstance(value, str):
                raise TypeError(f"[Type Error] Cannot assign string to float variable '{name}'")

        elif declared_type == "tsismis":  # string
            if not isinstance(value, str):
                raise TypeError(f"[Type Error] Expected string for '{name}', got {type(value).__name__}")

        elif declared_type == "emoji":  # char
            if not (isinstance(value, str) and len(value) == 1):
                raise TypeError(f"[Type Error] Expected single character for '{name}'")

        symbol.value = value
        return None

    def visitPrint_statement(self, ctx: FilipinoCodeParser.Print_statementContext):
        values = [self.visit(expr) for expr in ctx.expression()]
        print(*values)
        return None

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
        if ctx.funccall():
            return self.visit(ctx.funccall())
        # Handle parentheses and values
        if ctx.LPAREN():
            return self.visit(ctx.expression())
        if ctx.value():
            return self.visit(ctx.value())
        if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            symbol = self.global_scope.resolve(name)
            if symbol is None:
                print(f"[Runtime Error] Variable '{name}' not defined.")
                return 0
            return symbol.value
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
    

    def visitInput_statement(self, ctx: FilipinoCodeParser.Input_statementContext):
        var_name = ctx.IDENTIFIER().getText()

        try:
            symbol = self.global_scope.resolve(var_name)
        except NameError:
            print(f"[Runtime Error] Variable '{var_name}' not declared.")
            return None

        user_input = input(f"[Input] {var_name} ➜ ")

        # Detect value type from input
        value = user_input
        if user_input.lower() in ["meron", "alaws"]:
            value = user_input.lower() == "meron" #TODO: Check this
        else:
            try:
                if "." in user_input:
                    value = float(user_input)
                else:
                    value = int(user_input)
            except ValueError:
                pass  # leave as string if not numeric

        dtype = symbol.dtype

        if dtype == "bilang":  # int
            if isinstance(value, float):
                print(f"[Coercion] Converting float '{value}' to int for '{var_name}'")
                value = int(value)
            elif isinstance(value, str) and not value.isdigit():
                print(f"[Type Error] Cannot assign non-numeric string '{value}' to int variable '{var_name}'")
                return None

        elif dtype == "dobols":  # float
            if isinstance(value, int):
                print(f"[Coercion] Converting int '{value}' to float for '{var_name}'")
                value = float(value)
            elif isinstance(value, str):
                try:
                    value = float(value)
                except ValueError:
                    print(f"[Type Error] Cannot assign non-numeric string '{value}' to float variable '{var_name}'")
                    return None

        elif dtype == "tsismis":  # string
            if not isinstance(value, str):
                value = str(value)

        elif dtype == "emoji":  # char
            if isinstance(value, str) and len(value) != 1:
                print(f"[Type Error] Expected single character for '{var_name}', got '{value}'")
                return None
            ##TODO: accounts

        symbol.value = value
        return None
    

    # Control flow
    def visitIf_statement(self, ctx: FilipinoCodeParser.If_statementContext):
        main_condition = self.visit(ctx.expression(0))
        if main_condition:
            self.visit(ctx.block(0))
            return None

        elif_count = len(ctx.ELSE_IF())
        for i in range(elif_count):
            cond_index = i + 1 
            block_index = i + 1
            condition = self.visit(ctx.expression(cond_index))
            if condition:
                self.visit(ctx.block(block_index))
                return None

        if ctx.ELSE():
            self.visit(ctx.block(elif_count + 1))
        return None

    
    def visitWhile_statement(self, ctx: FilipinoCodeParser.While_statementContext):
        condition = self.visit(ctx.expression())
        # could simplify it but eh
        while condition:
            try:
                self.visit(ctx.block())
                condition = self.visit(ctx.expression())  # Re-evaluate after each loop
            except BreakSignal:
                break
            except ContinueSignal:
                continue
        return None
        

    def visitFor_statement(self, ctx: FilipinoCodeParser.For_statementContext):
        # By definition the for statement can be empty
        # Also note that the identifier hsa to be declared outside of the for()
        if ctx.assignment_statement(0):  
            self.visit(ctx.assignment_statement(0))
        
        condition = True
        if ctx.expression():
            condition = self.visit(ctx.expression())

        while condition:
            try:
                self.visit(ctx.block())  # execute body
            except BreakSignal:
                break
            except ContinueSignal:
                pass

            if len(ctx.assignment_statement()) > 1:
                self.visit(ctx.assignment_statement(1))
        
            if ctx.expression():
                condition = self.visit(ctx.expression())
            else:
                condition = True
                # Since an empty conditional for loop is just a while true
                # TIL.
        return None


    def visitBreak_statement(self, ctx):
        raise BreakSignal()

    def visitContinue_statement(self, ctx):
        raise ContinueSignal()
    
    def visitReturn_statement(self, ctx):
        if ctx.expression():
            value = self.visit(ctx.expression())
        else:
            value = None
        raise ReturnSignal(value)
    
    # Scoping, based on blocks, which are based on '{ statements }'
    def visitBlock(self, ctx: FilipinoCodeParser.BlockContext):
        # Create a new scope with current as parent
        previous_scope = self.global_scope
        self.global_scope = SymbolTable(parent=previous_scope)

        for stmt in ctx.statement():
            self.visit(stmt)

        self.global_scope = previous_scope
        return None
    
    # Functions
    def visitFunction_declaration(self, ctx):
        sig = ctx.function_signature()
        name = sig.IDENTIFIER().getText()
        return_type = None

        parameters = []
        if sig.parameter_list():
            for p in sig.parameter_list().parameter():
                dtype = p.data_type().getText()
                var = p.IDENTIFIER().getText()
                parameters.append((dtype, var))

        if sig.data_type():
            return_type = sig.data_type().getText()

        self.functions[name] = FuncDef(
            name = name, params = parameters, return_type = return_type,
            ctx = ctx.function_content()
        )
        
        print (f"Function '{name}' declared with return_type '{return_type}'")
        print (ctx.function_content())

        return None
    
    # def visitFunccall_statement(self, ctx: FilipinoCodeParser.FunccallContext):
    #     func_name = ctx.IDENTIFIER().getText()
        


    
    def visitFunccall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        #print(f"Function '{name}' was called.")
        if name not in self.functions:
            raise NameError(f"[Function Error] Function '{name}' not found. Did you misspell it?")
        func = self.functions[name]

        parameters = []
        if ctx.actual_parameter_list():
            parameters = ctx.actual_parameter_list().expression()
        if len(parameters) != len(func.params):
            raise TypeError(f"[Function Error] Got {len(parameters)}, Expected {len(func.params)}")
        
        local_scope = SymbolTable(parent = self.global_scope)
        parent_scope = self.global_scope
        self.global_scope = local_scope

        for (dtype, param_name), arg in zip(func.params, parameters):
            value = self.visit(arg)
            local_scope.define(param_name, dtype, value, False)
        
        #print (f"Function '{name}' entered.")
        result = None
        try:
            result = self.visit(func.ctx)
        except ReturnSignal as ret:
            result = ret.value

        self.global_scope = parent_scope
        return result



    # Finance
    def visitDeposit_statement(self, ctx):
        amount = self.visit(ctx.expression())
        acc_name = ctx.IDENTIFIER().getText()

        account = self.global_scope.resolve(acc_name)
        if not isinstance(account.value, Account):
            raise TypeError(f"[Finance Error] '{acc_name}' is not an account.")
        account.value.deposit(amount)
        return None

    def visitWithdraw_statement(self, ctx):
        amount = self.visit(ctx.expression())
        acc_name = ctx.IDENTIFIER().getText()

        account = self.global_scope.resolve(acc_name)
        if not isinstance(account.value, Account):
            raise TypeError(f"[Finance Error] '{acc_name}' is not an account.")
        account.value.withdraw(amount)
        return None

    def visitShow_balance_statement(self, ctx):
        acc_name = ctx.IDENTIFIER().getText()
        account = self.global_scope.resolve(acc_name)
        if not isinstance(account.value, Account):
            raise TypeError(f"[Finance Error] '{acc_name}' is not an account.")
        account.value.show_balance()
        return None

    def visitTransfer_statement(self, ctx):
        amount = self.visit(ctx.expression())
        src = ctx.IDENTIFIER(0).getText()
        dest = ctx.IDENTIFIER(1).getText()

        acc1 = self.global_scope.resolve(src)
        acc2 = self.global_scope.resolve(dest)
        if not isinstance(acc1.value, Account) or not isinstance(acc2.value, Account):
            raise TypeError(f"[Finance Error] Both must be accounts.")
        acc1.value.transfer(amount, acc2.value)
        return None

    def visitInterest_statement(self, ctx):
        acc_name = ctx.IDENTIFIER().getText()
        rate = self.visit(ctx.expression())
        account = self.global_scope.resolve(acc_name)
        if not isinstance(account.value, Account):
            raise TypeError(f"[Finance Error] '{acc_name}' is not an account.")
        account.value.compute_interest(rate)
        return None




    def visitProgram(self, ctx: FilipinoCodeParser.ProgramContext):
        for child in ctx.getChildren():
            self.visit(child)
        return None
    
class BreakSignal(Exception):
    pass

class ContinueSignal(Exception):
    pass

class ReturnSignal(Exception):
    def __init__(self, value):
        self.value = value

class FuncDef():
    def __init__(self, name, params, return_type, ctx):
        self.name = name
        self.params = params  # list of (dtype, name)
        self.return_type = return_type
        self.ctx = ctx        # function_content context