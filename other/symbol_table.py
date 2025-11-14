class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent  

    def define(self, name, dtype, value, is_const):
        self.symbols[name] = Symbol(name, dtype, value, is_const)
        #print("Symbol created", self.symbols[name].value.balance)
        

    def assign(self, name, value):
        sym = self.symbols[name]
        if sym.is_const:
            raise TypeError(f"Cannot reassign to constant '{name}'.") # The (global) constants
        sym.value = value
        return

    def resolve(self, name):
        # Lookup var name for scoping
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.resolve(name)
        else:
            raise NameError(f"Undefined variable '{name}'")
        
    def initial_resolve(self, name):
        # Initial resolver to check if the name exists in above scopes, particularly for constants
        # IE, a constant is global, the name cannot be reused in a different/child {} scope
        # this might be broken but im not 100% sure
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.initial_resolve(name)
        
    # def initial_resolve(self, name):
    #     if name in self.symbols:
    #         return self.symbols[name]
    #     elif self.parent:
    #         sym = self.parent.initial_resolve(name)
    #         if sym and sym.is_const:
    #             return sym
    #     return None

    def __repr__(self):
        return str(self.symbols)


class Symbol:
    def __init__(self, name, dtype, value=None, is_const=False):
        self.name = name
        self.dtype = dtype
        self.value = value
        self.is_const = is_const 

    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.dtype}, value={self.value}, const={self.is_const})"