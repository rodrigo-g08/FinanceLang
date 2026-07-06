from generated.grammar.FinanceLangParser import FinanceLangParser
from generated.grammar.FinanceLangVisitor import FinanceLangVisitor


class LLVMCodeGenerator(FinanceLangVisitor):
    """Generador LLVM IR inicial para FinanceLang.

    Avance de Hito 2: genera IR textual para operaciones aritméticas,
    almacenamiento de variables y proyección por interés compuesto mediante
    llvm.pow.f64. Todavía no ejecuta el IR; deja lista la base para integrarlo
    con llvmlite/lli en el hito final.
    """

    def __init__(self):
        self.counter = 0
        self.symbols = {}
        self.body = []
        self.comments = []

    def temp(self):
        self.counter += 1
        return f"%t{self.counter}"

    def generate(self, tree):
        self.visit(tree)
        lines = [
            "; FinanceLang LLVM IR - avance Hito 2",
            "declare double @llvm.pow.f64(double, double)",
            "define double @main() {",
            "entry:",
        ]
        lines.extend(f"  {line}" for line in self.body)
        lines.append("  ret double 0.0")
        lines.append("}")
        return "\n".join(lines)

    def ensure_alloca(self, name: str):
        if name not in self.symbols:
            ptr = f"%{name}"
            self.symbols[name] = ptr
            self.body.insert(0, f"{ptr} = alloca double")
        return self.symbols[name]

    def visitStmtCreate(self, ctx: FinanceLangParser.StmtCreateContext):
        return self.visit(ctx.createOperation())

    def visitStmtDelete(self, ctx: FinanceLangParser.StmtDeleteContext):
        return self.visit(ctx.deleteOperation())

    def visitStmtProject(self, ctx: FinanceLangParser.StmtProjectContext):
        return self.visit(ctx.projectOperation())

    def visitStmtExpr(self, ctx: FinanceLangParser.StmtExprContext):
        value = self.visit(ctx.expr())
        self.body.append(f"; expresión evaluada en {value}")
        return value

    def visitCreateOperation(self, ctx: FinanceLangParser.CreateOperationContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        ptr = self.ensure_alloca(name)
        self.body.append(f"store double {value}, double* {ptr}")
        return ptr

    def visitDeleteOperation(self, ctx: FinanceLangParser.DeleteOperationContext):
        name = ctx.ID().getText()
        self.body.append(f"; eliminar operacion {name}: liberación lógica en tabla de símbolos")
        self.symbols.pop(name, None)
        return None

    def visitProjectOperation(self, ctx: FinanceLangParser.ProjectOperationContext):
        name = ctx.ID().getText()
        months = float(ctx.NUMBER().getText())
        rate = self.visit(ctx.expr())
        ptr = self.ensure_alloca(name)
        current = self.temp()
        base = self.temp()
        factor = self.temp()
        future = self.temp()
        self.body.append(f"{current} = load double, double* {ptr}")
        self.body.append(f"{base} = fadd double 1.0, {rate}")
        self.body.append(f"{factor} = call double @llvm.pow.f64(double {base}, double {months})")
        self.body.append(f"{future} = fmul double {current}, {factor}")
        self.body.append(f"; proyectar {name} a {int(months)} meses con tasa {rate} => {future}")
        return future

    def visitExprNeg(self, ctx: FinanceLangParser.ExprNegContext):
        value = self.visit(ctx.expr())
        out = self.temp()
        self.body.append(f"{out} = fsub double 0.0, {value}")
        return out

    def visitExprMulDiv(self, ctx: FinanceLangParser.ExprMulDivContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        out = self.temp()
        op = "fmul" if ctx.op.text == "*" else "fdiv"
        self.body.append(f"{out} = {op} double {left}, {right}")
        return out

    def visitExprAddSub(self, ctx: FinanceLangParser.ExprAddSubContext):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        out = self.temp()
        op = "fadd" if ctx.op.text == "+" else "fsub"
        self.body.append(f"{out} = {op} double {left}, {right}")
        return out

    def visitExprParens(self, ctx: FinanceLangParser.ExprParensContext):
        return self.visit(ctx.expr())

    def visitExprId(self, ctx: FinanceLangParser.ExprIdContext):
        name = ctx.ID().getText()
        ptr = self.ensure_alloca(name)
        out = self.temp()
        self.body.append(f"{out} = load double, double* {ptr}")
        return out

    def visitExprNum(self, ctx: FinanceLangParser.ExprNumContext):
        return ctx.NUMBER().getText()
