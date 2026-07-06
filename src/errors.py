from antlr4.error.ErrorListener import ErrorListener


class FinanceLangSyntaxError(Exception):
    """Error sintáctico controlado para FinanceLang."""


class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise FinanceLangSyntaxError(
            f"Error sintáctico en línea {line}, columna {column}: {msg}"
        )
