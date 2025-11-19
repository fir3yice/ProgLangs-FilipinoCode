from antlr4 import *
from FilipinoCodeLexer import FilipinoCodeLexer
from FilipinoCodeParser import FilipinoCodeParser
from FilipinoInterpreter2 import FilipinoInterpreter

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

input_stream = FileStream(r"D:\_GitRepos\ProgLangs\other\test1_iomath.fil", encoding="utf-8")
lexer = FilipinoCodeLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = FilipinoCodeParser(tokens)
tree = parser.program()

print_tree(tree)


interpreter = FilipinoInterpreter()
interpreter.visit(tree)
