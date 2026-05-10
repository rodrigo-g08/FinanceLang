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
        4,1,19,60,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,36,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,55,8,2,10,2,12,
        2,58,9,2,1,2,0,1,4,3,0,2,4,0,2,1,0,11,12,1,0,9,10,65,0,7,1,0,0,0,
        2,35,1,0,0,0,4,46,1,0,0,0,6,8,3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,
        7,1,0,0,0,9,10,1,0,0,0,10,11,1,0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,
        13,14,5,1,0,0,14,15,5,2,0,0,15,16,5,17,0,0,16,17,5,15,0,0,17,18,
        3,4,2,0,18,19,5,16,0,0,19,36,1,0,0,0,20,21,5,3,0,0,21,22,5,2,0,0,
        22,23,5,17,0,0,23,36,5,16,0,0,24,25,5,4,0,0,25,26,5,17,0,0,26,27,
        5,5,0,0,27,28,5,18,0,0,28,29,5,6,0,0,29,30,5,7,0,0,30,31,5,8,0,0,
        31,32,3,4,2,0,32,33,5,16,0,0,33,36,1,0,0,0,34,36,3,4,2,0,35,13,1,
        0,0,0,35,20,1,0,0,0,35,24,1,0,0,0,35,34,1,0,0,0,36,3,1,0,0,0,37,
        38,6,2,-1,0,38,39,5,10,0,0,39,47,3,4,2,6,40,47,5,17,0,0,41,47,5,
        18,0,0,42,43,5,13,0,0,43,44,3,4,2,0,44,45,5,14,0,0,45,47,1,0,0,0,
        46,37,1,0,0,0,46,40,1,0,0,0,46,41,1,0,0,0,46,42,1,0,0,0,47,56,1,
        0,0,0,48,49,10,5,0,0,49,50,7,0,0,0,50,55,3,4,2,6,51,52,10,4,0,0,
        52,53,7,1,0,0,53,55,3,4,2,5,54,48,1,0,0,0,54,51,1,0,0,0,55,58,1,
        0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,58,56,1,0,0,0,5,9,
        35,46,54,56
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
                      "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stmt", "expr" ]

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
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stmt()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 402458) != 0)):
                    break

            self.state = 11
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



    class ProjVariableContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProjVariable" ):
                return visitor.visitProjVariable(self)
            else:
                return visitor.visitChildren(self)


    class RegVariableContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

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

        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegVariable" ):
                return visitor.visitRegVariable(self)
            else:
                return visitor.visitChildren(self)


    class DelVariableContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ELIMINAR(self):
            return self.getToken(FinanceLangParser.ELIMINAR, 0)
        def OPERACION(self):
            return self.getToken(FinanceLangParser.OPERACION, 0)
        def ID(self):
            return self.getToken(FinanceLangParser.ID, 0)
        def SEMI(self):
            return self.getToken(FinanceLangParser.SEMI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelVariable" ):
                return visitor.visitDelVariable(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a FinanceLangParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(FinanceLangParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = FinanceLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = FinanceLangParser.RegVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(FinanceLangParser.CREAR)
                self.state = 14
                self.match(FinanceLangParser.OPERACION)
                self.state = 15
                self.match(FinanceLangParser.ID)
                self.state = 16
                self.match(FinanceLangParser.ASSIGN)
                self.state = 17
                self.expr(0)
                self.state = 18
                self.match(FinanceLangParser.SEMI)
                pass
            elif token in [3]:
                localctx = FinanceLangParser.DelVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(FinanceLangParser.ELIMINAR)
                self.state = 21
                self.match(FinanceLangParser.OPERACION)
                self.state = 22
                self.match(FinanceLangParser.ID)
                self.state = 23
                self.match(FinanceLangParser.SEMI)
                pass
            elif token in [4]:
                localctx = FinanceLangParser.ProjVariableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                self.match(FinanceLangParser.PROYECTAR)
                self.state = 25
                self.match(FinanceLangParser.ID)
                self.state = 26
                self.match(FinanceLangParser.A)
                self.state = 27
                self.match(FinanceLangParser.NUMBER)
                self.state = 28
                self.match(FinanceLangParser.MESES)
                self.state = 29
                self.match(FinanceLangParser.CON)
                self.state = 30
                self.match(FinanceLangParser.TASA)
                self.state = 31
                self.expr(0)
                self.state = 32
                self.match(FinanceLangParser.SEMI)
                pass
            elif token in [10, 13, 17, 18]:
                localctx = FinanceLangParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 34
                self.expr(0)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = FinanceLangParser.ExprNegContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 38
                self.match(FinanceLangParser.MINUS)
                self.state = 39
                self.expr(6)
                pass
            elif token in [17]:
                localctx = FinanceLangParser.ExprIdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.match(FinanceLangParser.ID)
                pass
            elif token in [18]:
                localctx = FinanceLangParser.ExprNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.match(FinanceLangParser.NUMBER)
                pass
            elif token in [13]:
                localctx = FinanceLangParser.ExprParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.match(FinanceLangParser.LPAREN)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(FinanceLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = FinanceLangParser.ExprMulDivContext(self, FinanceLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 49
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = FinanceLangParser.ExprAddSubContext(self, FinanceLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 52
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expr(5)
                        pass

             
                self.state = 58
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
        self._predicates[2] = self.expr_sempred
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
         




