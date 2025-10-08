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

# --- ESTILOS PSICODÉLICOS Y ABSTRACTOS ---
STYLE_HTML = """
<style>
/* ----------------- REINICIO Y FONDO ----------------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;} 

.stApp {
    background: linear-gradient(45deg, #1A001A, #000033, #1A001A); /* Fondo oscuro con degradado profundo */
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite; /* Animación de fondo */
    font-family: 'Rubik Mono One', monospace; /* Fuente impactante */
    color: #E0E0E0;
    overflow: hidden; /* Para evitar scroll inesperado con elementos absolutos */
}

@keyframes gradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Contenedor principal para posicionar elementos */
.main-content-area {
    position: relative;
    width: 100vw;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    overflow: hidden;
}

/* ----------------- TÍTULO CENTRAL PSICODÉLICO ----------------- */
.titulo-psicodelico {
    font-family: 'Rubik Mono One', monospace;
    font-size: 90px;
    font-weight: 900;
    text-align: center;
    letter-spacing: 10px;
    color: #FFFFFF;
    text-transform: uppercase;
    text-shadow: 
        0 0 10px #FF00FF, /* Magenta */
        0 0 20px #00FFFF, /* Cyan */
        0 0 30px #FFFF00; /* Amarillo */
    animation: pulsateGlow 2s infinite alternate ease-in-out; /* Animación de resplandor */
    margin-bottom: 0px;
    z-index: 100; /* Asegurarse de que esté por encima de los botones */
    position: relative; /* Para que el z-index funcione bien */
    user-select: none; /* No seleccionable */
}

@keyframes pulsateGlow {
    0% { text-shadow: 0 0 8px #FF00FF, 0 0 16px #00FFFF, 0 0 24px #FFFF00; }
    100% { text-shadow: 0 0 15px #FF00FF, 0 0 25px #00FFFF, 0 0 40px #FFFF00; }
}

.subtitulo-psicodelico {
    font-family: 'Electrolize', sans-serif; /* Otra fuente más técnica */
    font-size: 20px;
    font-weight: 400;
    color: #AAAAAA; 
    text-align: center;
    letter-spacing: 3px;
    margin-top: 10px;
    margin-bottom: 80px; /* Más espacio para los botones */
    text-transform: uppercase;
    z-index: 100;
    position: relative;
    user-select: none;
}

/* ----------------- BOTONES ABSTRACTOS ALREDEDOR DEL TÍTULO ----------------- */

div.stButton > button {
    position: absolute; /* Posicionamiento libre */
    width: 250px; 
    height: 90px;
    padding: 10px 20px;
    background: rgba(0, 0, 0, 0.6); /* Fondo semi-transparente */
    color: #E0E0E0;
    font-family: 'Orbitron', sans-serif; /* Fuente futurista para botones */
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    border: 2px solid; /* Borde para el resplandor */
    box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
    transition: all 0.4s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    z-index: 50; /* Por debajo del título */
    cursor: pointer;
    overflow: hidden; /* Para ocultar cualquier cosa que se desborde al animar */
}

/* Formas Abstractas (modificando border-radius y transform) */
.btn-shape-1 { 
    border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; 
    top: 15%; left: 10%; transform: rotate(-15deg) scale(1);
    border-color: #FF00FF; /* Magenta */
    box-shadow: 0 0 10px #FF00FF;
}
.btn-shape-2 { 
    border-radius: 30% 70% 60% 40% / 70% 40% 60% 30%; 
    top: 25%; right: 10%; transform: rotate(10deg) scale(1);
    border-color: #00FFFF; /* Cyan */
    box-shadow: 0 0 10px #00FFFF;
}
.btn-shape-3 { 
    border-radius: 70% 30% 70% 30% / 30% 70% 30% 70%; 
    bottom: 25%; left: 8%; transform: rotate(20deg) scale(1);
    border-color: #FFFF00; /* Amarillo */
    box-shadow: 0 0 10px #FFFF00;
}
.btn-shape-4 { 
    border-radius: 40% 60% 70% 30% / 60% 70% 30% 40%; 
    bottom: 15%; right: 12%; transform: rotate(-8deg) scale(1);
    border-color: #FF69B4; /* Rosa */
    box-shadow: 0 0 10px #FF69B4;
}
.btn-shape-5 { 
    border-radius: 50% 50% 50% 50% / 50% 50% 50% 50%; /* Círculo/Óvalo */
    top: 50%; left: 5%; transform: translateY(-50%) rotate(-5deg) scale(1);
    border-color: #9370DB; /* Púrpura */
    box-shadow: 0 0 10px #9370DB;
}
.btn-shape-6 { 
    border-radius: 45% 55% 55% 45% / 55% 45% 55% 45%; /* Óvalo */
    top: 50%; right: 5%; transform: translateY(-50%) rotate(5deg) scale(1);
    border-color: #00FF7F; /* Verde Primavera */
    box-shadow: 0 0 10px #00FF7F;
}

/* Efecto Hover Psicodélico */
div.stButton > button:hover {
    background: rgba(255, 255, 255, 0.1); /* Fondo más claro al pasar */
    color: #FFFFFF;
    box-shadow: 0 0 25px var(--hover-color), 0 0 50px var(--hover-color); /* Resplandor intenso */
    transform: scale(1.05) rotate(var(--hover-rotate, 0deg)); /* Un poco de rotación aleatoria */
    z-index: 150; /* Lo trae al frente */
    animation: swirlHover 0.8s forwards; /* Animación de remolino */
}

/* Variables para los colores de hover dinámicos */
.btn-shape-1:hover { --hover-color: #FF00FF; --hover-rotate: -20deg; }
.btn-shape-2:hover { --hover-color: #00FFFF; --hover-rotate: 15deg; }
.btn-shape-3:hover { --hover-color: #FFFF00; --hover-rotate: 25deg; }
.btn-shape-4:hover { --hover-color: #FF69B4; --hover-rotate: -12deg; }
.btn-shape-5:hover { --hover-color: #9370DB; --hover-rotate: -10deg; }
.btn-shape-6:hover { --hover-color: #00FF7F; --hover-rotate: 8deg; }

@keyframes swirlHover {
    0% { transform: scale(1.02) rotate(var(--original-rotate, 0deg)); }
    50% { transform: scale(1.08) rotate(var(--hover-rotate)); }
    100% { transform: scale(1.05) rotate(var(--hover-rotate)); }
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
    background-color: #1A001A; /* Un fondo oscuro para la vista del dashboard */
    min-height: 100vh;
}

iframe[title="streamlit_component"] {
    height: 900px !important; /* Altura generosa para el dashboard */
    width: 100%;
    border-radius: 8px;
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.4), 0 0 50px rgba(255, 0, 255, 0.2); /* Sombra vibrante */
    border: 2px solid #00FFFF; /* Borde cian */
}
</style>

<link href="https://fonts.googleapis.com/css2?family=Rubik+Mono+One&family=Electrolize&family=Orbitron:wght@400;600&display=swap" rel="stylesheet">
"""
st.markdown(STYLE_HTML, unsafe_allow_html=True)


