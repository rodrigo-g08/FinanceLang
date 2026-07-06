from pathlib import Path
import subprocess
import sys
import os
import time


ROOT = Path(__file__).resolve().parents[1]
DEMO_FILE = ROOT / "examples" / "demo_menu.fin"
DRIVER = ROOT / "src" / "driver.py"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPresiona ENTER para continuar...")


def title():
    clear()
    print("=" * 70)
    print("                 FINANCELANG - FRONTEND DE CONSOLA")
    print("=" * 70)
    print("Lenguaje de dominio específico para operaciones financieras")
    print("ANTLR4 | Visitor semántico | Backend interpretado | LLVM IR")
    print("=" * 70)


def save_program(instructions):
    DEMO_FILE.write_text("\n".join(instructions) + "\n", encoding="utf-8")


def run_driver(mode, instructions):
    save_program(instructions)

    print("\n" + "=" * 70)
    print(f"EJECUTANDO MODO: {mode.upper()}")
    print("=" * 70 + "\n")

    subprocess.run(
        [sys.executable, str(DRIVER), str(DEMO_FILE), "--mode", mode],
        cwd=ROOT
    )


def show_program(instructions):
    print("\n" + "=" * 70)
    print("CODIGO FINANCELANG GENERADO")
    print("=" * 70)

    if not instructions:
        print("(Todavía no hay instrucciones.)")
    else:
        for i, line in enumerate(instructions, start=1):
            print(f"{i:02d}. {line}")


def load_demo():
    return [
        "crear operacion capital = 1000;",
        "crear operacion prestamo = 5000;",
        "interes simple interes_simple = capital con tasa 0.02 por 12 meses;",
        "interes compuesto monto_futuro = capital con tasa 0.02 por 12 meses;",
        "cuota mensual cuota_pago = prestamo con tasa 0.015 por 24 meses;",
        "mostrar capital;",
        "mostrar interes_simple;",
        "mostrar monto_futuro;",
        "mostrar cuota_pago;",
    ]


def show_pipeline():
    print("\n" + "=" * 70)
    print("PIPELINE DEL COMPILADOR")
    print("=" * 70)
    print("""
Programa FinanceLang (.fin)
        |
        v
Lexer de ANTLR4
        |
        v
Parser de ANTLR4
        |
        v
Arbol sintactico
        |
        v
Visitor semantico
        |
        v
Tabla de simbolos
        |
        +----------------------+
        |                      |
        v                      v
Backend interpretado       Backend LLVM IR
        |                      |
        v                      v
Salida en consola          Codigo intermedio LLVM
""")


def main():
    instructions = []

    while True:
        title()

        print("MENU PRINCIPAL")
        print("-" * 70)
        print("1. Crear operacion")
        print("2. Calcular interes simple")
        print("3. Calcular interes compuesto")
        print("4. Calcular cuota mensual")
        print("5. Mostrar variable")
        print("6. Cargar demo final automaticamente")
        print("7. Ver codigo FinanceLang generado")
        print("8. Ejecutar analisis lexico (tokens)")
        print("9. Ejecutar backend interpretado (eval)")
        print("10. Generar LLVM IR")
        print("11. Ver pipeline del compilador")
        print("12. Limpiar programa actual")
        print("0. Salir")
        print("-" * 70)

        option = input("Seleccione una opcion: ").strip()

        if option == "1":
            title()
            print("CREAR OPERACION")
            print("-" * 70)
            name = input("Nombre de la operacion: ").strip()
            value = input("Valor o expresion: ").strip()

            instructions.append(f"crear operacion {name} = {value};")

            print("\nInstruccion agregada:")
            print(f"crear operacion {name} = {value};")
            pause()

        elif option == "2":
            title()
            print("INTERES SIMPLE")
            print("-" * 70)
            name = input("Nombre del resultado: ").strip()
            base = input("Capital o variable base: ").strip()
            rate = input("Tasa decimal. Ejemplo 0.02: ").strip()
            months = input("Cantidad de meses: ").strip()

            line = f"interes simple {name} = {base} con tasa {rate} por {months} meses;"
            instructions.append(line)

            print("\nInstruccion agregada:")
            print(line)
            pause()

        elif option == "3":
            title()
            print("INTERES COMPUESTO")
            print("-" * 70)
            name = input("Nombre del resultado: ").strip()
            base = input("Capital o variable base: ").strip()
            rate = input("Tasa decimal. Ejemplo 0.02: ").strip()
            months = input("Cantidad de meses: ").strip()

            line = f"interes compuesto {name} = {base} con tasa {rate} por {months} meses;"
            instructions.append(line)

            print("\nInstruccion agregada:")
            print(line)
            pause()

        elif option == "4":
            title()
            print("CUOTA MENSUAL")
            print("-" * 70)
            name = input("Nombre del resultado: ").strip()
            base = input("Prestamo o variable base: ").strip()
            rate = input("Tasa decimal. Ejemplo 0.015: ").strip()
            months = input("Cantidad de meses: ").strip()

            line = f"cuota mensual {name} = {base} con tasa {rate} por {months} meses;"
            instructions.append(line)

            print("\nInstruccion agregada:")
            print(line)
            pause()

        elif option == "5":
            title()
            print("MOSTRAR VARIABLE")
            print("-" * 70)
            name = input("Variable a mostrar: ").strip()

            line = f"mostrar {name};"
            instructions.append(line)

            print("\nInstruccion agregada:")
            print(line)
            pause()

        elif option == "6":
            instructions = load_demo()
            title()
            print("DEMO FINAL CARGADA CORRECTAMENTE")
            show_program(instructions)
            pause()

        elif option == "7":
            title()
            show_program(instructions)
            pause()

        elif option == "8":
            title()
            if not instructions:
                print("No hay instrucciones. Primero carga la demo o crea operaciones.")
            else:
                run_driver("tokens", instructions)
            pause()

        elif option == "9":
            title()
            if not instructions:
                print("No hay instrucciones. Primero carga la demo o crea operaciones.")
            else:
                run_driver("eval", instructions)
            pause()

        elif option == "10":
            title()
            if not instructions:
                print("No hay instrucciones. Primero carga la demo o crea operaciones.")
            else:
                run_driver("ir", instructions)
            pause()

        elif option == "11":
            title()
            show_pipeline()
            pause()

        elif option == "12":
            instructions = []
            title()
            print("Programa actual limpiado.")
            pause()

        elif option == "0":
            title()
            print("Saliendo de FinanceLang...")
            time.sleep(1)
            break

        else:
            print("Opcion invalida.")
            pause()


if __name__ == "__main__":
    main()