from generated.grammar.FinanceLangVisitor import FinanceLangVisitor


class LLVMCodeGenerator(FinanceLangVisitor):
    def __init__(self):
        self.counter = 0
        self.symbols = {}
        self.body = []

    def temp(self):
        self.counter += 1
        return f"%t{self.counter}"

    def generate(self, tree):
        self.visit(tree)
        lines = [
            "; FinanceLang LLVM IR - Hito 3",
            "declare double @llvm.pow.f64(double, double)",
            "define double @main() {",
            "entry:",
        ]
        lines.extend(f"  {line}" for line in self.body)
        lines.append("  ret double 0.0")
        lines.append("}")
        return "\n".join(lines)

    def ensure_alloca(self, name):
        if name not in self.symbols:
            ptr = f"%{name}"
            self.symbols[name] = ptr
            self.body.insert(0, f"{ptr} = alloca double")
        return self.symbols[name]

    def visitStmtCreate(self, ctx):
        return self.visit(ctx.createOperation())

    def visitStmtDelete(self, ctx):
        return self.visit(ctx.deleteOperation())

    def visitStmtProject(self, ctx):
        return self.visit(ctx.projectOperation())

    def visitStmtShow(self, ctx):
        return self.visit(ctx.showOperation())

    def visitStmtSimpleInterest(self, ctx):
        return self.visit(ctx.simpleInterestOperation())

    def visitStmtCompoundInterest(self, ctx):
        return self.visit(ctx.compoundInterestOperation())

    def visitStmtMonthlyPayment(self, ctx):
        return self.visit(ctx.monthlyPaymentOperation())

    def visitStmtExpr(self, ctx):
        value = self.visit(ctx.expr())
        self.body.append(f"; expresión evaluada en {value}")
        return value

    def visitCreateOperation(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        ptr = self.ensure_alloca(name)
        self.body.append(f"store double {value}, double* {ptr}")
        return ptr

    def visitDeleteOperation(self, ctx):
        name = ctx.ID().getText()
        self.body.append(f"; eliminar operacion {name}")
        self.symbols.pop(name, None)
        return None

    def visitShowOperation(self, ctx):
        name = ctx.ID().getText()
        ptr = self.ensure_alloca(name)
        value = self.temp()
        self.body.append(f"{value} = load double, double* {ptr}")
        self.body.append(f"; mostrar {name} => {value}")
        return value

    def visitProjectOperation(self, ctx):
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

    def visitSimpleInterestOperation(self, ctx):
        name = ctx.ID().getText()
        base = self.visit(ctx.expr(0))
        rate = self.visit(ctx.expr(1))
        months = float(ctx.NUMBER().getText())

        tmp1 = self.temp()
        result = self.temp()
        ptr = self.ensure_alloca(name)

        self.body.append(f"{tmp1} = fmul double {base}, {rate}")
        self.body.append(f"{result} = fmul double {tmp1}, {months}")
        self.body.append(f"store double {result}, double* {ptr}")
        self.body.append(f"; interes simple {name} => {result}")

        return result

    def visitCompoundInterestOperation(self, ctx):
        name = ctx.ID().getText()
        base_value = self.visit(ctx.expr(0))
        rate = self.visit(ctx.expr(1))
        months = float(ctx.NUMBER().getText())

        base = self.temp()
        factor = self.temp()
        result = self.temp()
        ptr = self.ensure_alloca(name)

        self.body.append(f"{base} = fadd double 1.0, {rate}")
        self.body.append(f"{factor} = call double @llvm.pow.f64(double {base}, double {months})")
        self.body.append(f"{result} = fmul double {base_value}, {factor}")
        self.body.append(f"store double {result}, double* {ptr}")
        self.body.append(f"; interes compuesto {name} => {result}")

        return result

    def visitMonthlyPaymentOperation(self, ctx):
        name = ctx.ID().getText()
        principal = self.visit(ctx.expr(0))
        rate = self.visit(ctx.expr(1))
        months = float(ctx.NUMBER().getText())

        one_plus_rate = self.temp()
        exponent = self.temp()
        pow_value = self.temp()
        denominator = self.temp()
        numerator = self.temp()
        result = self.temp()
        ptr = self.ensure_alloca(name)

        self.body.append(f"{one_plus_rate} = fadd double 1.0, {rate}")
        self.body.append(f"{exponent} = fsub double 0.0, {months}")
        self.body.append(f"{pow_value} = call double @llvm.pow.f64(double {one_plus_rate}, double {exponent})")
        self.body.append(f"{denominator} = fsub double 1.0, {pow_value}")
        self.body.append(f"{numerator} = fmul double {principal}, {rate}")
        self.body.append(f"{result} = fdiv double {numerator}, {denominator}")
        self.body.append(f"store double {result}, double* {ptr}")
        self.body.append(f"; cuota mensual {name} => {result}")

        return result

    def visitExprNeg(self, ctx):
        value = self.visit(ctx.expr())
        out = self.temp()
        self.body.append(f"{out} = fsub double 0.0, {value}")
        return out

    def visitExprMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        out = self.temp()
        op = "fmul" if ctx.op.text == "*" else "fdiv"
        self.body.append(f"{out} = {op} double {left}, {right}")
        return out

    def visitExprAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        out = self.temp()
        op = "fadd" if ctx.op.text == "+" else "fsub"
        self.body.append(f"{out} = {op} double {left}, {right}")
        return out

    def visitExprParens(self, ctx):
        return self.visit(ctx.expr())

    def visitExprId(self, ctx):
        name = ctx.ID().getText()
        ptr = self.ensure_alloca(name)
        out = self.temp()
        self.body.append(f"{out} = load double, double* {ptr}")
        return out

    def visitExprNum(self, ctx):
        return ctx.NUMBER().getText()