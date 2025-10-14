lexer grammar ExprLexer;

// === KEYWORDS ===
IF              : 'ediwow';
ELSE            : 'edi';
ELSEIF          : 'ediAno';
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

// === LITERALS ===
FLOAT           : [0-9]+ '.' [0-9]+ ([eE][+-]?[0-9]+)?;
INTEGER         : [0-9]+ ([eE][+-]?[0-9]+)?;
STRING          : '"' ( ~["\\] | '\\' . )* '"';
CHAR            : '\'' ( '\\' . | ~['\\] ) '\'';

// === IDENTIFIERS ===
IDENTIFIER      : [a-zA-Z_][a-zA-Z0-9_]*;

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
