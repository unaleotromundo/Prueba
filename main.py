import streamlit as st
import streamlit.components.v1 as components
import os
import random

# --- 1. Configuración Inicial y Estilos ---
st.set_page_config(layout="wide", page_title="Galería Cósmica 🌌")

# Mapeo de los nombres a mostrar con el nombre real del archivo
DASHBOARD_FILES = {
    "01. VISIONES CÓSMICAS": {"file": "Dashboard Moderno2.html", "icon": "👁️"},
    "02. MENTALISMO ABSTRACTO": {"file": "dashboard-financial.html", "icon": "🧠"},
    "03. LABERINTOS INTERIORES": {"file": "dashboard-industrial.html", "icon": "🌀"},
    "04. PULSO GALÁCTICO": {"file": "dashboard-medical.html", "icon": "💖"},
    "05. ECOS FRACTALES": {"file": "dashboard-retail.html", "icon": "⚛️"},
    "06. SINFONÍA PSÍQUICA": {"file": "dashboard-tech.html", "icon": "🔮"},
}

# Colores Psicodélicos para la rotación de estilos
PSYCHEDELIC_COLORS = ["#FF00FF", "#00FFFF", "#FFFF00", "#FF69B4", "#9370DB", "#00FF7F"]

# --- ESTILOS PSICODÉLICOS Y ABSTRACTOS (Ajustados para Columnas) ---
STYLE_HTML = """
<style>
/* ----------------- REINICIO Y FONDO ----------------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;} 

.stApp {
    background: linear-gradient(45deg, #1A001A, #000033, #1A001A);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite; 
    font-family: 'Rubik Mono One', monospace;
    color: #E0E0E0;
    min-height: 100vh;
    padding-top: 50px; /* Espacio superior */
}

@keyframes gradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ----------------- TÍTULO CENTRAL PSICODÉLICO ----------------- */
.titulo-psicodelico {
    font-family: 'Rubik Mono One', monospace;
    font-size: 80px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 10px;
    color: #FFFFFF;
    text-transform: uppercase;
    text-shadow: 
        0 0 10px #FF00FF,
        0 0 20px #00FFFF,
        0 0 30px #FFFF00;
    animation: pulsateGlow 2s infinite alternate ease-in-out;
    margin-bottom: 5px;
    padding-top: 50px; /* Más espacio para centrar visualmente */
}

@keyframes pulsateGlow {
    0% { text-shadow: 0 0 8px #FF00FF, 0 0 16px #00FFFF, 0 0 24px #FFFF00; }
    100% { text-shadow: 0 0 15px #FF00FF, 0 0 25px #00FFFF, 0 0 40px #FFFF00; }
}

.subtitulo-psicodelico {
    font-family: 'Electrolize', sans-serif;
    font-size: 20px;
    font-weight: 400;
    color: #AAAAAA; 
    text-align: center;
    letter-spacing: 3px;
    margin-top: 10px;
    margin-bottom: 80px;
    text-transform: uppercase;
}

/* ----------------- BOTONES ABSTRACTOS (DISTRIBUCIÓN GARANTIZADA) ----------------- */

div.stButton > button {
    width: 100%; 
    height: 120px;
    padding: 10px 20px;
    background: rgba(0, 0, 0, 0.6); 
    color: #E0E0E0;
    font-family: 'Orbitron', sans-serif; 
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    border: 2px solid;
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
    transition: all 0.4s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    cursor: pointer;
    margin: 15px 0; /* Espaciado entre filas */
    
    /* FORMA ABSTRACTA ÚNICA PARA TODA LA GALERÍA */
    border-radius: 40% 60% 70% 30% / 60% 40% 60% 40%; 
    transform: rotate(2deg);
}

/* Efecto Hover Psicodélico */
div.stButton > button:hover {
    background: rgba(255, 255, 255, 0.1); 
    color: #FFFFFF;
    /* Usaremos el color del borde como un color cíclico para mantener la psicodelia */
    border-color: #FF00FF; 
    box-shadow: 0 0 25px #00FFFF, 0 0 50px #FF00FF; 
    transform: scale(1.08) rotate(-2deg); /* Efecto de giro al acercarse */
    z-index: 150; 
}

/* Ajustes para el contenido del botón */
div.stButton > button > div > p {
    font-size: 15px;
    margin: 0;
    padding: 0;
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
}

/* ----------------- VISTA DEL DASHBOARD ----------------- */
.dashboard-view-container {
    padding: 30px;
    background-color: #1A001A;
    min-height: 100vh;
}

iframe[title="streamlit_component"] {
    height: 900px !important;
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.4), 0 0 50px rgba(255, 0, 255, 0.2);
    border: 2px solid #00FFFF;
}
</style>

<link href="https://fonts.googleapis.com/css2?family=Rubik+Mono+One&family=Electrolize&family=Orbitron:wght@400;600&display=swap" rel="stylesheet">
"""
st.markdown(STYLE_HTML, unsafe_allow_html=True)


