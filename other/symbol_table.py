class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent  # for nested scopes later (functions, blocks)

    def define(self, name, value):
        """Create or update a variable in the current scope."""
        self.symbols[name] = value

    def assign(self, name, value):
        """Create or update a variable in the current scope."""
        self.symbols[name] = value

    def initial_resolve(self, name):
        """Initial resolver for declaring variables"""
        if name in self.symbols:
            return
        elif self.parent:
            return self.parent.initial_resolve(name)

    def resolve(self, name):
        """Look up a variable by name, checking parent scopes."""
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.resolve(name)
        else:
            raise NameError(f"Undefined variable '{name}'")

    def __repr__(self):
        return str(self.symbols)
