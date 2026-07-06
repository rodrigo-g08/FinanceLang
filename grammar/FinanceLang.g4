grammar FinanceLang;

prog
    : stmt* EOF
    ;

stmt
    : createOperation SEMI             # stmtCreate
    | deleteOperation SEMI             # stmtDelete
    | projectOperation SEMI            # stmtProject
    | showOperation SEMI               # stmtShow
    | simpleInterestOperation SEMI     # stmtSimpleInterest
    | compoundInterestOperation SEMI   # stmtCompoundInterest
    | monthlyPaymentOperation SEMI     # stmtMonthlyPayment
    | expr SEMI                        # stmtExpr
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

simpleInterestOperation
    : INTERES SIMPLE ID ASSIGN expr CON TASA expr POR NUMBER MESES
    ;

compoundInterestOperation
    : INTERES COMPUESTO ID ASSIGN expr CON TASA expr POR NUMBER MESES
    ;

monthlyPaymentOperation
    : CUOTA MENSUAL ID ASSIGN expr CON TASA expr POR NUMBER MESES
    ;

expr
    : MINUS expr                 # exprNeg
    | expr op=(MUL | DIV) expr   # exprMulDiv
    | expr op=(PLUS | MINUS) expr# exprAddSub
    | LPAREN expr RPAREN         # exprParens
    | ID                         # exprId
    | NUMBER                     # exprNum
    ;

CREAR     : 'crear' ;
OPERACION : 'operacion' ;
ELIMINAR  : 'eliminar' ;
PROYECTAR : 'proyectar' ;
MOSTRAR   : 'mostrar' ;
INTERES   : 'interes' ;
SIMPLE    : 'simple' ;
COMPUESTO : 'compuesto' ;
CUOTA     : 'cuota' ;
MENSUAL   : 'mensual' ;
POR       : 'por' ;
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

WS      : [ \t\r\n]+ -> skip ;
COMMENT : '//' ~[\r\n]* -> skip ;