from FilipinoCodeVisitor import FilipinoCodeVisitor
from FilipinoCodeParser import FilipinoCodeParser
from symbol_table import SymbolTable
from account import Account
from antlr4.error.ErrorListener import ErrorListener


## TODO: negative numbers (hopefully fixed, maybe fix if there's a space so like - <value> vs -<value>)
## TODO: blank assignment or incorrect assignment (the first is a raised error, the second is a warning only -> error recovery)
## TODO: Final checking/edge case stuff

## TODO: Error handling improvements (fixed maybe? remove the one in the grammar later)
## TODO: Increment and Decrement, += -= etc? probably will only implement the ++ and -- since that's what's in the grammar
## TODO: Domain layer double check everything or add complexity idk

## Conditionals
    # Lazy evaluation will allow non-boolean expressions, as long as the evaluation finishes before reaching it. I think that's kinda ok. 
    # It looks like Py actually allows expression AND/OR expression, so things like bool AND/OR 10 would resolve as True. Only 0 is False.
    # Java is stricter, allowing only bool AND/OR bool
    # Current implementation is bool/0/1 AND/OR bool/0/1

## Optimization Techniques
        #1. adding caching system for functions
        #2. lazy condition checking
        #3. added a 'kind' keyword per context, so each check is cheaper in visitArith_factor
    # Maybe convert it to AST but that is a LOT of work and I don't think there's enough time.

## Debugger
        #1. Parser level
        #2. Interpreter level
        #3. Print the parse tree

allowed_types = ["bilang", "dobols", "tsismis", "emoji", "account", "bulyan"]

