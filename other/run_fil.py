from antlr4 import *
from FilipinoCodeLexer import FilipinoCodeLexer
from FilipinoCodeParser import FilipinoCodeParser
from FilipinoInterpreter2 import FilipinoInterpreter

def print_tree(node, indent=0):
    prefix = "  " * indent
    # Get the text for this node
    text = node.getText()
    
    # If it has children, print the rule name
    if hasattr(node, 'getChildCount') and node.getChildCount() > 0:
        print(f"{prefix}{type(node).__name__.replace('Context','')}")
        for i in range(node.getChildCount()):
            print_tree(node.getChild(i), indent + 1)
    else:
        # Terminal node
        print(f"{prefix}{text}")

def print_tree_lines(node, prefix="", is_last=True):
    connector = "└── " if is_last else "├── "
    
    # Node label
    if hasattr(node, "getChildCount") and node.getChildCount() > 0:
        label = type(node).__name__.replace("Context", "")
    else:
        label = node.getText()
    
    print(prefix + connector + label)
    
    # Iterate over children safely
    if hasattr(node, "getChildCount"):
        child_count = node.getChildCount()
        for i in range(child_count):
            child = node.getChild(i)
            is_last_child = i == (child_count - 1)
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree_lines(child, new_prefix, is_last_child)




input_stream = FileStream(r"D:\_GitRepos\ProgLangs\other\test1.fil", encoding="utf-8")
lexer = FilipinoCodeLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = FilipinoCodeParser(tokens)
tree = parser.program()

#print_tree_lines(tree)


interpreter = FilipinoInterpreter()
interpreter.visit(tree)
