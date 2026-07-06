grammar FinanceLang;

// =======================
// PARSER RULES
// =======================
prog
    : stmt* EOF
    ;

stmt
    : createOperation SEMI       # stmtCreate
    | deleteOperation SEMI       # stmtDelete
    | projectOperation SEMI      # stmtProject
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

expr
    : MINUS expr                 # exprNeg
    | expr op=(MUL | DIV) expr   # exprMulDiv
    | expr op=(PLUS | MINUS) expr# exprAddSub
    | LPAREN expr RPAREN         # exprParens
    | ID                         # exprId
    | NUMBER                     # exprNum
    ;

// =======================
// LEXER RULES
// =======================
CREAR     : 'crear' ;
OPERACION : 'operacion' ;
ELIMINAR  : 'eliminar' ;
PROYECTAR : 'proyectar' ;
A         : 'a' ;
MESES     : 'meses' ;
CON       : 'con' ;
TASA      : 'tasa' ;

PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
LPAREN : '(' ;
RPAREN : ')' ;
ASSIGN : '=' ;
SEMI   : ';' ;

ID     : [a-zA-Z_][a-zA-Z0-9_]* ;
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS     : [ \t\r\n]+ -> skip ;
COMMENT: '//' ~[\r\n]* -> skip ;
