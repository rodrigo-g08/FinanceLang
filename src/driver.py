import argparse
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from antlr4 import CommonTokenStream, FileStream, InputStream, Token
from generated.grammar.FinanceLangLexer import FinanceLangLexer
from generated.grammar.FinanceLangParser import FinanceLangParser
from src.codegen_llvm import LLVMCodeGenerator
from src.errors import FinanceLangSyntaxError, ThrowingErrorListener
from src.evaluator import FinanceEvaluator


def parse_code(code: str):
    lexer = FinanceLangLexer(InputStream(code))
    lexer.removeErrorListeners()
    lexer.addErrorListener(ThrowingErrorListener())

    tokens = CommonTokenStream(lexer)
    parser = FinanceLangParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())
    tree = parser.prog()
    return tree, tokens, parser


def run_file(path: str, mode: str):
    code = pathlib.Path(path).read_text(encoding="utf-8")
    tree, tokens, parser = parse_code(code)

    if mode == "tokens":
        tokens.fill()
        for token in tokens.tokens:
            if token.type == Token.EOF:
                token_name = "EOF"
            else:
                token_name = FinanceLangParser.symbolicNames[token.type]
            print(f"{token.text!r:25} -> {token_name}")
        return 0

    if mode == "tree":
        print(tree.toStringTree(recog=parser))
        return 0

    if mode == "ir":
        print(LLVMCodeGenerator().generate(tree))
        return 0

    evaluator = FinanceEvaluator()
    evaluator.visit(tree)
    for message in evaluator.messages:
        print(message)
    print("\nTabla de símbolos:")
    if evaluator.symbol_table:
        for name, value in evaluator.symbol_table.items():
            print(f"  {name:<20} = {value:,.4f}")
    else:
        print("  (vacía)")
    return 1 if evaluator.errors else 0


def main():
    parser = argparse.ArgumentParser(description="Driver de FinanceLang - Hito 2")
    parser.add_argument("input", help="Archivo .fin a procesar")
    parser.add_argument(
        "--mode",
        choices=["eval", "tokens", "tree", "ir"],
        default="eval",
        help="Modo de ejecución",
    )
    args = parser.parse_args()
    try:
        return run_file(args.input, args.mode)
    except FinanceLangSyntaxError as exc:
        print(f"[Error] {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