# --- 2. Funciones de Lógica y Estado ---

# Inicialización de estado y confeti (¡ahora es confeti!)
if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.snow() # Nieve o confeti para un efecto más psicodélico
    st.balloons() # También globos para ese efecto

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

def load_html_file(filename):
    """Carga el contenido de un archivo HTML de la misma carpeta."""
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
    # Contenedor para los elementos posicionados absolutamente
    st.markdown('<div class="main-content-area">', unsafe_allow_html=True)
    
    # Título y subtítulo
    st.markdown('<div class="titulo-psicodelico">EL NEXO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-psicodelico">CONEXIONES VISUALES A TRAVÉS DEL CAOS ORDENADO</div>', unsafe_allow_html=True)
    
    # Asignar clases de estilo a cada botón para las formas y posiciones
    button_styles = [
        "btn-shape-1", "btn-shape-2", "btn-shape-3", 
        "btn-shape-4", "btn-shape-5", "btn-shape-6"
    ]
    
    # Crear los botones con posicionamiento absoluto
    for i, (nombre, data) in enumerate(DASHBOARD_FILES.items()):
        # Se genera un ID único para cada botón para el CSS
        st.markdown(f'<div class="{button_styles[i]}" id="button_{i}">', unsafe_allow_html=True)
        # El st.button real, con un key único
        if st.button(f"{data['icon']} {nombre}", key=f"dash_btn_{i}"):
            navigate_to_dashboard(nombre)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Cierra main-content-area
    
    # Pie de página sutil
    st.markdown("""
        <div style="position: fixed; bottom: 20px; width: 100%; text-align: center; color: #555555; font-size: 12px; z-index: 10;">
            <p>👁️ EXPLORA EL MULTIVERSO VISUAL 👁️</p>
        </div>
    """, unsafe_allow_html=True)


# --- VISTA DE DASHBOARD ESPECÍFICO - Muestra el HTML completo ---
elif st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    clave_actual = st.session_state.selected_dashboard
    archivo_html = DASHBOARD_FILES[clave_actual]['file']
    
    # Contenedor para la vista del dashboard para un fondo consistente
    st.markdown('<div class="dashboard-view-container">', unsafe_allow_html=True)

    # Botón de regreso con un estilo más alineado
    st.button("⬅️ REGRESAR AL NEXO", on_click=navigate_to_home, help="Vuelve a la galería de abstracciones.")

    st.markdown(f"<h2 style='color: #00FFFF; font-family: Orbitron, sans-serif; text-shadow: 0 0 5px #00FFFF;'>PROYECCIÓN ACTIVA: {clave_actual}</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-top: 2px solid #FF00FF;'>", unsafe_allow_html=True) # Separador psicodélico
    
    # Cargar el contenido HTML del disco
    dashboard_html = load_html_file(archivo_html)

    if dashboard_html:
        # Renderizar el contenido HTML
        components.html(
            dashboard_html,
            height=900, 
            scrolling=True
        )
    st.markdown('</div>', unsafe_allow_html=True) # Cierra dashboard-view-container