# FinanceLang

**FinanceLang** es un lenguaje de dominio específico orientado a operaciones financieras simples.  
El proyecto fue desarrollado para el curso **Teoría de Compiladores** y tiene como objetivo aplicar el uso de **ANTLR4** para definir una gramática, generar el analizador léxico y sintáctico, y validar instrucciones mediante un driver simple en Python.

La idea principal del lenguaje es permitir que operaciones como crear un capital, calcular intereses, eliminar registros o proyectar valores en el tiempo puedan escribirse con una sintaxis más cercana al dominio financiero.

---


## Descripción del proyecto

FinanceLang permite escribir instrucciones financieras usando una sintaxis sencilla.  
En esta primera versión, el lenguaje soporta tres acciones principales:

- Crear operaciones financieras.
- Eliminar operaciones previamente registradas.
- Proyectar una operación en el tiempo usando una tasa.

Además, permite utilizar expresiones aritméticas con:

- Suma
- Resta
- Multiplicación
- División
- Paréntesis
- Números
- Identificadores

### Ejemplo básico

```fin
crear operacion capital = 1000;
crear operacion interes = capital * 0.10;
crear operacion total = capital + interes;
proyectar total 12 meses con tasa 0.05;
eliminar operacion interes;
```

En este ejemplo se crea un capital inicial, se calcula un interés, se obtiene un total, se proyecta ese total a 12 meses y finalmente se elimina una operación registrada.

---

## Motivación

En el área financiera es común realizar cálculos repetitivos como registrar montos, calcular intereses o proyectar valores. Aunque estas tareas pueden resolverse con hojas de cálculo o lenguajes de programación generales, muchas veces requieren fórmulas o estructuras que no son tan directas para representar la lógica del problema.

FinanceLang busca plantear una sintaxis más específica para este tipo de operaciones. El objetivo no es reemplazar herramientas financieras completas, sino construir un lenguaje pequeño que permita aplicar los conceptos del curso, principalmente el diseño de gramáticas y el uso de ANTLR4.

---

## Objetivos

### Objetivo general

Diseñar e implementar una primera versión de FinanceLang, un lenguaje de dominio específico para representar operaciones financieras básicas mediante una gramática desarrollada en ANTLR4.

### Objetivos específicos

- Definir una sintaxis clara para operaciones financieras simples.
- Implementar una gramática en ANTLR4.
- Generar lexer, parser y visitor a partir de la gramática.
- Permitir expresiones aritméticas con operadores básicos.
- Validar instrucciones correctas e incorrectas mediante un driver simple.
- Mostrar tokens, árbol sintáctico y ejecución básica del lenguaje.

---

## Sintaxis del lenguaje

Todas las instrucciones en FinanceLang terminan con punto y coma.

### Crear una operación

```fin
crear operacion capital = 1000;
```

También se pueden crear operaciones usando expresiones:

```fin
crear operacion interes = capital * 0.10;
crear operacion total = capital + interes;
```

### Eliminar una operación

```fin
eliminar operacion interes;
```

### Proyectar una operación

```fin
proyectar total 12 meses con tasa 0.05;
```

---

## Gramática

La gramática principal del lenguaje se encuentra en el archivo:

```text
FinanceLang.g4
```

La estructura general del lenguaje está basada en las siguientes reglas:

```antlr
program
    : statement* EOF
    ;

statement
    : createOperation SEMI
    | deleteOperation SEMI
    | projectOperation SEMI
    ;

createOperation
    : CREAR OPERACION ID ASSIGN expr
    ;

deleteOperation
    : ELIMINAR OPERACION ID
    ;

projectOperation
    : PROYECTAR ID NUMBER MESES CON TASA NUMBER
    ;
```

Para las expresiones aritméticas, el lenguaje considera números, identificadores, paréntesis y operadores básicos:

```antlr
expr
    : expr op=(MUL | DIV) expr
    | expr op=(PLUS | MINUS) expr
    | LPAREN expr RPAREN
    | NUMBER
    | ID
    ;
```

