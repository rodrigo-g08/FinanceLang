from generated.grammar.FinanceLangVisitor import FinanceLangVisitor


class FinanceEvaluator(FinanceLangVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.messages = []
        self.errors = []

    def emit(self, message: str):
        self.messages.append(message)

    def error(self, message: str):
        self.errors.append(message)
        self.messages.append(f"[Error] {message}")

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
        if value is not None:
            self.emit(f"[Resultado] {value:,.4f}")
        return value

    def visitCreateOperation(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())

        if value is None:
            self.error(f"No se pudo registrar '{name}' porque la expresión no es válida.")
            return None

        self.symbol_table[name] = value
        self.emit(f"[Registro] {name} = {value:,.2f}")
        return value

    def visitDeleteOperation(self, ctx):
        name = ctx.ID().getText()

        if name not in self.symbol_table:
            self.error(f"No se puede eliminar '{name}' porque no existe.")
            return None

        del self.symbol_table[name]
        self.emit(f"[Eliminar] Operación '{name}' borrada de la memoria.")
        return None

    def visitShowOperation(self, ctx):
        name = ctx.ID().getText()

        if name not in self.symbol_table:
            self.error(f"No se puede mostrar '{name}' porque no existe.")
            return None

        value = self.symbol_table[name]
        self.emit(f"[Mostrar] {name} = {value:,.2f}")
        return value

    def visitProjectOperation(self, ctx):
        name = ctx.ID().getText()
        months = float(ctx.NUMBER().getText())
        rate = self.visit(ctx.expr())

        if name not in self.symbol_table:
            self.error(f"No se puede proyectar '{name}' porque no está definido.")
            return None

        if rate is None:
            self.error(f"La tasa de proyección para '{name}' no es válida.")
            return None

        if months < 0:
            self.error("La cantidad de meses no puede ser negativa.")
            return None

        if rate <= -1:
            self.error(f"Tasa {rate} inválida: debe ser mayor a -1.")
            return None

        present_value = self.symbol_table[name]
        future_value = present_value * ((1 + rate) ** months)

        self.emit(
            f"[Proyección] {name}: VP={present_value:,.2f}, meses={int(months)}, "
            f"tasa={rate:.4f}, VF={future_value:,.2f}"
        )

        return future_value

    def visitSimpleInterestOperation(self, ctx):
        name = ctx.ID().getText()
        base = self.visit(ctx.expr(0))
        rate = self.visit(ctx.expr(1))
        months = float(ctx.NUMBER().getText())

        if base is None or rate is None:
            self.error(f"No se pudo calcular el interés simple '{name}'.")
            return None

        if months < 0:
            self.error("La cantidad de meses no puede ser negativa.")
            return None

        value = base * rate * months
        self.symbol_table[name] = value

        self.emit(
            f"[Interés simple] {name}: capital={base:,.2f}, meses={int(months)}, "
            f"tasa={rate:.4f}, resultado={value:,.2f}"
        )

        return value

    def visitCompoundInterestOperation(self, ctx):
        name = ctx.ID().getText()
        base = self.visit(ctx.expr(0))
        rate = self.visit(ctx.expr(1))
        months = float(ctx.NUMBER().getText())

        if base is None or rate is None:
            self.error(f"No se pudo calcular el interés compuesto '{name}'.")
            return None

        if months < 0:
            self.error("La cantidad de meses no puede ser negativa.")
            return None

        if rate <= -1:
            self.error(f"Tasa {rate} inválida: debe ser mayor a -1.")
            return None

        value = base * ((1 + rate) ** months)
        self.symbol_table[name] = value

        self.emit(
            f"[Interés compuesto] {name}: capital={base:,.2f}, meses={int(months)}, "
            f"tasa={rate:.4f}, resultado={value:,.2f}"
        )

        return value

    def visitMonthlyPaymentOperation(self, ctx):
        name = ctx.ID().getText()
        principal = self.visit(ctx.expr(0))
        rate = self.visit(ctx.expr(1))
        months = float(ctx.NUMBER().getText())

        if principal is None or rate is None:
            self.error(f"No se pudo calcular la cuota mensual '{name}'.")
            return None

        if months <= 0:
            self.error("La cantidad de meses debe ser mayor a cero.")
            return None

        if rate <= -1:
            self.error(f"Tasa {rate} inválida: debe ser mayor a -1.")
            return None

        if rate == 0:
            value = principal / months
        else:
            value = principal * rate / (1 - (1 + rate) ** (-months))

        self.symbol_table[name] = value

        self.emit(
            f"[Cuota mensual] {name}: préstamo={principal:,.2f}, meses={int(months)}, "
            f"tasa={rate:.4f}, cuota={value:,.2f}"
        )

        return value

    def visitExprNeg(self, ctx):
        value = self.visit(ctx.expr())
        return None if value is None else -value

    def visitExprMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text

        if left is None or right is None:
            return None

        if op == "*":
            return left * right

        if right == 0:
            self.error("División por cero.")
            return None

        return left / right

    def visitExprAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text

        if left is None or right is None:
            return None

        return left + right if op == "+" else left - right

    def visitExprParens(self, ctx):
        return self.visit(ctx.expr())

    def visitExprId(self, ctx):
        name = ctx.ID().getText()

        if name not in self.symbol_table:
            self.error(f"Variable '{name}' no definida.")
            return None

        return self.symbol_table[name]

    def visitExprNum(self, ctx):
        return float(ctx.NUMBER().getText())