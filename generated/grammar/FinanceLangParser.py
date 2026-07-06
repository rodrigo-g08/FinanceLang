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
        4,1,20,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,63,8,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,71,8,5,10,5,12,
        5,74,9,5,1,5,0,1,10,6,0,2,4,6,8,10,0,2,1,0,11,12,1,0,9,10,78,0,15,
        1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,0,6,40,1,0,0,0,8,44,1,0,0,0,10,62,
        1,0,0,0,12,14,3,2,1,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,
        15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,1,0,
        0,0,20,21,3,4,2,0,21,22,5,16,0,0,22,33,1,0,0,0,23,24,3,6,3,0,24,
        25,5,16,0,0,25,33,1,0,0,0,26,27,3,8,4,0,27,28,5,16,0,0,28,33,1,0,
        0,0,29,30,3,10,5,0,30,31,5,16,0,0,31,33,1,0,0,0,32,20,1,0,0,0,32,
        23,1,0,0,0,32,26,1,0,0,0,32,29,1,0,0,0,33,3,1,0,0,0,34,35,5,1,0,
        0,35,36,5,2,0,0,36,37,5,17,0,0,37,38,5,15,0,0,38,39,3,10,5,0,39,
        5,1,0,0,0,40,41,5,3,0,0,41,42,5,2,0,0,42,43,5,17,0,0,43,7,1,0,0,
        0,44,45,5,4,0,0,45,46,5,17,0,0,46,47,5,5,0,0,47,48,5,18,0,0,48,49,
        5,6,0,0,49,50,5,7,0,0,50,51,5,8,0,0,51,52,3,10,5,0,52,9,1,0,0,0,
        53,54,6,5,-1,0,54,55,5,10,0,0,55,63,3,10,5,6,56,57,5,13,0,0,57,58,
        3,10,5,0,58,59,5,14,0,0,59,63,1,0,0,0,60,63,5,17,0,0,61,63,5,18,
        0,0,62,53,1,0,0,0,62,56,1,0,0,0,62,60,1,0,0,0,62,61,1,0,0,0,63,72,
        1,0,0,0,64,65,10,5,0,0,65,66,7,0,0,0,66,71,3,10,5,6,67,68,10,4,0,
        0,68,69,7,1,0,0,69,71,3,10,5,5,70,64,1,0,0,0,70,67,1,0,0,0,71,74,
        1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,11,1,0,0,0,74,72,1,0,0,0,
        5,15,32,62,70,72
    ]

class FinanceLangParser ( Parser ):

    grammarFileName = "FinanceLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'crear'", "'operacion'", "'eliminar'", 
                     "'proyectar'", "'a'", "'meses'", "'con'", "'tasa'", 
                     "'+'", "'-'", "'*'", "'/'", "'('", "')'", "'='", "';'" ]

    symbolicNames = [ "<INVALID>", "CREAR", "OPERACION", "ELIMINAR", "PROYECTAR", 
                      "A", "MESES", "CON", "TASA", "PLUS", "MINUS", "MUL", 
                      "DIV", "LPAREN", "RPAREN", "ASSIGN", "SEMI", "ID", 
                      "NUMBER", "WS", "COMMENT" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_createOperation = 2
    RULE_deleteOperation = 3
    RULE_projectOperation = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "stmt", "createOperation", "deleteOperation", 
                   "projectOperation", "expr" ]

    EOF = Token.EOF
    CREAR=1
    OPERACION=2
    ELIMINAR=3
    PROYECTAR=4
    A=5
    MESES=6
    CON=7
    TASA=8
    PLUS=9
    MINUS=10
    MUL=11
    DIV=12
    LPAREN=13
    RPAREN=14
    ASSIGN=15
    SEMI=16
    ID=17
    NUMBER=18
    WS=19
    COMMENT=20

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
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 402458) != 0):
                self.state = 12
                self.stmt()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
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



    def stmt(self):

        localctx = FinanceLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = FinanceLangParser.StmtCreateContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.createOperation()
                self.state = 21
                self.match(FinanceLangParser.SEMI)
                pass
            elif token in [3]:
                localctx = FinanceLangParser.StmtDeleteContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.deleteOperation()
                self.state = 24
                self.match(FinanceLangParser.SEMI)
                pass
            elif token in [4]:
                localctx = FinanceLangParser.StmtProjectContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.projectOperation()
                self.state = 27
                self.match(FinanceLangParser.SEMI)
                pass
            elif token in [10, 13, 17, 18]:
                localctx = FinanceLangParser.StmtExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.expr(0)
                self.state = 30
                self.match(FinanceLangParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 34
            self.match(FinanceLangParser.CREAR)
            self.state = 35
            self.match(FinanceLangParser.OPERACION)
            self.state = 36
            self.match(FinanceLangParser.ID)
            self.state = 37
            self.match(FinanceLangParser.ASSIGN)
            self.state = 38
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
            self.state = 40
            self.match(FinanceLangParser.ELIMINAR)
            self.state = 41
            self.match(FinanceLangParser.OPERACION)
            self.state = 42
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
            self.state = 44
            self.match(FinanceLangParser.PROYECTAR)
            self.state = 45
            self.match(FinanceLangParser.ID)
            self.state = 46
            self.match(FinanceLangParser.A)
            self.state = 47
            self.match(FinanceLangParser.NUMBER)
            self.state = 48
            self.match(FinanceLangParser.MESES)
            self.state = 49
            self.match(FinanceLangParser.CON)
            self.state = 50
            self.match(FinanceLangParser.TASA)
            self.state = 51
            self.expr(0)
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = FinanceLangParser.ExprNegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 54
                self.match(FinanceLangParser.MINUS)
                self.state = 55
                self.expr(6)
                pass
            elif token in [13]:
                localctx = FinanceLangParser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(FinanceLangParser.LPAREN)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(FinanceLangParser.RPAREN)
                pass
            elif token in [17]:
                localctx = FinanceLangParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(FinanceLangParser.ID)
                pass
            elif token in [18]:
                localctx = FinanceLangParser.ExprNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(FinanceLangParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 72
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 70
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = FinanceLangParser.ExprMulDivContext(self, FinanceLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 64
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 65
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 66
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = FinanceLangParser.ExprAddSubContext(self, FinanceLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 67
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 68
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 69
                        self.expr(5)
                        pass

             
                self.state = 74
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
        self._predicates[5] = self.expr_sempred
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
         




