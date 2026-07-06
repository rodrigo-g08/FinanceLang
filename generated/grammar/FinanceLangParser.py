# Generated from FinanceLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,27,135,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,122,
        8,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,130,8,9,10,9,12,9,133,9,9,1,9,0,
        1,18,10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,18,19,1,0,16,17,137,0,23,
        1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,60,1,0,0,0,8,64,1,0,0,0,10,73,
        1,0,0,0,12,76,1,0,0,0,14,88,1,0,0,0,16,100,1,0,0,0,18,121,1,0,0,
        0,20,22,3,2,1,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,
        1,0,0,0,24,26,1,0,0,0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,
        29,3,4,2,0,29,30,5,23,0,0,30,53,1,0,0,0,31,32,3,6,3,0,32,33,5,23,
        0,0,33,53,1,0,0,0,34,35,3,8,4,0,35,36,5,23,0,0,36,53,1,0,0,0,37,
        38,3,10,5,0,38,39,5,23,0,0,39,53,1,0,0,0,40,41,3,12,6,0,41,42,5,
        23,0,0,42,53,1,0,0,0,43,44,3,14,7,0,44,45,5,23,0,0,45,53,1,0,0,0,
        46,47,3,16,8,0,47,48,5,23,0,0,48,53,1,0,0,0,49,50,3,18,9,0,50,51,
        5,23,0,0,51,53,1,0,0,0,52,28,1,0,0,0,52,31,1,0,0,0,52,34,1,0,0,0,
        52,37,1,0,0,0,52,40,1,0,0,0,52,43,1,0,0,0,52,46,1,0,0,0,52,49,1,
        0,0,0,53,3,1,0,0,0,54,55,5,1,0,0,55,56,5,2,0,0,56,57,5,24,0,0,57,
        58,5,22,0,0,58,59,3,18,9,0,59,5,1,0,0,0,60,61,5,3,0,0,61,62,5,2,
        0,0,62,63,5,24,0,0,63,7,1,0,0,0,64,65,5,4,0,0,65,66,5,24,0,0,66,
        67,5,12,0,0,67,68,5,25,0,0,68,69,5,13,0,0,69,70,5,14,0,0,70,71,5,
        15,0,0,71,72,3,18,9,0,72,9,1,0,0,0,73,74,5,5,0,0,74,75,5,24,0,0,
        75,11,1,0,0,0,76,77,5,6,0,0,77,78,5,7,0,0,78,79,5,24,0,0,79,80,5,
        22,0,0,80,81,3,18,9,0,81,82,5,14,0,0,82,83,5,15,0,0,83,84,3,18,9,
        0,84,85,5,11,0,0,85,86,5,25,0,0,86,87,5,13,0,0,87,13,1,0,0,0,88,
        89,5,6,0,0,89,90,5,8,0,0,90,91,5,24,0,0,91,92,5,22,0,0,92,93,3,18,
        9,0,93,94,5,14,0,0,94,95,5,15,0,0,95,96,3,18,9,0,96,97,5,11,0,0,
        97,98,5,25,0,0,98,99,5,13,0,0,99,15,1,0,0,0,100,101,5,9,0,0,101,
        102,5,10,0,0,102,103,5,24,0,0,103,104,5,22,0,0,104,105,3,18,9,0,
        105,106,5,14,0,0,106,107,5,15,0,0,107,108,3,18,9,0,108,109,5,11,
        0,0,109,110,5,25,0,0,110,111,5,13,0,0,111,17,1,0,0,0,112,113,6,9,
        -1,0,113,114,5,17,0,0,114,122,3,18,9,6,115,116,5,20,0,0,116,117,
        3,18,9,0,117,118,5,21,0,0,118,122,1,0,0,0,119,122,5,24,0,0,120,122,
        5,25,0,0,121,112,1,0,0,0,121,115,1,0,0,0,121,119,1,0,0,0,121,120,
        1,0,0,0,122,131,1,0,0,0,123,124,10,5,0,0,124,125,7,0,0,0,125,130,
        3,18,9,6,126,127,10,4,0,0,127,128,7,1,0,0,128,130,3,18,9,5,129,123,
        1,0,0,0,129,126,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,19,1,0,0,0,133,131,1,0,0,0,5,23,52,121,129,131
    ]

