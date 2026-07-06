"""Pruebas de humo para FinanceLang Hito 2.

Ejecutar desde la raíz del repositorio:
    python tests/test_driver_smoke.py
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DRIVER = ROOT / "src" / "driver.py"


def run(args):
    return subprocess.run(
        [sys.executable, str(DRIVER), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )


def main():
    valid = run(["examples/valid_input.fin", "--mode", "eval"])
    assert valid.returncode == 0, valid.stderr + valid.stdout
    assert "[Registro] capital" in valid.stdout
    assert "[Proyección] total" in valid.stdout

    ir = run(["examples/valid_input.fin", "--mode", "ir"])
    assert ir.returncode == 0, ir.stderr + ir.stdout
    assert "define double @main()" in ir.stdout
    assert "@llvm.pow.f64" in ir.stdout

    invalid_semantic = run(["examples/invalid_semantic.fin", "--mode", "eval"])
    assert invalid_semantic.returncode == 1
    assert "Variable 'deuda' no definida" in invalid_semantic.stdout
    assert "División por cero" in invalid_semantic.stdout

    invalid_syntax = run(["examples/invalid_syntax.fin", "--mode", "eval"])
    assert invalid_syntax.returncode == 2
    assert "Error sintáctico" in invalid_syntax.stderr

    print("Todas las pruebas de humo pasaron correctamente.")


if __name__ == "__main__":
    main()
