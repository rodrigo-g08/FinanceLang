grammar FinanceLang;

//PARSER
prog: stmt+ EOF;

stmt: CREAR OPERACION ID '=' expr ';' # regVariable
    | ELIMINAR OPERACION ID ';'       # delVariable
    | PROYECTAR ID A NUMBER MESES CON TASA expr ';' # projVariable
    | expr                            # printExpr
    ;

expr: '-' expr                        # exprNeg
    | expr ('*'|'/') expr             # exprMulDiv
    | expr ('+'|'-') expr             # exprAddSub
    | ID                              # exprId
    | NUMBER                          # exprNum
    | '(' expr ')'                    # exprParens
    ;

// --- LEXER ---

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
