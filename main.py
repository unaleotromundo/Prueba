import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. Configuración Inicial y Estilos ---
st.set_page_config(layout="wide", page_title="Galería Minimalista 🌐")

# Mapeo de los nombres a mostrar con el nombre real del archivo
DASHBOARD_FILES = {
    "01. Corporate (Inter)": {"file": "Dashboard Moderno2.html", "icon": "💎"},
    "02. Financial (Plex)": {"file": "dashboard-financial.html", "icon": "📈"},
    "03. Industrial (Rajdhani)": {"file": "dashboard-industrial.html", "icon": "🏭"},
    "04. Medical (Roboto)": {"file": "dashboard-medical.html", "icon": "🩺"},
    "05. Retail/Sales (Outfit)": {"file": "dashboard-retail.html", "icon": "🛍️"},
    "06. Tech/Vibrant (Poppins)": {"file": "dashboard-tech.html", "icon": "🧠"},
}

# CSS para el estilo Dark, Minimalista y ahora COMPACTO
STYLE_HTML = """
<style>
/* ----------------- REINICIO Y FONDO ----------------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;} 

.stApp {
    background-color: #0A0A0A; 
    font-family: 'Inter', sans-serif;
}

/* ----------------- TÍTULO Y BANNER (Efecto Thin-Glow) ----------------- */
.titulo-minimal {
    font-family: 'Inter', sans-serif;
    font-size: 72px;
    font-weight: 200; 
    text-align: center;
    letter-spacing: 5px;
    color: #FFFFFF;
    text-transform: uppercase;
    text-shadow: 
        0 0 5px rgba(0, 200, 255, 0.5), 
        0 0 10px rgba(0, 200, 255, 0.2);
    margin-bottom: 5px;
    border-bottom: 1px solid rgba(0, 200, 255, 0.2); 
    padding-bottom: 10px;
}

.subtitulo-minimal {
    font-size: 16px;
    font-weight: 300;
    color: #888888; 
    text-align: center;
    letter-spacing: 2px;
    margin-bottom: 60px;
    text-transform: uppercase;
}

/* ----------------- SECCIÓN DE BOTONES (Compactos) ----------------- */

/* Estilo para Streamlit Button (El Ítem de la Lista) */
div.stButton > button {
    width: 100%; 
    height: 80px; /* ALTURA REDUCIDA A LA MITAD */ 
    border: 1px solid #222222; 
    border-radius: 4px; 
    padding: 15px 25px; /* Más espacio horizontal que vertical */
    background-color: #1A1A1A; 
    color: #BDBDBD; 
    font-family: 'Inter', sans-serif;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
    
    /* Alineación Horizontal (Icono y Texto en la misma línea) */
    display: flex;
    flex-direction: row; 
    justify-content: flex-start; /* Alinear el contenido a la izquierda */
    align-items: center;
    text-align: left;
    white-space: nowrap; /* Evitar que el texto se rompa */
}

/* Ajusta el texto dentro del botón */
div.stButton > button > div > p {
    font-weight: 500;
    font-size: 15px; 
    margin: 0;
    padding-left: 15px; /* Separación entre el icono y el texto */
    color: #FFFFFF; 
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Efecto hover DRAMÁTICO y Minimalista */
div.stButton > button:hover {
    background-color: #0F0F0F; 
    border-color: #00C8FF; 
    color: #00C8FF;
    box-shadow: 0 0 15px rgba(0, 200, 255, 0.6); 
    transform: scale(1.02); 
}

/* Estilo del iframe de visualización (Dashboard View) */
iframe[title="streamlit_component"] {
    height: 1000px !important;
    width: 100%;
    border-radius: 4px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.7);
    border: 1px solid #222222;
}
</style>
"""
st.markdown(STYLE_HTML, unsafe_allow_html=True)


# --- 2. Funciones de Lógica y Estado ---

# Inicialización de estado y globos
if 'page' not in st.session_state:
    st.session_state.page = 'home'
    st.balloons() # Globos al inicio

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
        st.error(f"⚠️ Error: El archivo '{filename}' no se encontró. Asegúrate de que esté en la misma carpeta que main.py.")
        return None
    except Exception as e:
        st.error(f"❌ Error al leer el archivo '{filename}': {e}")
        return None

# --- 3. Renderizado del Contenido ---

# --- VISTA PRINCIPAL (HOME) - Muestra los Botones Compactos ---
if st.session_state.page == 'home':
    # Título y subtítulo
    st.markdown('<div class="titulo-minimal">Mirá Cho!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-minimal">Directorio de Temas | Estilo Consola Minimalista</div>', unsafe_allow_html=True)
    st.subheader("Selecciona con dos clic un Tema para Cargar la Vista Completa")
    st.markdown("---")

    # Usamos 3 columnas, pero las tarjetas son más pequeñas.
    cols = st.columns(3) 
    
    # Iterar y crear botones en la cuadrícula
    for i, (nombre, data) in enumerate(DASHBOARD_FILES.items()):
        with cols[i % 3]: 
            btn_label = f"{data['icon']} {nombre}"
            
            if st.button(btn_label, key=nombre):
                navigate_to_dashboard(nombre)

    st.write("")
    st.markdown("---")
    st.markdown('<p style="text-align: center; color: #555555; font-size: 14px; margin-top: 20px;">Cada vista se carga directamente desde el archivo HTML original, garantizando la integridad funcional.</p>', unsafe_allow_html=True)


# --- VISTA DE DASHBOARD ESPECÍFICO - Muestra el HTML completo ---
elif st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    clave_actual = st.session_state.selected_dashboard
    archivo_html = DASHBOARD_FILES[clave_actual]['file']
    
    # Botón de regreso
    col_back, col_title = st.columns([1, 4])
    
    with col_back:
        st.button("⬅️ VOLVER AL DIRECTORIO", on_click=navigate_to_home)

    with col_title:
        st.header(f"Vista Activa: {clave_actual}")

    st.markdown("---")
    
    # Cargar el contenido HTML del disco
    dashboard_html = load_html_file(archivo_html)

    if dashboard_html:
        # Renderizar el contenido HTML
        components.html(
            dashboard_html,
            height=1000, 
            scrolling=True
        )