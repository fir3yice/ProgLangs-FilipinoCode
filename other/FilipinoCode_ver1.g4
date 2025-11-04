grammar FilipinoCode;

program
    : use_list constdecl_list funcdecl_list main_function EOF
    ;

main_function
    : 'func' 'main' LPAREN RPAREN function_content // Based on "func main()" <function_content> 
    ;

function_content
    : statement* return_statement? // Modified to allow zero or more statements before an optional return
    ;

statement
    : assignment_statement SEMICOLON
    | funccall_statement SEMICOLON
    | if_statement
    | while_statement
    | for_statement
    | return_statement SEMICOLON
    | LBRACE statement* RBRACE
    | BREAK SEMICOLON
    | CONTINUE SEMICOLON
    | print_statement SEMICOLON // Added the missing print/input statements
    | input_statement SEMICOLON
    | vardecl_statement SEMICOLON // Need a rule for variable declaration
    ;

assignment_statement
    : IDENTIFIER ASSIGN (expression | funccall_statement | value) // Using IDENTIFIER for <identifier>
    ;


expression
    : boolexpr                                         // Start with the lowest precedence (boolean)
    ;

boolexpr
    : not_expr                                # ToNotExpr
    | boolexpr AND not_expr                   # LogicalAndExpr // New alternative
    | boolexpr OR not_expr                    # LogicalOrExpr  // New alternative
    ;
    
not_expr
    : NOT not_expr                                   # NotExpr
    | relational_expr                               # ToRelationalExpr
    ;
    
relational_expr
    : arith_expr (EQ | NEQ | LT | GT | LEQ | GEQ) arith_expr # RelationalOpExpr
    | arith_expr                                  # ToArithExpr // If no relational operator, it's just arithmetic
    ;

arith_expr
    : mult_expr                               # ToMultExpr     // 👈 Base Case Labelled
    | arith_expr PLUS mult_expr               # AddExpr        // Separate +
    | arith_expr MINUS mult_expr              # SubExpr        // Separate -
    ;

mult_expr
    : unary_expr                              # ToUnaryExpr    // 👈 Base Case Labelled
    | mult_expr MULT unary_expr               # MulExpr        // Separate *
    | mult_expr DIV unary_expr                # DivExpr        // Separate /
    | mult_expr MODULO unary_expr             # ModuloExpr     // Separate MODULO
    ;

unary_expr
    : INCREMENT IDENTIFIER                                 # PreIncrement
    | DECREMENT IDENTIFIER                                 # PreDecrement
    | factor                                            # ToFactorExpr
    ;


factor
    : LPAREN expression RPAREN                       # ParenthesisExpr
    | funccall_statement                             # FunctionCallExpr
    | IDENTIFIER (INCREMENT | DECREMENT)?            # IdExpr 
    | value                                          # ValueExpr
    ;

value
    : INTEGER
    | FLOAT
    | STRING
    | CHAR
    | BOOLEAN_LITERAL
    | NULL_LITERAL
    ;
    

vardecl_statement
    : VAR data_type identifier_list // 'lods bilang IDENTIFIER, IDENTIFIER'
    ;

data_type
    : KW_INT
    | KW_DOUBLE
    | KW_CHAR
    | KW_STRING
    // KW_BOOLEAN
    ;

identifier_list
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;


funcdecl_list
    : function_declaration funcdecl_list
    | // epsilon
    ;

function_declaration
    : FUNCTION function_signature function_content
    ;
    
function_signature
    : IDENTIFIER LPAREN parameter_list RPAREN (':' data_type)? // function IDENTIFIER (params) : return_type
    ;

parameter_list 
    : (parameter (COMMA parameter)*)? 
    ;

parameter
    : data_type IDENTIFIER // e.g., bilang x
    ;
    
funccall_statement
    : IDENTIFIER LPAREN actual_parameter_list RPAREN // func_name ( actual_params )
    ;

actual_parameter_list
    : expression (COMMA expression)*
    | // epsilon
    ;

return_statement
    : RETURN expression? // uwianNa expression
    ;


// Block helper rule (for statement lists in loops/if/else)
block
    : statement
    | LBRACE statement* RBRACE
    ;

// Branching Logic (Rubric 8)
if_statement
    : IF LPAREN expression RPAREN block (ELSE_IF LPAREN expression RPAREN block)* (ELSE block)?
    ;

// Iterative Logic (Rubric 9)
while_statement
    : WHILE LPAREN expression RPAREN block
    ;
    
for_statement
    : FOR LPAREN assignment_statement SEMICOLON expression SEMICOLON assignment_statement RPAREN block
    ;

// IO Statements (Rubric 10)
print_statement
    : PRINT expression (COMMA expression)* // yawit expr, expr, ...
    ;
    
input_statement
    : READ IDENTIFIER // ngutana identifier
    ;

// CONSTANTS
constdecl_list
    : const_statement constdecl_list
    | // epsilon (allows zero or more declarations)
    ;
    
const_statement
    : CONST data_type IDENTIFIER ASSIGN expression SEMICOLON// 'forever bilang X etoNaLods 100;' 
    ;

// Use/Import Statements
use_list
    : use_statement use_list
    | // epsilon
    ;

use_statement
    : 'use' IDENTIFIER '.' IDENTIFIER SEMICOLON
    ;

//lexer stuff

// === KEYWORDS ===
IF              : 'ediwow';
ELSE            : 'edi';
ELSE_IF          : 'ediAno';
WHILE           : 'weh';
FOR             : 'sakalam';
FUNCTION        : 'buhat';
RETURN          : 'uwianNa';
VAR             : 'lods';
BREAK           : 'charot';
CONTINUE        : 'padayon';
CONST           : 'forever';

// === DATA TYPES ===
KW_INT          : 'bilang';
KW_DOUBLE       : 'dobols';
KW_CHAR         : 'emoji';
KW_STRING       : 'tsismis';

// === BOOLEAN & NULL ===
BOOLEAN_LITERAL : 'meron' | 'alaws';
NULL_LITERAL    : 'waley';

// === OPERATOpRS ===
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

// === SYMBOLS ===
LPAREN          : '(';
RPAREN          : ')';
LBRACE          : '{';
RBRACE          : '}';
SEMICOLON       : ';';
COMMA           : ',';
REFERENCE       : '&';
DEREFERENCE     : '*';

// === INPUT/OUTPUT ===
READ            : 'ngutana';
PRINT           : 'yawit';

// === IDENTIFIERS ===
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;

// === LITERALS ===
FLOAT           : [0-9]+ '.' [0-9]+ ([eE][+-]?[0-9]+)?;
INTEGER         : [0-9]+ ([eE][+-]?[0-9]+)?;
STRING          : '"' ( ~["\\] | '\\' . )* '"';
CHAR            : '\'' ( '\\' . | ~['\\] ) '\'';

// === COMMENTS & WHITESPACE ===
LINE_COMMENT    : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT   : '/*' .*? '*/' -> skip;
WS              : [ \t\r\n]+ -> skip;

// === ERROR HANDLING ===
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