# Visitor extends parsetree
# Interpreter class because re-writing things into regenerated visitors is not fun :DDDDD (definitely didn't experience that :DDDDD )
class FilipinoInterpreter(FilipinoCodeVisitor):
    def __init__(self, verbose):
        super().__init__()
        self.global_scope = SymbolTable()
        self.functions = {}
        self.imported_modules = {}
        self.verbose = verbose
        #print("verbose is:", self.verbose)
    
    
    def default_value_for_type(self, dtype):
        if dtype == "bilang": return 0
        elif dtype == "dobols": return 0.0
        elif dtype == "tsismis": return ""
        elif dtype == "emoji": return '\0'
        elif dtype == "bulyan": return False
        else: return None

    def visitConst_statement(self, ctx: FilipinoCodeParser.Const_statementContext):
        dtype = ctx.data_type().getText()
        name = ctx.IDENTIFIER().getText()
        #print(ctx.expression())
        expr_ctx = ctx.expression()
        if expr_ctx is None or expr_ctx.getChildCount() == 0 or expr_ctx.getText().strip() == "":
            raise SyntaxError(f"[Syntax Error] Missing value for constant '{name}'.")
        value = self.visit(ctx.expression())

        if name in self.global_scope.symbols:
            raise NameError(f"[Semantic Error] Constant '{name}' already declared in this scope.")
        
        if dtype == "bilang":
            if isinstance(value, float):
                print(f"[Coercion] Converting float '{value}' to int for '{name}'")
                value = int(value)
            elif isinstance(value, str):
                raise TypeError(f"[Type Error] Cannot assign string to int variable '{name}'")
        elif dtype == "dobols": 
            if isinstance(value, int):
                print(f"[Coercion] Converting int '{value}' to float for '{name}'")
                value = float(value)
            elif isinstance(value, str):
                raise TypeError(f"[Type Error] Cannot assign string to float variable '{name}'")
        elif dtype == "tsismis":  
            if not isinstance(value, str):
                raise TypeError(f"[Type Error] Expected string for '{name}', got {type(value).__name__}")
        elif dtype == "emoji":
            if not (isinstance(value, str) and len(value) == 1):
                raise TypeError(f"[Type Error] Expected single character for '{name}'")
        elif dtype == "account":
            raise TypeError(f"[Type Error] Account types cannot be made constant but '{name}' was declared as one.")
        # elif dtype == "bulyan":
        #     if not (isinstance(value, bool)):
        #         raise 
        
        else:
            raise TypeError(f"[Type Error] Datatype does not exist for '{name}'.")
            
        self.global_scope.define(name, dtype, value, is_const=True)
        if(self.verbose):
            print(f"[Debug] Constant '{name}' created with datatype '{dtype}'")
        return None


    # Variable Declaration
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

            if(self.verbose):
                print(f"[Debug] Variable '{name}' created with datatype '{data_type}'")
        return None

    # Assignment
    def visitAssignment_statement(self, ctx: FilipinoCodeParser.Assignment_statementContext):
        #print(ctx.expression())
        if ctx.expression() is None:
            raise RuntimeError(f"Missing value in variable assignment at line {ctx.start.line}")
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
                  
        elif declared_type == "bulyan": # bool
            if not isinstance(value, bool):
                raise TypeError(f"[Type Error] Expected boolean for '{name}'")
        elif declared_type == "account":

            raise TypeError(f"[Type Error] Different commands expected for '{name}' with datatype account")

        symbol.value = value
        if(self.verbose):
            print(f"[Debug] Variable '{name}' value changed to '{value}'")
        return None

    def visitPrint_statement(self, ctx: FilipinoCodeParser.Print_statementContext):
        values = [self.visit(expr) for expr in ctx.expression()]
        print(*values)
        return None

    def visitExpression(self, ctx: FilipinoCodeParser.ExpressionContext):
        return self.visit(ctx.bool_expr())
    

    def visitTry_catch_statement(self, ctx):
        try_block_ctx = ctx.block(0)
        catch_block_ctx = ctx.block(1)

        exception_var_name = ctx.IDENTIFIER().getText()

        try:
            self.visit(try_block_ctx)

        except Exception as e:
            
            original_scope = self.global_scope
            self.global_scope = SymbolTable(original_scope) 

            try:
                self.global_scope.define(exception_var_name, Exception, e, False)

                self.visit(catch_block_ctx)
                
            finally:
                self.global_scope = original_scope
        
        return None

    # Boolean Expressions 
    def visitBool_expr(self, ctx: FilipinoCodeParser.Bool_exprContext):
        terms = ctx.bool_term()
        if len(terms) == 1:
            return self.visit(terms[0])

        result = self.visit(terms[0])
        for i in range(1, len(terms)):
            op = ctx.getChild(2 * i - 1).getText()
            # right = self.visit(terms[i])
            # if op in ("uban", "&&"):
            #     result = result and right
            # elif op in ("maskinUnsa", "||"):
            #     result = result or right
            
            if op in ("uban","&&") and not result: 
                print("short circuit AND") #DEMO
                return False  # no need to evaluate right side
            if op in ("maskinUnsa","||") and result: 
                print("short circuit OR") #DEMO
                return True
            right = self.visit(terms[i])
            ## COMMENT OUT THIS LINE IF WANNA CHANGE THE CONDITIONALS 
            if((result not in [False, True, 1, 0]) or right not in [False, True, 1, 0]):
                raise ValueError(f"[Conditional Error] Conditionals can only take True or False. Got '{result}' and '{right}'")
            result = result and right if op in ("uban","&&") else result or right

        return result

    def visitBool_term(self, ctx: FilipinoCodeParser.Bool_termContext):
        if ctx.NOT():
            return not self.visit(ctx.relational_expr())
        return self.visit(ctx.relational_expr())

    # Relational 
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

    # Arithmetic Expressions
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
                if(right == 0):
                    raise ValueError("[Value Error] Division by Zero")
                result /= right
            elif op == "sobra":
                result %= right
        return result

    def visitArith_factor(self, ctx: FilipinoCodeParser.Arith_factorContext):
        #print("here")
        if ctx.getChildCount() == 2:
            #print("hhh")
            op = ctx.getChild(0).getText()
            inner = ctx.getChild(1)
            if inner.getText().startswith("-"):
                #print("here")
                pass  
            value = self.visit(inner)

            if op == "-":
                if not isinstance(value, (int, float)):
                    raise TypeError(f"[Type Error] Cannot apply unary '-' to '{value}'.")
                return -value
            elif op == "+":
                if not isinstance(value, (int, float)):
                    raise TypeError(f"[Type Error] Cannot apply unary '+' to '{value}'.")
                return +value

        if not hasattr(ctx, "kind"):
            if ctx.funccall():
                ctx.kind = "funccall"
            elif ctx.LPAREN():
                ctx.kind = "paren"
            elif ctx.value():
                ctx.kind = "value"
            elif ctx.IDENTIFIER():
                ctx.kind = "identifier"

        if ctx.kind == "funccall":
            return self.visit(ctx.funccall())
        elif ctx.kind == "paren":
            return self.visit(ctx.expression())
        elif ctx.kind == "value":
            return self.visit(ctx.value())
        elif ctx.kind == "identifier":
        # if ctx.funccall():
        #     return self.visit(ctx.funccall())
        # if ctx.LPAREN():
        #     return self.visit(ctx.expression())
        # if ctx.value():
        #     return self.visit(ctx.value())
        # if ctx.IDENTIFIER():
            name = ctx.IDENTIFIER().getText()
            if getattr(self, 'current_func', None) and self.current_func and self.current_func._local_cache and name in self.current_func._local_cache:
                #print("jere")
                return self.current_func._local_cache[name].value
            
            # if getattr(self, '_local_cache', None) and name in self._local_cache:
            #     print("using cache")
            #     return self._local_cache[name]

            
            symbol = self.global_scope.resolve(name)
            if symbol is None:
                print(f"[Runtime Error] Variable '{name}' not defined.")
                return 0
            return symbol.value
        else:
            print(f"[Syntax Error] Unknown '{name}'. Maybe you did not define it?")
        return 0

    # Value Literals 
    def visitValue(self, ctx: FilipinoCodeParser.ValueContext):
        if ctx.INTEGER():
            return int(ctx.INTEGER().getText())
        elif ctx.FLOAT():
            return float(ctx.FLOAT().getText())
        elif ctx.NEG_INTEGER():
            return int(ctx.NEG_INTEGER().getText())
        elif ctx.NEG_FLOAT():
            return float(ctx.NEG_FLOAT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText().strip('"')
        elif ctx.CHAR():
            return ctx.CHAR().getText().strip("'")
        elif ctx.BOOLEAN_LITERAL():
            return ctx.BOOLEAN_LITERAL().getText() == "Totoo"
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

        value = user_input
        if user_input.lower() in ["Totoo", "Mali"]:
            value = user_input.lower() == "Totoo" #TODO: not actually tested
        else:
            try:
                if "." in user_input:
                    value = float(user_input)
                else:
                    value = int(user_input)
            except ValueError:
                pass

        dtype = symbol.dtype

        if dtype == "bilang":
            if isinstance(value, float):
                print(f"[Coercion] Converting float '{value}' to int for '{var_name}'")
                value = int(value)
            elif isinstance(value, str) and not value.isdigit():
                print(f"[Type Error] Cannot assign non-numeric string '{value}' to int variable '{var_name}'")
                return None

        elif dtype == "dobols":
            if isinstance(value, int):
                print(f"[Coercion] Converting int '{value}' to float for '{var_name}'")
                value = float(value)
            elif isinstance(value, str):
                try:
                    value = float(value)
                except ValueError:
                    print(f"[Type Error] Cannot assign non-numeric string '{value}' to float variable '{var_name}'")
                    return None

        elif dtype == "tsismis":
            if not isinstance(value, str):
                value = str(value)

        elif dtype == "emoji":
            if isinstance(value, str) and len(value) != 1:
                print(f"[Type Error] Expected single character for '{var_name}', got '{value}'")
                return None
            ##TODO: accounts

        symbol.value = value
        return None
    

    # Control flow
    def visitIf_statement(self, ctx: FilipinoCodeParser.If_statementContext):
        if(self.verbose):
            print(f"[Debug] Entering a conditional block")
        main_condition = self.visit(ctx.expression(0))
        #print(main_condition)
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

    
    # def visitWhile_statement(self, ctx: FilipinoCodeParser.While_statementContext):
    #     condition = self.visit(ctx.expression())
    #     # could simplify it but eh
    #     while condition:
    #         try:
    #             self.visit(ctx.block())
    #             condition = self.visit(ctx.expression())
    #         except BreakSignal:
    #             break
    #         except ContinueSignal:
    #             continue
    #     return None
    def visitWhile_statement(self, ctx):
        self._local_cache = {}
        condition = self.visit(ctx.expression())
        if(self.verbose):
            print(f"[Debug] Entering a loop")
        while condition:
            try:
                self.visit(ctx.block())
                condition = self.visit(ctx.expression())
            except BreakSignal:
                break
            except ContinueSignal:
                continue
        self._local_cache = None
        if(self.verbose):
            print(f"[Debug] Exited the loop")   
        return None


    def visitFor_statement(self, ctx: FilipinoCodeParser.For_statementContext):
        # By definition the for statement can be empty
        # Also note that the identifier hsa to be declared outside of the for()
        
        if ctx.assignment_statement(0):  
            self.visit(ctx.assignment_statement(0))

        if(self.verbose):
            print(f"[Debug] Entering a loop")
        condition = True
        if ctx.expression():
            condition = self.visit(ctx.expression())

        while condition:
            try:
                self.visit(ctx.block())
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
        if(self.verbose):
            print(f"[Debug] Exited the loop")    
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
        # New scope with current as parent
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

        if name in self.functions:
            raise NameError(f"[Function Error] Function named '{name}' already exists.")

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
        if(self.verbose):
            print(f"Function '{name}' declared with return_type '{return_type}'") 
        #print (f"Function '{name}' declared with return_type '{return_type}'")
        #print (ctx.function_content())

        return None
        
    def visitFunccall(self, ctx):
        name = ctx.IDENTIFIER().getText()
        if(self.verbose):
            print(f"Function '{name}' call attempted") 
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

        # for (dtype, param_name), arg in zip(func.params, parameters):
        #     value = self.visit(arg)
        #     local_scope.define(param_name, dtype, value, False)
        

        func.local_cache = {}
        for (dtype, param_name), arg in zip(func.params, parameters):
            value = self.visit(arg)
            local_scope.define(param_name, dtype, value, False)
            func._local_cache[param_name] = local_scope.resolve(param_name)

        
        #print (f"Function '{name}' entered.")
        result = None
        # try:
        #     result = self.visit(func.ctx)
        # except ReturnSignal as ret:
        #     result = ret.value

        self.current_func = func
        try:
            result = self.visit(func.ctx)
        except ReturnSignal as ret:
            result = ret.value
        self.current_func = None

        self.global_scope = parent_scope
        if(self.verbose):
            print(f"Function '{name}' done") 
        return result
    
    def visitUse_list(self, ctx: FilipinoCodeParser.Use_listContext):
        for use_stmt in ctx.use_statement():
            self.visit(use_stmt)
        return None

    def visitUse_statement(self, ctx):
        file_name = ctx.IDENTIFIER(0).getText()
        symbol_name = ctx.IDENTIFIER(1).getText()
        #print(file_name, symbol_name)

        #read and parse the file contents and convert to part of the parse tree
        #run through those parts of the parse tree and put it into the respective scopes before proceeding with the rest

        # if symbol_name is not "fil":
        #     raise ImportError(f"[Use Error] Expected extension \'.fil\', got '{symbol_name}'")

        if file_name not in self.imported_modules:
            self.imported_modules[file_name] = set()
        self.imported_modules[file_name].add(symbol_name)

        #print("Looking for ", file_name, symbol_name)

        # TODO: Probably change the logic to just use the entire file since the parser goes through everything anyway

        module_file = f"{file_name}.{symbol_name}"  
        try:
            #module_file = r"D:\_GitRepos\ProgLangs\other\\" + module_file
            with open(module_file, "r") as f:
                source = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"[Use Error] Module '{module_file}' not found. Perhaps the module is not a \'.fil\' file or is in the wrong dir.")

        from antlr4 import InputStream, CommonTokenStream
        from FilipinoCodeLexer import FilipinoCodeLexer
        from FilipinoCodeParser import FilipinoCodeParser

        input_stream = InputStream(source)
        lexer = FilipinoCodeLexer(input_stream)
        tokens = CommonTokenStream(lexer)
        parser = FilipinoCodeParser(tokens)
        parser.removeErrorListeners()
        listener = VerboseErrorListener()
        parser.addErrorListener(listener)

        tree = parser.module()
        if(self.verbose):
            #print(f"Function '{name}' done") 
            print(f"[Use] Loading module '{module_file}'")
        self.visit(tree)
        if(self.verbose):
            print(f"[Use] Made '{symbol_name}' from module '{module_file}' available")
        return None


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
        self.params = params
        self.return_type = return_type
        self.ctx = ctx       
        self._local_cache = {}

class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #if "missing \';\' at" in msg:
            #print("")
        error_msg = f"[Syntax Error] in a use file at line {line}:{column} -> {msg}"
        self.errors.append(error_msg)
        print(error_msg)