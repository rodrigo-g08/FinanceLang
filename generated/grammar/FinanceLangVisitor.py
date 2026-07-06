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


    # Visit a parse tree produced by FinanceLangParser#stmtCreate.
    def visitStmtCreate(self, ctx:FinanceLangParser.StmtCreateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtDelete.
    def visitStmtDelete(self, ctx:FinanceLangParser.StmtDeleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtProject.
    def visitStmtProject(self, ctx:FinanceLangParser.StmtProjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtShow.
    def visitStmtShow(self, ctx:FinanceLangParser.StmtShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtSimpleInterest.
    def visitStmtSimpleInterest(self, ctx:FinanceLangParser.StmtSimpleInterestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtCompoundInterest.
    def visitStmtCompoundInterest(self, ctx:FinanceLangParser.StmtCompoundInterestContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtMonthlyPayment.
    def visitStmtMonthlyPayment(self, ctx:FinanceLangParser.StmtMonthlyPaymentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#stmtExpr.
    def visitStmtExpr(self, ctx:FinanceLangParser.StmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#createOperation.
    def visitCreateOperation(self, ctx:FinanceLangParser.CreateOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#deleteOperation.
    def visitDeleteOperation(self, ctx:FinanceLangParser.DeleteOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#projectOperation.
    def visitProjectOperation(self, ctx:FinanceLangParser.ProjectOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#showOperation.
    def visitShowOperation(self, ctx:FinanceLangParser.ShowOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#simpleInterestOperation.
    def visitSimpleInterestOperation(self, ctx:FinanceLangParser.SimpleInterestOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#compoundInterestOperation.
    def visitCompoundInterestOperation(self, ctx:FinanceLangParser.CompoundInterestOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#monthlyPaymentOperation.
    def visitMonthlyPaymentOperation(self, ctx:FinanceLangParser.MonthlyPaymentOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprNeg.
    def visitExprNeg(self, ctx:FinanceLangParser.ExprNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprAddSub.
    def visitExprAddSub(self, ctx:FinanceLangParser.ExprAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprParens.
    def visitExprParens(self, ctx:FinanceLangParser.ExprParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprId.
    def visitExprId(self, ctx:FinanceLangParser.ExprIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprNum.
    def visitExprNum(self, ctx:FinanceLangParser.ExprNumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FinanceLangParser#exprMulDiv.
    def visitExprMulDiv(self, ctx:FinanceLangParser.ExprMulDivContext):
        return self.visitChildren(ctx)



del FinanceLangParser