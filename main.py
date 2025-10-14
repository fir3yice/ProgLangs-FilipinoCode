from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from antlr4.error.ErrorListener import ErrorListener
import sys

class ErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line {line}, column {column}: {msg}")

def main():
    input_code = """
    lods bilang a etoNaLods 0
    weh (a masGamay 5) {
        yawit("Current: ");
        @yawit(a);
        a etoNaLods a dagdag 1;
    }
    yawit("Done!")
    """

    input_stream = InputStream(input_code)
    lexer = ExprLexer(input_stream)
    sys.modules[ExprLexer.__name__].lexical_errors = []
    tokens = CommonTokenStream(lexer)
    
    print("TOKENS:")
    lexer.reset()  
    token = lexer.nextToken()
    while token.type != Token.EOF:
        token_name = lexer.symbolicNames[token.type]
        print(f"Line {token.line:<3} Col {token.column:<3} Type: {token_name:<15} Text: {repr(token.text)}")
        token = lexer.nextToken()
    
    lexical_errors = getattr(sys.modules[ExprLexer.__name__], "lexical_errors", [])
    if lexical_errors:
        print("\nLEXICAL ERRORS:")
        for text, line, col in lexical_errors:
            print(f"Invalid character '{text}' at line {line}, column {col}")
    else:
        print("\nNo lexical errors detected.")
    
    input_stream.seek(0)
    lexer = ExprLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    parser = ExprParser(tokens)
    parser.removeErrorListeners()  
    parser.addErrorListener(ErrorListener())  
    
    try:
        tree = parser.program()  
        print("\nParse tree:")
        print(tree.toStringTree(recog=parser))
    except Exception as e:
        print(f"\nParser error: {e}")

if __name__ == '__main__':
    main()