class FinanceLangParser ( Parser ):

    grammarFileName = "FinanceLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'crear'", "'operacion'", "'eliminar'", 
                     "'proyectar'", "'mostrar'", "'interes'", "'simple'", 
                     "'compuesto'", "'cuota'", "'mensual'", "'por'", "'a'", 
                     "'meses'", "'con'", "'tasa'", "'+'", "'-'", "'*'", 
                     "'/'", "'('", "')'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "CREAR", "OPERACION", "ELIMINAR", "PROYECTAR", 
                      "MOSTRAR", "INTERES", "SIMPLE", "COMPUESTO", "CUOTA", 
                      "MENSUAL", "POR", "A", "MESES", "CON", "TASA", "PLUS", 
                      "MINUS", "MUL", "DIV", "LPAREN", "RPAREN", "ASSIGN", 
                      "SEMI", "ID", "NUMBER", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_createOperation = 2
    RULE_deleteOperation = 3
    RULE_projectOperation = 4
    RULE_showOperation = 5
    RULE_simpleInterestOperation = 6
    RULE_compoundInterestOperation = 7
    RULE_monthlyPaymentOperation = 8
    RULE_expr = 9

    ruleNames =  [ "prog", "stmt", "createOperation", "deleteOperation", 
                   "projectOperation", "showOperation", "simpleInterestOperation", 
                   "compoundInterestOperation", "monthlyPaymentOperation", 
                   "expr" ]

    EOF = Token.EOF
    CREAR=1
    OPERACION=2
    ELIMINAR=3
    PROYECTAR=4
    MOSTRAR=5
    INTERES=6
    SIMPLE=7
    COMPUESTO=8
    CUOTA=9
    MENSUAL=10
    POR=11
    A=12
    MESES=13
    CON=14
    TASA=15
    PLUS=16
    MINUS=17
    MUL=18
    DIV=19
    LPAREN=20
    RPAREN=21
    ASSIGN=22
    SEMI=23
    ID=24
    NUMBER=25
    WS=26
    COMMENT=27

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FinanceLangParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(FinanceLangParser.StmtContext,i)


        def getRuleIndex(self):
            return FinanceLangParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = FinanceLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 51511930) != 0):
                self.state = 20
                self.stmt()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(FinanceLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FinanceLangParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StmtShowContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def showOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.ShowOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtShow" ):
                return visitor.visitStmtShow(self)
            else:
                return visitor.visitChildren(self)


    class StmtSimpleInterestContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simpleInterestOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.SimpleInterestOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtSimpleInterest" ):
                return visitor.visitStmtSimpleInterest(self)
            else:
                return visitor.visitChildren(self)


    class StmtCompoundInterestContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compoundInterestOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.CompoundInterestOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtCompoundInterest" ):
                return visitor.visitStmtCompoundInterest(self)
            else:
                return visitor.visitChildren(self)


    class StmtExprContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FinanceLangParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtExpr" ):
                return visitor.visitStmtExpr(self)
            else:
                return visitor.visitChildren(self)


    class StmtCreateContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def createOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.CreateOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtCreate" ):
                return visitor.visitStmtCreate(self)
            else:
                return visitor.visitChildren(self)


    class StmtProjectContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def projectOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.ProjectOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtProject" ):
                return visitor.visitStmtProject(self)
            else:
                return visitor.visitChildren(self)


    class StmtDeleteContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def deleteOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.DeleteOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtDelete" ):
                return visitor.visitStmtDelete(self)
            else:
                return visitor.visitChildren(self)


    class StmtMonthlyPaymentContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def monthlyPaymentOperation(self):
            return self.getTypedRuleContext(FinanceLangParser.MonthlyPaymentOperationContext,0)

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtMonthlyPayment" ):
                return visitor.visitStmtMonthlyPayment(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = FinanceLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = FinanceLangParser.StmtCreateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.createOperation()
                self.state = 29
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 2:
                localctx = FinanceLangParser.StmtDeleteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.deleteOperation()
                self.state = 32
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 3:
                localctx = FinanceLangParser.StmtProjectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.projectOperation()
                self.state = 35
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 4:
                localctx = FinanceLangParser.StmtShowContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 37
                self.showOperation()
                self.state = 38
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 5:
                localctx = FinanceLangParser.StmtSimpleInterestContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.simpleInterestOperation()
                self.state = 41
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 6:
                localctx = FinanceLangParser.StmtCompoundInterestContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 43
                self.compoundInterestOperation()
                self.state = 44
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 7:
                localctx = FinanceLangParser.StmtMonthlyPaymentContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.monthlyPaymentOperation()
                self.state = 47
                self.match(FinanceLangParser.SEMI)
                pass

            elif la_ == 8:
                localctx = FinanceLangParser.StmtExprContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(FinanceLangParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREAR(self):
            return self.getToken(FinanceLangParser.CREAR, 0)

        def OPERACION(self):
            return self.getToken(FinanceLangParser.OPERACION, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(FinanceLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(FinanceLangParser.ExprContext,0)


        def getRuleIndex(self):
            return FinanceLangParser.RULE_createOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateOperation" ):
                return visitor.visitCreateOperation(self)
            else:
                return visitor.visitChildren(self)




    def createOperation(self):

        localctx = FinanceLangParser.CreateOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_createOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(FinanceLangParser.CREAR)
            self.state = 55
            self.match(FinanceLangParser.OPERACION)
            self.state = 56
            self.match(FinanceLangParser.ID)
            self.state = 57
            self.match(FinanceLangParser.ASSIGN)
            self.state = 58
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIMINAR(self):
            return self.getToken(FinanceLangParser.ELIMINAR, 0)

        def OPERACION(self):
            return self.getToken(FinanceLangParser.OPERACION, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def getRuleIndex(self):
            return FinanceLangParser.RULE_deleteOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteOperation" ):
                return visitor.visitDeleteOperation(self)
            else:
                return visitor.visitChildren(self)




    def deleteOperation(self):

        localctx = FinanceLangParser.DeleteOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_deleteOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(FinanceLangParser.ELIMINAR)
            self.state = 61
            self.match(FinanceLangParser.OPERACION)
            self.state = 62
            self.match(FinanceLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProjectOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROYECTAR(self):
            return self.getToken(FinanceLangParser.PROYECTAR, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def A(self):
            return self.getToken(FinanceLangParser.A, 0)

        def NUMBER(self):
            return self.getToken(FinanceLangParser.NUMBER, 0)

        def MESES(self):
            return self.getToken(FinanceLangParser.MESES, 0)

        def CON(self):
            return self.getToken(FinanceLangParser.CON, 0)

        def TASA(self):
            return self.getToken(FinanceLangParser.TASA, 0)

        def expr(self):
            return self.getTypedRuleContext(FinanceLangParser.ExprContext,0)


        def getRuleIndex(self):
            return FinanceLangParser.RULE_projectOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProjectOperation" ):
                return visitor.visitProjectOperation(self)
            else:
                return visitor.visitChildren(self)




    def projectOperation(self):

        localctx = FinanceLangParser.ProjectOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_projectOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(FinanceLangParser.PROYECTAR)
            self.state = 65
            self.match(FinanceLangParser.ID)
            self.state = 66
            self.match(FinanceLangParser.A)
            self.state = 67
            self.match(FinanceLangParser.NUMBER)
            self.state = 68
            self.match(FinanceLangParser.MESES)
            self.state = 69
            self.match(FinanceLangParser.CON)
            self.state = 70
            self.match(FinanceLangParser.TASA)
            self.state = 71
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOSTRAR(self):
            return self.getToken(FinanceLangParser.MOSTRAR, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def getRuleIndex(self):
            return FinanceLangParser.RULE_showOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowOperation" ):
                return visitor.visitShowOperation(self)
            else:
                return visitor.visitChildren(self)




    def showOperation(self):

        localctx = FinanceLangParser.ShowOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_showOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(FinanceLangParser.MOSTRAR)
            self.state = 74
            self.match(FinanceLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SimpleInterestOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERES(self):
            return self.getToken(FinanceLangParser.INTERES, 0)

        def SIMPLE(self):
            return self.getToken(FinanceLangParser.SIMPLE, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(FinanceLangParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinanceLangParser.ExprContext,i)


        def CON(self):
            return self.getToken(FinanceLangParser.CON, 0)

        def TASA(self):
            return self.getToken(FinanceLangParser.TASA, 0)

        def POR(self):
            return self.getToken(FinanceLangParser.POR, 0)

        def NUMBER(self):
            return self.getToken(FinanceLangParser.NUMBER, 0)

        def MESES(self):
            return self.getToken(FinanceLangParser.MESES, 0)

        def getRuleIndex(self):
            return FinanceLangParser.RULE_simpleInterestOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleInterestOperation" ):
                return visitor.visitSimpleInterestOperation(self)
            else:
                return visitor.visitChildren(self)




    def simpleInterestOperation(self):

        localctx = FinanceLangParser.SimpleInterestOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_simpleInterestOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(FinanceLangParser.INTERES)
            self.state = 77
            self.match(FinanceLangParser.SIMPLE)
            self.state = 78
            self.match(FinanceLangParser.ID)
            self.state = 79
            self.match(FinanceLangParser.ASSIGN)
            self.state = 80
            self.expr(0)
            self.state = 81
            self.match(FinanceLangParser.CON)
            self.state = 82
            self.match(FinanceLangParser.TASA)
            self.state = 83
            self.expr(0)
            self.state = 84
            self.match(FinanceLangParser.POR)
            self.state = 85
            self.match(FinanceLangParser.NUMBER)
            self.state = 86
            self.match(FinanceLangParser.MESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundInterestOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTERES(self):
            return self.getToken(FinanceLangParser.INTERES, 0)

        def COMPUESTO(self):
            return self.getToken(FinanceLangParser.COMPUESTO, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(FinanceLangParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinanceLangParser.ExprContext,i)


        def CON(self):
            return self.getToken(FinanceLangParser.CON, 0)

        def TASA(self):
            return self.getToken(FinanceLangParser.TASA, 0)

        def POR(self):
            return self.getToken(FinanceLangParser.POR, 0)

        def NUMBER(self):
            return self.getToken(FinanceLangParser.NUMBER, 0)

        def MESES(self):
            return self.getToken(FinanceLangParser.MESES, 0)

        def getRuleIndex(self):
            return FinanceLangParser.RULE_compoundInterestOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundInterestOperation" ):
                return visitor.visitCompoundInterestOperation(self)
            else:
                return visitor.visitChildren(self)




    def compoundInterestOperation(self):

        localctx = FinanceLangParser.CompoundInterestOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_compoundInterestOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(FinanceLangParser.INTERES)
            self.state = 89
            self.match(FinanceLangParser.COMPUESTO)
            self.state = 90
            self.match(FinanceLangParser.ID)
            self.state = 91
            self.match(FinanceLangParser.ASSIGN)
            self.state = 92
            self.expr(0)
            self.state = 93
            self.match(FinanceLangParser.CON)
            self.state = 94
            self.match(FinanceLangParser.TASA)
            self.state = 95
            self.expr(0)
            self.state = 96
            self.match(FinanceLangParser.POR)
            self.state = 97
            self.match(FinanceLangParser.NUMBER)
            self.state = 98
            self.match(FinanceLangParser.MESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MonthlyPaymentOperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CUOTA(self):
            return self.getToken(FinanceLangParser.CUOTA, 0)

        def MENSUAL(self):
            return self.getToken(FinanceLangParser.MENSUAL, 0)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(FinanceLangParser.ASSIGN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinanceLangParser.ExprContext,i)


        def CON(self):
            return self.getToken(FinanceLangParser.CON, 0)

        def TASA(self):
            return self.getToken(FinanceLangParser.TASA, 0)

        def POR(self):
            return self.getToken(FinanceLangParser.POR, 0)

        def NUMBER(self):
            return self.getToken(FinanceLangParser.NUMBER, 0)

        def MESES(self):
            return self.getToken(FinanceLangParser.MESES, 0)

        def getRuleIndex(self):
            return FinanceLangParser.RULE_monthlyPaymentOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonthlyPaymentOperation" ):
                return visitor.visitMonthlyPaymentOperation(self)
            else:
                return visitor.visitChildren(self)




    def monthlyPaymentOperation(self):

        localctx = FinanceLangParser.MonthlyPaymentOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_monthlyPaymentOperation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(FinanceLangParser.CUOTA)
            self.state = 101
            self.match(FinanceLangParser.MENSUAL)
            self.state = 102
            self.match(FinanceLangParser.ID)
            self.state = 103
            self.match(FinanceLangParser.ASSIGN)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(FinanceLangParser.CON)
            self.state = 106
            self.match(FinanceLangParser.TASA)
            self.state = 107
            self.expr(0)
            self.state = 108
            self.match(FinanceLangParser.POR)
            self.state = 109
            self.match(FinanceLangParser.NUMBER)
            self.state = 110
            self.match(FinanceLangParser.MESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FinanceLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprNegContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(FinanceLangParser.MINUS, 0)
        def expr(self):
            return self.getTypedRuleContext(FinanceLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNeg" ):
                return visitor.visitExprNeg(self)
            else:
                return visitor.visitChildren(self)


    class ExprAddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinanceLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(FinanceLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(FinanceLangParser.MINUS, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprAddSub" ):
                return visitor.visitExprAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ExprParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(FinanceLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(FinanceLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(FinanceLangParser.RPAREN, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprParens" ):
                return visitor.visitExprParens(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprId" ):
                return visitor.visitExprId(self)
            else:
                return visitor.visitChildren(self)


    class ExprNumContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(FinanceLangParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprNum" ):
                return visitor.visitExprNum(self)
            else:
                return visitor.visitChildren(self)


    class ExprMulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FinanceLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(FinanceLangParser.ExprContext,i)

        def MUL(self):
            return self.getToken(FinanceLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(FinanceLangParser.DIV, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprMulDiv" ):
                return visitor.visitExprMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = FinanceLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = FinanceLangParser.ExprNegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 113
                self.match(FinanceLangParser.MINUS)
                self.state = 114
                self.expr(6)
                pass
            elif token in [20]:
                localctx = FinanceLangParser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(FinanceLangParser.LPAREN)
                self.state = 116
                self.expr(0)
                self.state = 117
                self.match(FinanceLangParser.RPAREN)
                pass
            elif token in [24]:
                localctx = FinanceLangParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 119
                self.match(FinanceLangParser.ID)
                pass
            elif token in [25]:
                localctx = FinanceLangParser.ExprNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(FinanceLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 129
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = FinanceLangParser.ExprMulDivContext(self, FinanceLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 124
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 125
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = FinanceLangParser.ExprAddSubContext(self, FinanceLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 126
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 127
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expr(5)
                        pass

             
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