---

## Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python 3 | Implementación del driver y visitor |
| ANTLR4 | Generación del lexer, parser y visitor |
| Google Colab | Entorno usado para desarrollo y pruebas |
| Java Runtime | Requisito para ejecutar ANTLR4 |
| antlr4-python3-runtime | Runtime de ANTLR4 para Python |

---

## Estructura del repositorio

La estructura sugerida del proyecto es la siguiente:

```text
FinanceLang/
│
├── grammar/
│   └── FinanceLang.g4
│
├── examples/
│   ├── valid_input.fin
│   └── invalid_input.fin
│
├── src/
│   └── driver.py
│
├── notebooks/
│   └── TrabajoParcial_FinanceLang.ipynb
│
├── docs/
│   └── informe.md
│
└── README.md
```

### Descripción de carpetas

| Carpeta / archivo | Descripción |
|---|---|
| `grammar/` | Contiene la gramática desarrollada en ANTLR4. |
| `examples/` | Contiene programas de prueba escritos en FinanceLang. |
| `src/` | Contiene el driver simple para probar el lenguaje. |
| `notebooks/` | Contiene el notebook usado para el desarrollo y pruebas. |
| `docs/` | Contiene el informe del trabajo parcial. |
| `README.md` | Explica el proyecto, su estructura y forma de uso. |

---

## Ejecución del proyecto

El proyecto fue probado principalmente desde **Google Colab**.

### 1. Instalar ANTLR4 y runtime de Python

```bash
pip install antlr4-python3-runtime
```

### 2. Generar los archivos del lexer, parser y visitor

Desde la carpeta donde se encuentra `FinanceLang.g4`, ejecutar:

```bash
antlr4 -Dlanguage=Python3 -visitor FinanceLang.g4
```

Este comando genera los archivos necesarios para trabajar con la gramática desde Python.

### 3. Ejecutar el driver

Luego de generar los archivos, se puede ejecutar el driver para analizar un archivo de entrada escrito en FinanceLang.

```bash
python src/driver.py
```

---

## Pruebas realizadas

Durante el desarrollo se probaron casos válidos e inválidos para revisar el comportamiento inicial del lenguaje.

### Caso válido

```fin
crear operacion capital = 1000;
crear operacion interes = capital * 0.10;
crear operacion total = capital + interes;
proyectar total 12 meses con tasa 0.05;
```

### Casos inválidos o controlados

```fin
crear operacion resultado = deuda + 100;
crear operacion division = 100 / 0;
eliminar operacion noExiste;
proyectar capital 12 meses con tasa -0.05;
```

Estas pruebas permiten verificar que la gramática reconoce correctamente la estructura del lenguaje y que el visitor puede manejar errores básicos durante la ejecución.

---

## Estado actual del proyecto

Actualmente, el proyecto cuenta con:

- Gramática inicial en ANTLR4.
- Generación de lexer y parser.
- Generación de visitor.
- Driver simple en Python.
- Pruebas de tokens.
- Visualización del árbol sintáctico.
- Evaluación básica de instrucciones.
- Manejo inicial de errores semánticos.

---

## Trabajo pendiente

Para los siguientes hitos se plantea continuar con:

- Mejor organización del front end del compilador.
- Separación entre análisis sintáctico y análisis semántico.
- Ampliación de operaciones financieras.
- Definición de un plan de validación más completo.
- Preparación de la arquitectura del compilador.
- Integración posterior con LLVM.

---

## Recomendaciones de uso

Se recomienda ejecutar primero los ejemplos válidos para revisar el funcionamiento general del lenguaje. Luego, se pueden probar los casos inválidos para comprobar el comportamiento frente a errores.

También es recomendable mantener separados los archivos de prueba, la gramática y el driver, para que el proyecto sea más fácil de revisar y continuar en los siguientes avances.

---

## Curso

**Teoría de Compiladores**  
Universidad Peruana de Ciencias Aplicadas  
Trabajo Parcial - 2026-2
