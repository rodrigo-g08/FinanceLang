# Generated from FinanceLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .FinanceLangParser import FinanceLangParser
else:
    from FinanceLangParser import FinanceLangParser

# This class defines a complete generic visitor for a parse tree produced by FinanceLangParser.

class FinanceLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FinanceLangParser#prog.
    def visitProg(self, ctx:FinanceLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#regVariable.
    def visitRegVariable(self, ctx:FinanceLangParser.RegVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#delVariable.
    def visitDelVariable(self, ctx:FinanceLangParser.DelVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#projVariable.
    def visitProjVariable(self, ctx:FinanceLangParser.ProjVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#printExpr.
    def visitPrintExpr(self, ctx:FinanceLangParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprNeg.
    def visitExprNeg(self, ctx:FinanceLangParser.ExprNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprAddSub.
    def visitExprAddSub(self, ctx:FinanceLangParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprId.
    def visitExprId(self, ctx:FinanceLangParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprParens.
    def visitExprParens(self, ctx:FinanceLangParser.ExprParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprNum.
    def visitExprNum(self, ctx:FinanceLangParser.ExprNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprMulDiv.
    def visitExprMulDiv(self, ctx:FinanceLangParser.ExprMulDivContext):
        return self.visitChildren(ctx)



del FinanceLangParser