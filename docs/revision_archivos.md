# Revisión de archivos recibidos para Hito 2

## 1. Enunciado PDF

El enunciado exige que el Hito 2 incluya: informe con lo anterior, gramática actualizada, arquitectura del compilador, plan de validación y repositorio con avance de implementación del compilador. También indica que los documentos escritos deben estar en Markdown y las imágenes en SVG.

## 2. Informe DOCX del trabajo parcial

El informe del Hito 1 contiene problemática, objetivos, descripción del lenguaje, gramática, pruebas y recomendaciones. Para Hito 2 sirve como base, pero necesita convertirse o reescribirse en Markdown y agregar tres secciones obligatorias: gramática actualizada, arquitectura del compilador y plan de validación.

## 3. Notebook del trabajo parcial

El notebook demuestra el uso de ANTLR4, generación de lexer/parser/visitor, tokens, árbol sintáctico, visitor básico y pruebas válidas/ inválidas. Es útil como evidencia, pero no debe ser el único soporte de implementación. Para Hito 2 conviene mover la lógica principal a archivos `.py` separados.

## 4. ZIP del repositorio FinanceLang

El ZIP contiene la gramática, archivos generados por ANTLR, README, notebook, JAR de ANTLR y archivo de entrada. Sin embargo, no tiene la estructura que el propio README sugiere: faltan carpetas `src`, `docs`, `examples` y `tests`. Por eso se preparó una versión reorganizada para Hito 2.

## 5. Correcciones aplicadas en la versión Hito 2

- Se creó una estructura profesional de repositorio.
- Se separó la gramática en `grammar/`.
- Se ubicó el código generado en `generated/grammar/`.
- Se creó un driver ejecutable desde consola.
- Se creó un visitor semántico con tabla de símbolos.
- Se creó un generador inicial de LLVM IR.
- Se agregaron ejemplos válidos e inválidos.
- Se agregó una prueba de humo automatizada.
- Se redactó el informe del Hito 2 en Markdown.
- Se creó el diagrama de arquitectura en SVG.
