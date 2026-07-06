# FinanceLang - Hito 2

FinanceLang es un lenguaje de dominio específico para representar operaciones financieras simples. Este repositorio corresponde al segundo avance del proyecto de Teoría de Compiladores.

## Estado del avance

El Hito 2 incluye:

- Gramática actualizada en ANTLR4.
- Lexer, parser y visitor generados.
- Driver de consola con modos de ejecución.
- Evaluador semántico con tabla de símbolos.
- Manejo de errores sintácticos y semánticos.
- Generador inicial de LLVM IR textual.
- Ejemplos válidos e inválidos.
- Pruebas de humo.
- Informe en Markdown.
- Diagrama de arquitectura en SVG.

## Estructura

```text
FinanceLang_Hito2/
├── grammar/                 # Gramática ANTLR4
├── generated/grammar/       # Lexer, parser y visitor generados
├── src/                     # Código fuente del compilador
├── examples/                # Entradas de prueba .fin
├── tests/                   # Pruebas automatizadas básicas
├── docs/                    # Informe y diagrama SVG
├── notebooks/               # Notebook del trabajo parcial
├── requirements.txt
└── README.md
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecutar un programa FinanceLang

```bash
python src/driver.py examples/valid_input.fin --mode eval
```

## Ver tokens

```bash
python src/driver.py examples/valid_input.fin --mode tokens
```

## Ver árbol sintáctico

```bash
python src/driver.py examples/valid_input.fin --mode tree
```

## Generar LLVM IR inicial

```bash
python src/driver.py examples/valid_input.fin --mode ir
```

## Ejecutar pruebas de humo

```bash
python tests/test_driver_smoke.py
```

## Regenerar archivos ANTLR

Desde la raíz del repositorio:

```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -no-listener -o generated grammar/FinanceLang.g4
```

## Sintaxis básica

```fin
crear operacion capital = 1000;
crear operacion interes = capital * 0.10;
crear operacion total = capital + interes;
proyectar total a 12 meses con tasa 0.05;
eliminar operacion interes;
```