# --- 2. Funciones de Lógica y Estado ---

if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.snow()
    st.balloons() 

if 'selected_dashboard' not in st.session_state:
    st.session_state.selected_dashboard = None

def navigate_to_home():
    st.session_state.page = 'home'
    st.session_state.selected_dashboard = None
    
def navigate_to_dashboard(clave):
    st.session_state.page = 'dashboard_view'
    st.session_state.selected_dashboard = clave

def load_html_file(filename):
    try:
        filepath = os.path.join(os.getcwd(), filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"⚠️ ¡Error de Realidad\! El archivo '{filename}' no se encuentra en este plano existencial.")
        return None
    except Exception as e:
        st.error(f"❌ ¡Anomalía dimensional\! Error al leer el archivo '{filename}': {e}")
        return None

# --- 3. Renderizado del Contenido ---

# --- VISTA PRINCIPAL (HOME) - Galería de Formas Abstractas ---
if st.session_state.page == 'home':
    
    # Título y subtítulo
    st.markdown('<div class="titulo-psicodelico">EL NEXO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-psicodelico">CONEXIONES VISUALES A TRAVÉS DEL CAOS ORDENADO</div>', unsafe_allow_html=True)
    
    # Lista de botones y sus nombres
    items = list(DASHBOARD_FILES.items())
    
    # --- FILA 1: Botones exteriores (01 y 06) ---
    # Distribución: Espaciador grande (2) - Botón (3) - Espaciador medio (2) - Botón (3) - Espaciador grande (2)
    # Esto empuja los botones más hacia los lados de la pantalla, lejos del centro.
    cols1 = st.columns([2, 3, 2, 3, 2])
    
    with cols1[1]:
        nombre, data = items[0]
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_0"):
            navigate_to_dashboard(nombre)

    with cols1[3]:
        nombre, data = items[5] # El sexto botón
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_5"):
            navigate_to_dashboard(nombre)


    # --- FILA 2: Botones intermedios (02 y 05) ---
    # Distribución: Espaciador medio (1) - Botón (3.5) - Espaciador pequeño (1) - Botón (3.5) - Espaciador medio (1)
    # Esto los acerca un poco más al centro.
    cols2 = st.columns([1, 3.5, 1, 3.5, 1])
    
    with cols2[1]:
        nombre, data = items[1]
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_1"):
            navigate_to_dashboard(nombre)

    with cols2[3]:
        nombre, data = items[4] # El quinto botón
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_4"):
            navigate_to_dashboard(nombre)


    # --- FILA 3: Botones centrales (03 y 04) ---
    # Distribución: Espaciador pequeño (0.5) - Botón (4) - Espaciador mínimo (0) - Botón (4) - Espaciador pequeño (0.5)
    # Estos son los más cercanos al centro vertical, justo debajo del título.
    cols3 = st.columns([0.5, 4, 0, 4, 0.5])
    
    with cols3[1]:
        nombre, data = items[2]
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_2"):
            navigate_to_dashboard(nombre)
            
    with cols3[3]:
        nombre, data = items[3] # El cuarto botón
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_3"):
            navigate_to_dashboard(nombre)
            
    
    # Pie de página sutil
    st.markdown("""
        <div style="text-align: center; color: #555555; font-size: 12px; z-index: 10; margin-top: 100px;">
            <p>👁️ EXPLORA EL MULTIVERSO VISUAL 👁️</p>
        </div>
    """, unsafe_allow_html=True)


# --- VISTA DE DASHBOARD ESPECÍFICO - Muestra el HTML completo ---
elif st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    clave_actual = st.session_state.selected_dashboard
    archivo_html = DASHBOARD_FILES[clave_actual]['file']
    
    st.markdown('<div class="dashboard-view-container">', unsafe_allow_html=True)

    # Botón de regreso
    st.button("⬅️ REGRESAR AL NEXO", on_click=navigate_to_home, help="Vuelve a la galería de abstracciones.")

    st.markdown(f"<h2 style='color: #00FFFF; font-family: Orbitron, sans-serif; text-shadow: 0 0 5px #00FFFF;'>PROYECCIÓN ACTIVA: {clave_actual}</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid #FF00FF;'>", unsafe_allow_html=True)
    
    dashboard_html = load_html_file(archivo_html)

    if dashboard_html:
        components.html(
            dashboard_html,
            height=900, 
            scrolling=True
        )
    st.markdown('</div>', unsafe_allow_html=True)