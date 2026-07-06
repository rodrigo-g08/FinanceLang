grammar FinanceLang;
// =======================
// PARSER
// =======================

// Punto de entrada del programa.
// Un programa FinanceLang tiene cero o más sentencias y luego termina.
prog
    : stmt* EOF
    ;

// Cada sentencia termina con punto y coma.
// SEMI representa el símbolo ';'
stmt
    : createOperation SEMI       # stmtCreate
    | deleteOperation SEMI       # stmtDelete
    | projectOperation SEMI      # stmtProject
    | showOperation SEMI         # stmtShow
    | expr SEMI                  # stmtExpr
    ;


createOperation
    : CREAR OPERACION ID ASSIGN expr
    ;
deleteOperation
    : ELIMINAR OPERACION ID
    ;
projectOperation
    : PROYECTAR ID A NUMBER MESES CON TASA expr
    ;
showOperation
    : MOSTRAR ID
    ;

expr
    : MINUS expr                 # exprNeg
    | expr op=(MUL | DIV) expr   # exprMulDiv
    | expr op=(PLUS | MINUS) expr# exprAddSub
    | LPAREN expr RPAREN         # exprParens
    | ID                         # exprId
    | NUMBER                     # exprNum
    ;


// =======================
// LEXER
// =======================

// Palabras reservadas del lenguaje.
// Importante: van antes de ID para que ANTLR las reconozca como keywords.
CREAR     : 'crear' ;
OPERACION : 'operacion' ;
ELIMINAR  : 'eliminar' ;
PROYECTAR : 'proyectar' ;
A         : 'a' ;
MESES     : 'meses' ;
CON       : 'con' ;
TASA      : 'tasa' ;
MOSTRAR   : 'mostrar' ;

// Operadores y símbolos.
PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
LPAREN : '(' ;
RPAREN : ')' ;
ASSIGN : '=' ;
SEMI   : ';' ;

// Identificadores y números.
ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;

// Espacios y comentarios.
WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;