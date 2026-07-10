from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
DRIVER = ROOT / "src" / "driver.py"
FRONTEND_INPUT = ROOT / "examples" / "demo_frontend.fin"
DEMO_FINAL = ROOT / "examples" / "demo_final.fin"

DEFAULT_CODE = """crear operacion capital = 1000;
crear operacion prestamo = 5000;
interes simple interes_simple = capital con tasa 0.02 por 12 meses;
interes compuesto monto_futuro = capital con tasa 0.02 por 12 meses;
cuota mensual cuota_pago = prestamo con tasa 0.015 por 24 meses;
mostrar capital;
mostrar interes_simple;
mostrar monto_futuro;
mostrar cuota_pago;
"""


def load_demo_code() -> str:
    if DEMO_FINAL.exists():
        return DEMO_FINAL.read_text(encoding="utf-8")
    return DEFAULT_CODE


def run_driver(code: str, mode: str) -> tuple[int, str]:
    FRONTEND_INPUT.write_text(code.strip() + "\n", encoding="utf-8")

    completed = subprocess.run(
        [sys.executable, str(DRIVER), str(FRONTEND_INPUT), "--mode", mode],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    output = completed.stdout or ""

    if completed.stderr:
        output += "\n" + completed.stderr

    return completed.returncode, output.strip()


st.set_page_config(
    page_title="FinanceLang Demo",
    page_icon="💸",
    layout="wide",
)

st.title("💸 FinanceLang")
st.caption(
    "Frontend web para demostrar el compilador: ANTLR4 · Visitor semántico · "
    "Backend interpretado · LLVM IR"
)

with st.sidebar:
    st.header("Pipeline")
    st.markdown(
        """
        **.fin** → Lexer ANTLR → Parser ANTLR → Árbol sintáctico → Visitor semántico → Backend interpretado / LLVM IR
        """
    )

    st.divider()

    st.write(
        "Este frontend no reemplaza al compilador: permite editar código FinanceLang "
        "y ejecuta el mismo `src/driver.py`."
    )

    st.divider()

    st.markdown("### Modos disponibles")
    st.markdown(
        """
        - **Tokens:** análisis léxico.
        - **Ejecutar:** backend interpretado.
        - **LLVM IR:** generación de código intermedio.
        """
    )

if "code" not in st.session_state:
    st.session_state.code = load_demo_code()

col_a, col_b = st.columns([1.15, 1])

with col_a:
    st.subheader("Programa FinanceLang")

    st.session_state.code = st.text_area(
        "Edita o carga el programa de demostración",
        value=st.session_state.code,
        height=330,
        label_visibility="collapsed",
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        if st.button("Cargar demo", use_container_width=True):
            st.session_state.code = load_demo_code()
            st.rerun()

    with c2:
        run_tokens = st.button("Tokens", use_container_width=True)

    with c3:
        run_eval = st.button("Ejecutar", use_container_width=True)

    with c4:
        run_ir = st.button("LLVM IR", use_container_width=True)

with col_b:
    st.subheader("Operaciones soportadas")

    st.markdown(
        """
        - `crear operacion nombre = expr;`
        - `interes simple resultado = capital con tasa r por n meses;`
        - `interes compuesto resultado = capital con tasa r por n meses;`
        - `cuota mensual resultado = prestamo con tasa r por n meses;`
        - `proyectar capital a n meses con tasa r;`
        - `mostrar variable;`
        """
    )

    st.info("Las tasas se ingresan en decimal. Ejemplo: `0.02` representa 2%.")

    st.markdown("### Fórmulas")
    st.code(
        """Interés simple:
resultado = capital * tasa * meses

Interés compuesto:
resultado = capital * (1 + tasa) ^ meses

Cuota mensual:
cuota = P * r / (1 - (1 + r)^(-n))""",
        language="text",
    )

mode_to_run = None

if run_tokens:
    mode_to_run = "tokens"
elif run_eval:
    mode_to_run = "eval"
elif run_ir:
    mode_to_run = "ir"

st.divider()
st.subheader("Resultado")

if mode_to_run:
    with st.spinner(f"Ejecutando modo {mode_to_run}..."):
        returncode, output = run_driver(st.session_state.code, mode_to_run)

    if returncode == 0:
        st.success(f"Ejecución finalizada correctamente. Código de salida: {returncode}")
    elif returncode == 1:
        st.warning(
            f"Ejecución finalizada con errores semánticos. Código de salida: {returncode}"
        )
    else:
        st.error(
            f"Ejecución finalizada con error sintáctico o de compilación. "
            f"Código de salida: {returncode}"
        )

    st.code(output or "(sin salida)", language="text")
else:
    st.code("Selecciona Tokens, Ejecutar o LLVM IR para ver la salida.", language="text")

with st.expander("Ver explicación del flujo"):
    st.markdown(
        """
        1. El usuario escribe o carga un programa FinanceLang.
        2. El frontend guarda temporalmente el archivo `.fin`.
        3. Se ejecuta `src/driver.py` con el modo seleccionado.
        4. ANTLR genera tokens y árbol sintáctico.
        5. El visitor semántico calcula resultados y llena la tabla de símbolos.
        6. El backend LLVM genera código intermedio textual cuando se usa el modo `ir`.
        """
    )