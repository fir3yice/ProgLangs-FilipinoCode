import argparse
from antlr4 import *
from FilipinoCodeLexer import FilipinoCodeLexer
from FilipinoCodeParser import FilipinoCodeParser
from FilipinoInterpreter2 import FilipinoInterpreter
from antlr4.error.ErrorListener import ErrorListener

class VerboseErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        #if "missing \';\' at" in msg:
            #print("")
        error_msg = f"[Syntax Error] line {line}:{column} -> {msg}"
        self.errors.append(error_msg)
        print(error_msg)

def print_tree(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    
    if hasattr(node, "getChildCount") and node.getChildCount() > 0:
        label = type(node).__name__.replace("Context", "")
    else:
        label = node.getText()
    
    print(prefix + connector + label)
    
    if hasattr(node, "getChildCount"):
        child_count = node.getChildCount()
        for i in range(child_count):
            child = node.getChild(i)
            is_last_child = i == (child_count - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(child, new_prefix, is_last_child)

#filename repo
# test0_scoping test1_iomath test3_if_else test4_for test4_while
# test5_functions test6_use
# test10_accounts

# sample1_basic sample2_medium sample3_complex

# test_00.fil

input_stream = FileStream(r"D:\_GitRepos\ProgLangs\other\test6_use.fil", encoding="utf-8")
lexer = FilipinoCodeLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = FilipinoCodeParser(tokens)
parser.removeErrorListeners()
listener = VerboseErrorListener()
parser.addErrorListener(listener)
tree = parser.program()

#print_tree(tree)

interpreter = FilipinoInterpreter(verbose=False)
try:
    interpreter.visit(tree)
except Exception as e:
    print(f"{e}")



# on/off switch for verbose dumping of the processing that's happening within the interpreter
# so like a debugger kinda thing. 
# antlr has a feature like that already, just need to fix it together/implement with the project
# what kinda messaging tho? like everything? so like "read an 'if' at line xx" 
# basta for easier tracing. just look into the antlr one for now since we using antlr anyway
# THIS COUNTS AS AUXILLIARY FEATURES