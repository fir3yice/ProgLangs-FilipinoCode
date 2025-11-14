parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

// Entry rule
program
    : statement* EOF
    ;

// === STATEMENTS ===
statement
    : vardecl
    | assignment
    | incDecStmt        
    | printStmt
    | ifStmt
    | whileStmt
    | forStmt
    | funcDecl
    | funcCall SEMICOLON
    | RETURN expression? SEMICOLON
    | BREAK SEMICOLON
    | CONTINUE SEMICOLON
    ;

// Variable declaration outside loops
vardecl
    : VAR dataType IDENTIFIER (ASSIGN expression)? SEMICOLON
    ;

// Assignment statement (with semicolon)
assignment
    : IDENTIFIER ASSIGN expression SEMICOLON
    ;

// Increment / Decrement statement (standalone)
incDecStmt
    : (IDENTIFIER INCREMENT | IDENTIFIER DECREMENT) SEMICOLON
    ;

// Assignment for 'for' headers (no semicolon)
assignmentNoSemicolon
    : IDENTIFIER ASSIGN expression
    ;

// Type-only variable declaration for 'for' header
typedVarDecl
    : dataType IDENTIFIER (ASSIGN expression)?
    ;

// Print statement
printStmt
    : PRINT expression SEMICOLON
    ;

// If-ElseIf-Else chain
ifStmt
    : IF LPAREN expression RPAREN block (ELSEIF LPAREN expression RPAREN block)* (ELSE block)?
    ;

// While loop
whileStmt
    : WHILE LPAREN expression RPAREN block
    ;

// For loop
forStmt
    : FOR LPAREN (vardecl | typedVarDecl | assignmentNoSemicolon)? SEMICOLON expression? SEMICOLON expression? RPAREN block
    ;

// Function declaration
funcDecl
    : FUNCTION IDENTIFIER LPAREN paramList? RPAREN block
    ;

// Function call
funcCall
    : IDENTIFIER LPAREN argList? RPAREN
    ;

// === EXPRESSIONS ===
expression
    : IDENTIFIER ASSIGN expression              # AssignExpr
    | expression (PLUS|MINUS) expression       # AddSubExpr
    | expression (MULT|DIV|MODULO) expression  # MulDivExpr
    | expression (EQ|NEQ|LT|LEQ|GT|GEQ) expression # CompareExpr
    | expression (AND|OR) expression           # LogicExpr
    | NOT expression                            # NotExpr
    | LPAREN expression RPAREN                  # ParenExpr
    | funcCall                                  # FuncCallExpr
    | IDENTIFIER INCREMENT                       # PostIncrement
    | IDENTIFIER DECREMENT                       # PostDecrement
    | literal                                   # LiteralExpr
    | IDENTIFIER                                # IdExpr
    ;

// === TYPES & LITERALS ===
dataType
    : KW_INT
    | KW_DOUBLE
    | KW_CHAR
    | KW_STRING
    ;

literal
    : INTEGER
    | FLOAT
    | STRING
    | CHAR
    | BOOLEAN_LITERAL
    | NULL_LITERAL
    ;

// === PARAMETERS & ARGUMENTS ===
paramList
    : dataType IDENTIFIER (COMMA dataType IDENTIFIER)*
    ;

argList
    : expression (COMMA expression)*
    ;

// === BLOCK ===
block
    : LBRACE statement* RBRACE
    ;
