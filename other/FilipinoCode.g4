grammar FilipinoCode;

program
    : use_list? constdecl_list? funcdecl_list? main_function EOF
    ;

module
    : constdecl_list? funcdecl_list? EOF
    ;

main_function
    : FUNCTION MAIN LPAREN RPAREN function_content
    ;

function_content
    : block // { statements }, change to allow single statement?
    ;

// Statements 
statement
    : assignment_statement SEMICOLON
    | funccall_stmt SEMICOLON
    | if_statement
    | while_statement
    | for_statement
    | return_statement SEMICOLON
    | block
    | break_statement
    | continue_statement
    | print_statement SEMICOLON
    | input_statement SEMICOLON
    | vardecl_statement SEMICOLON
    | deposit_statement SEMICOLON
    | withdraw_statement SEMICOLON
    | show_balance_statement SEMICOLON
    | transfer_statement SEMICOLON
    | interest_statement SEMICOLON
    ;

deposit_statement
    : DEPOSIT expression SA IDENTIFIER
    ;

withdraw_statement
    : WITHDRAW expression SA IDENTIFIER
    ;

show_balance_statement
    : SHOWBALANCE LPAREN IDENTIFIER RPAREN
    ;

transfer_statement
    : TRANSFER expression GIKAN IDENTIFIER NGADTO IDENTIFIER
    ;

interest_statement
    : COMPUTEINTEREST LPAREN IDENTIFIER COMMA expression RPAREN
    ;


break_statement 
    : BREAK SEMICOLON 
    ;

continue_statement 
    : CONTINUE SEMICOLON 
    ;

assignment_statement
    : IDENTIFIER ASSIGN ( expression | funccall | value )
    ;

// ---------------- Expressions ----------------
// Start with boolean-level rule delegating to arithmetic with precedence
expression
    : bool_expr
    ;

bool_expr
    : bool_term ( (AND | OR) bool_term )*
    ;

bool_term
    : NOT? relational_expr
    ;

relational_expr
    : arith_expr ( (EQ | NEQ | LT | GT | LEQ | GEQ) arith_expr )?
    ;

// arithmetic with precedence: +-, then */, then unary
arith_expr
    : arith_term ( (PLUS | MINUS) arith_term )*
    ;

arith_term
    : arith_factor ( (MULT | DIV | MODULO) arith_factor )*
    ;

arith_factor
    : '-' arith_factor
    | '+' arith_factor
    | (INCREMENT IDENTIFIER)          
    | (DECREMENT IDENTIFIER)           
    | IDENTIFIER (INCREMENT | DECREMENT)?
    | funccall
    | LPAREN expression RPAREN
    | value
    ;

// Values, Identifiers, and similar
value
    : INTEGER
    | FLOAT
    | STRING
    | CHAR
    | BOOLEAN_LITERAL
    | NULL_LITERAL
    ;

vardecl_statement
    : VAR data_type identifier_list
    ;

data_type
    : KW_INT
    | KW_DOUBLE
    | KW_CHAR
    | KW_STRING
    | KW_ACCOUNT
    | KW_BOOLEAN
    ;

identifier_list
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

// Functions
funcdecl_list
    : (function_declaration)*
    ;

function_declaration
    : FUNCTION function_signature function_content
    ;

function_signature
    : IDENTIFIER LPAREN parameter_list? RPAREN (':' data_type)?
    ;

// function call as expression
funccall
    : IDENTIFIER LPAREN actual_parameter_list? RPAREN
    ;

// function call as statement (alias)
funccall_stmt
    : funccall
    ;

parameter_list
    : parameter (COMMA parameter)*
    ;

parameter
    : data_type IDENTIFIER
    ;

// Parameters & returns
actual_parameter_list
    : expression (COMMA expression)*
    ;

return_statement
    : RETURN expression?
    ;

// Blocks & control flow
block
    : LBRACE statement* RBRACE
    ;

if_statement
    : IF LPAREN expression RPAREN block (ELSE_IF LPAREN expression RPAREN block)* (ELSE block)? //edit to allow only 1 line?
    ;

while_statement
    : WHILE LPAREN expression RPAREN block
    ;

for_statement
    : FOR LPAREN (assignment_statement SEMICOLON | SEMICOLON) expression? SEMICOLON assignment_statement? RPAREN block
    ;

// I/O
print_statement
    : PRINT expression (COMMA expression)*
    ;

input_statement
    : READ IDENTIFIER
    ;

// Constants & use
constdecl_list
    : (const_statement)*
    ;

const_statement
    : CONST data_type IDENTIFIER ASSIGN expression SEMICOLON
    ;

use_list
    : (use_statement)*
    ;

use_statement
    : USE IDENTIFIER '.' IDENTIFIER SEMICOLON
    ;

// Lexical Definitions 

// Main Keywords
MAIN            : 'main'; 
FUNCTION        : 'buhat';
RETURN          : 'uwianNa';
VAR             : 'lods';
BREAK           : 'charot';
CONTINUE        : 'padayon';
CONST           : 'forever';
USE             : 'use'; 

// Finance Keywords
DEPOSIT         : 'deposit';
WITHDRAW        : 'withdraw';
SHOWBALANCE     : 'showBalance';
TRANSFER        : 'transfer';
COMPUTEINTEREST : 'computeInterest';
SA              : 'sa';
GIKAN           : 'gikan';
NGADTO          : 'ngadto';

KW_ACCOUNT : 'account'; // technically should go below but yeah

// Data types
KW_INT          : 'bilang';
KW_DOUBLE       : 'dobols';
KW_CHAR         : 'emoji';
KW_STRING       : 'tsismis';
KW_BOOLEAN      : 'bulyan';


// Boolean and null
BOOLEAN_LITERAL : 'Totoo' | 'Mali';
NULL_LITERAL    : 'Waley';

// I/O
READ            : 'ngutana';
PRINT           : 'yawit';

// Operators
PLUS            : 'dagdag';
MINUS           : 'bawas';
MULT            : 'dobolDobol';
DIV             : 'hati';
MODULO          : 'sobra';

ASSIGN          : 'etoNaLods';
EQ              : 'parehasLods';
NEQ             : 'diParehasLods';
LT              : 'masGamay';
GT              : 'masDako';
LEQ             : 'saktoGamay';
GEQ             : 'saktoDako';

INCREMENT       : '++';
DECREMENT       : '--';
AND             : 'uban' | '&&';
OR              : 'maskinUnsa' | '||';
NOT             : 'dili';

// Control-flow
IF              : 'ediwow';
ELSE            : 'edi';
ELSE_IF         : 'ediAno';
WHILE           : 'weh';
FOR             : 'sakalam';

// Symbols
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
SEMICOLON       : ';';
COMMA           : ',';
 
// Identifier & data types
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;

FLOAT           : [0-9]+ '.' [0-9]+ ([eE][+-]?[0-9]+)? ;
INTEGER         : [0-9]+ ;
STRING          : '"' ( ~["\\] | '\\' . )* '"' ;
CHAR            : '\'' ( '\\' . | ~['\\] ) '\'' ;

// Comments & whitespace
LINE_COMMENT    : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip ;
WS              : [ \t\r\n]+ -> skip ;


ERROR_CHAR
    : .
      {
          import sys
          if not hasattr(sys.modules[__name__], "lexical_errors"):
              sys.modules[__name__].lexical_errors = []
          sys.modules[__name__].lexical_errors.append(
              (self.text, self.line, self.column)
          )
      }
      -> skip
    ;
