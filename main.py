import streamlit as st
from streamlit.components.v1 import html

# -----------------------------------------------
# 1. Definición de Contenidos y Estructura
# -----------------------------------------------

# Los contenidos HTML completos de los archivos subidos (se usan como cadenas de texto)
# NOTA: En la implementación real, estos contenidos provienen de la herramienta,
# pero para el código final, los asignamos a variables para la demostración.

# Se asume que el contenido completo de los archivos ya fue recuperado:
HTML_CONTENT = {
    "Moderno": """
""" + f"""{HTML_FILE_1}""" + """
""",
    "Financiero": """
""" + f"""{HTML_FILE_2}""" + """
""",
    "Industrial": """
""" + f"""{HTML_FILE_3}""" + """
""",
    "Médico": """
""" + f"""{HTML_FILE_4}""" + """
""",
    "Retail": """
""" + f"""{HTML_FILE_5}""" + """
""",
    "Tecnológico": """
""" + f"""{HTML_FILE_6}""" + """
"""
}

# La lista de plantillas que se mostrarán en la galería
PLANTILLAS = [
    {"nombre": "Dashboard Moderno", "clave": "Moderno", "icono": "✨"},
    {"nombre": "Dashboard Financiero", "clave": "Financiero", "icono": "💰"},
    {"nombre": "Dashboard Industrial", "clave": "Industrial", "icono": "⚙️"},
    {"nombre": "Dashboard Médico", "clave": "Médico", "icono": "⚕️"},
    {"nombre": "Dashboard Retail/Ventas", "clave": "Retail", "icono": "🛒"},
    {"nombre": "Dashboard Tecnológico", "clave": "Tecnológico", "icono": "🤖"}
]

# -----------------------------------------------
# 2. Funciones de Navegación (Session State)
# -----------------------------------------------

# Inicializa el estado de la página si no existe
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'selected_dashboard' not in st.session_state:
    st.session_state.selected_dashboard = None

def navigate_to_home():
    """Vuelve a la página principal de la galería."""
    st.session_state.page = 'home'
    st.session_state.selected_dashboard = None

def navigate_to_dashboard(clave):
    """Navega a la vista de un dashboard específico."""
    st.session_state.page = 'dashboard_view'
    st.session_state.selected_dashboard = clave

# -----------------------------------------------
# 3. Estilos CSS (Título 3D y Botones)
# -----------------------------------------------

estilo_completo = """
<style>
/* ----------------- TÍTULO 3D ----------------- */
.titulo-3d {
    font-size: 80px;
    font-weight: bold;
    color: #00FFFF; /* CYAN Brillante (base) */
    text-shadow: 
        -4px -4px 0 #0000FF, 
        -2px -2px 0 #0000FF,
        2px 2px 0 #0000AA,
        4px 4px 0 #0000AA;
    line-height: 1.0;
}

.subtitulo-texto {
    font-size: 24px;
    color: #FFFF00; /* AMARILLO Brillante */
    margin-top: 10px; 
    margin-bottom: 30px;
    font-style: italic;
}

/* ----------------- BOTONES DE PLANTILLA (Simulación de Miniaturas) ----------------- */

/* Estilo general para el contenedor del botón */
div.stButton > button {
    width: 100%; /* Ocupa el ancho de la columna */
    height: 180px; /* Hacemos el botón grande para la miniatura */
    border: 3px solid #00FFFF;
    border-radius: 10px;
    padding: 10px;
    background-color: #1a1a1a; /* Fondo oscuro */
    color: white;
    font-size: 18px;
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(0, 255, 255, 0.2);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

/* Efecto hover */
div.stButton > button:hover {
    background-color: #000033; /* Azul oscuro al pasar el mouse */
    border-color: #FFFF00; /* Borde amarillo brillante */
    box-shadow: 0 6px 16px rgba(255, 255, 0, 0.4);
    transform: translateY(-2px);
}

/* Estilo del texto dentro del botón */
.stButton span {
    font-weight: 600;
}

/* Icono grande para la "miniatura" */
.btn-icon {
    font-size: 40px;
    margin-bottom: 10px;
}
</style>
"""

# Aplicar todos los estilos
st.set_page_config(layout="wide", page_title="Galería Cho")
st.markdown(estilo_completo, unsafe_allow_html=True)

# -----------------------------------------------
# 4. Renderizado del Contenido (Lógica de Navegación)
# -----------------------------------------------

# --- 4.1. VISTA DE DASHBOARD ESPECÍFICO ---
if st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    # Muestra un botón de regreso
    st.button("⬅️ Volver a la Galería Principal", on_click=navigate_to_home)

    # Título de la vista
    st.title(f"Vista Completa: {st.session_state.selected_dashboard}")
    st.write("---")
    
    # Renderiza el contenido HTML completo.
    # Usamos altura y ancho completos para que el dashboard se vea bien.
    dashboard_html = HTML_CONTENT[st.session_state.selected_dashboard]
    html(dashboard_html, height=1200, scrolling=True)

# --- 4.2. VISTA PRINCIPAL (HOME) ---
else:
    # Título y subtítulo 3D
    st.markdown('<div class="titulo-3d">Mirá cho!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-texto">Tenemos estas plantillas</div>', unsafe_allow_html=True)
    st.write("---")
    st.header("Selecciona una Plantilla para ver la Vista Previa")

    # Creamos 6 columnas (una por cada botón/miniatura)
    cols = st.columns(6) 
    
    # Iteramos sobre las plantillas y creamos los botones en las columnas
    for i, plantilla in enumerate(PLANTILLAS):
        with cols[i]:
            # El contenido HTML del botón (la "miniatura")
            btn_html = f"""
            <div class="btn-icon">{plantilla['icono']}</div>
            <div>{plantilla['nombre']}</div>
            """
            
            # Usamos st.markdown con el HTML del botón, y colocamos el st.button inmediatamente después
            # para capturar el clic y cambiar el estado.
            st.markdown(btn_html, unsafe_allow_html=True)
            
            # Importante: Streamlit no permite HTML dentro de st.button.
            # Por eso usamos st.markdown para el aspecto visual y un st.button transparente para la acción.
            # Aquí uso un truco de estilo más avanzado para hacer que la "columna" sea el botón.
            # La forma más simple y robusta es usar el botón normal de Streamlit, pero
            # le aplicamos el estilo CSS global que le da el tamaño y apariencia de miniatura.
            
            # Reemplazamos el st.markdown con un botón con la acción:
            if st.button(f"Ver {plantilla['clave']}", key=plantilla['clave']):
                navigate_to_dashboard(plantilla['clave'])

    # Contenido extra en la página principal
    st.write("---")
    st.info("Haz clic en cualquier botón de la galería para cargar la plantilla en tamaño completo.")
    
    st.balloons()