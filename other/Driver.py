
from antlr4 import *
from FilipinoCodeLexer import FilipinoCodeLexer
from FilipinoCodeParser import FilipinoCodeParser
from antlr4.error.ErrorListener import ErrorListener


# Optional: simple custom error listener
class FilipinoErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"[Syntax Error] line {line}:{column} - {msg}")


def main():
    # Load the test file
    input_stream = FileStream(r"D:\_GitRepos\ProgLangs\other\test1.fil", encoding="utf-8")

    # Create lexer and token stream
    lexer = FilipinoCodeLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Create parser
    parser = FilipinoCodeParser(token_stream)

    # Add custom error listener
    parser.removeErrorListeners()
    parser.addErrorListener(FilipinoErrorListener())

    # Parse starting from the <program> rule
    tree = parser.program()

    # Print the parse tree (optional, for debugging)
    print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main()
