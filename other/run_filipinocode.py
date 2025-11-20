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

def main():
    parser = argparse.ArgumentParser(description="FilipinoCode Interpreter CLI")
    parser.add_argument("file", help="FilipinoCode source file (.fil)")
    parser.add_argument(
        "--debug_p", "-dp",
        action="store_true",
        help="Enable verbose debug mode for parser"
    )
    parser.add_argument(
        "--debug_i", "-di",
        action="store_true",
        help="Enable verbose debug mode for interpreter"
    )
    parser.add_argument(
        "--print-tree", "-t",
        action="store_true",
        help="Print the parse tree before execution"
    )
    # parser.add_argument(
    #     "--interactive", "-i",
    #     action="store_true",
    #     help="Run in interactive mode after executing the file"
    # )
    args = parser.parse_args()

    args.interactive = False

    # Read file
    try:
        input_stream = FileStream(args.file, encoding="utf-8")
    except FileNotFoundError:
        print(f"[Error] File '{args.file}' not found.")
        return

    # Lexer & Parser
    lexer = FilipinoCodeLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser_obj = FilipinoCodeParser(tokens)
    parser_obj.removeErrorListeners()
    listener = VerboseErrorListener()
    parser_obj.addErrorListener(listener)

    if args.debug_p:
        parser_obj.setTrace(True)

    tree = parser_obj.program()

    # Optionally print parse tree
    if args.print_tree:
        print_tree(tree)

    # Interpreter
    interpreter = FilipinoInterpreter(args.debug_i)
    #interpreter.verbose = args.debug  # your interpreter should handle this flag
    try:
        interpreter.visit(tree)
    except Exception as e:
        print(f"[Runtime Error] {e}")
        return

    # Interactive mode
    if args.interactive:
        print("\n[Interactive Mode] Type commands or 'exit' to quit.")
        while True:
            try:
                line = input(">>> ")
                if line.strip().lower() == "exit":
                    break
                input_stream = InputStream(line)
                lexer = FilipinoCodeLexer(input_stream)
                tokens = CommonTokenStream(lexer)
                parser_obj = FilipinoCodeParser(tokens)
                tree = parser_obj.program()
                interpreter.visit(tree)
            except Exception as e:
                print(f"[Error] {e}")

if __name__ == "__main__":
    main()
