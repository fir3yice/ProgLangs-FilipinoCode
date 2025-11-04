from antlr4 import *
from FilipinoCodeLexer import FilipinoCodeLexer
from FilipinoCodeParser import FilipinoCodeParser
from FilipinoInterpreter2 import FilipinoInterpreter

input_stream = FileStream(r"D:\_GitRepos\ProgLangs\other\test2.fil", encoding="utf-8")
lexer = FilipinoCodeLexer(input_stream)
tokens = CommonTokenStream(lexer)
parser = FilipinoCodeParser(tokens)
tree = parser.program()

interpreter = FilipinoInterpreter()
interpreter.visit(tree)
