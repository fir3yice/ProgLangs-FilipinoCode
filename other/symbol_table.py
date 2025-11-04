class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent  # for nested scopes later (functions, blocks)

    #def define(self, name, value):
    def define(self, name, dtype, value, is_const=False):
        """Create or update a variable in the current scope."""
        self.symbols[name] = Symbol(name, dtype, value, is_const)
        #TODO: CONSTANTS

    def assign(self, name, value):
        """Create or update a variable in the current scope."""
        sym = self.symbols[name]
        if sym.is_const:
            raise TypeError(f"Cannot reassign to constant '{name}'.")
        sym.value = value
        return

    def resolve(self, name):
        """Look up a variable by name, checking parent scopes."""
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.resolve(name)
        else:
            raise NameError(f"Undefined variable '{name}'")
        
    def initial_resolve(self, name):
        """Initial resolver for declaring variables"""
        if name in self.symbols:
            return
        elif self.parent:
            return self.parent.initial_resolve(name)
    

    def __repr__(self):
        return str(self.symbols)


class Symbol:
    def __init__(self, name, dtype, value=None, is_const=False):
        self.name = name
        self.dtype = dtype
        self.value = value
        self.is_const = is_const  # optional: for 'forever' constants

    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.dtype}, value={self.value}, const={self.is_const})"