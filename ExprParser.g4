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

// Variable declaration
vardecl
    : VAR dataType IDENTIFIER (ASSIGN expression)? SEMICOLON
    ;

// Assignment
assignment
    : IDENTIFIER ASSIGN expression SEMICOLON
    ;

// Print statement
printStmt
    : PRINT expression SEMICOLON
    ;

// If-Else chain
ifStmt
    : IF LPAREN expression RPAREN block (ELSEIF LPAREN expression RPAREN block)* (ELSE block)?
    ;

// While loop
whileStmt
    : WHILE LPAREN expression RPAREN block
    ;

// For loop
forStmt
    : FOR LPAREN assignment expression SEMICOLON expression RPAREN block
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
    : expression (PLUS|MINUS) expression        # AddSubExpr
    | expression (MULT|DIV|MODULO) expression   # MulDivExpr
    | expression (EQ|NEQ|LT|LEQ|GT|GEQ) expression # CompareExpr
    | expression (AND|OR) expression            # LogicExpr
    | NOT expression                            # NotExpr
    | LPAREN expression RPAREN                  # ParenExpr
    | funcCall                                  # FuncCallExpr
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