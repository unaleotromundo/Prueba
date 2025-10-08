import streamlit as st
import streamlit.components.v1 as components
import pathlib

# --- 1. Configuración Inicial y Estilos ---
BASE_DIR = pathlib.Path(__file__).parent.resolve()

st.set_page_config(
    layout="wide",
    page_title="Galería Minimalista 🌐",
    page_icon="🌐"
)

# Mapeo original (se filtrará luego)
DASHBOARD_FILES_RAW = {
    "01. Corporate (Inter)": {"file": "Dashboard Moderno2.html", "icon": "💎"},
    "02. Financial (Plex)": {"file": "dashboard-financial.html", "icon": "📈"},
    "03. Industrial (Rajdhani)": {"file": "dashboard-industrial.html", "icon": "🏭"},
    "04. Medical (Roboto)": {"file": "dashboard-medical.html", "icon": "🩺"},
    "05. Retail/Sales (Outfit)": {"file": "dashboard-retail.html", "icon": "🛍️"},
    "06. Tech/Vibrant (Poppins)": {"file": "dashboard-tech.html", "icon": "🧠"},
}

# Filtrar solo los dashboards cuyos archivos existen
DASHBOARD_FILES = {
    name: data for name, data in DASHBOARD_FILES_RAW.items()
    if (BASE_DIR / data["file"]).exists()
}

# CSS para el estilo Dark, Minimalista y COMPACTO
STYLE_HTML = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;500&display=swap" rel="stylesheet">
<style>
/* ----------------- REINICIO Y FONDO ----------------- */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;} 

.stApp {
    background-color: #0A0A0A; 
    font-family: 'Inter', sans-serif;
}

/* ----------------- TÍTULO Y BANNER ----------------- */
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

/* ----------------- BOTONES COMPACTOS ----------------- */
div.stButton > button {
    width: 100%; 
    height: 80px; 
    border: 1px solid #222222; 
    border-radius: 4px; 
    padding: 15px 25px;
    background-color: #1A1A1A; 
    color: #BDBDBD; 
    font-family: 'Inter', sans-serif;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
    display: flex;
    flex-direction: row; 
    justify-content: flex-start;
    align-items: center;
    text-align: left;
    white-space: nowrap;
}

div.stButton > button > div > p {
    font-weight: 500;
    font-size: 15px; 
    margin: 0;
    padding-left: 15px;
    color: #FFFFFF; 
    text-transform: uppercase;
    letter-spacing: 1px;
}

div.stButton > button:hover {
    background-color: #0F0F0F; 
    border-color: #00C8FF; 
    color: #00C8FF;
    box-shadow: 0 0 15px rgba(0, 200, 255, 0.6); 
    transform: scale(1.02); 
}

/* Estilo del iframe */
iframe[title="streamlit_component"] {
    width: 100%;
    border-radius: 4px;
    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.7);
    border: 1px solid #222222;
}
</style>
"""
st.markdown(STYLE_HTML, unsafe_allow_html=True)


# --- 2. Funciones de Lógica y Estado ---
if 'page' not in st.session_state:
    st.session_state.page = 'home'
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
        filepath = BASE_DIR / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"⚠️ Error: El archivo '{filename}' no se encontró.")
        return None
    except Exception as e:
        st.error(f"❌ Error al leer '{filename}': {e}")
        return None


# --- 3. Renderizado del Contenido ---

# --- VISTA PRINCIPAL (HOME) ---
if st.session_state.page == 'home':
    st.markdown('<div class="titulo-minimal">Mirá Cho!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-minimal">Directorio de Temas | Estilo Consola Minimalista</div>', unsafe_allow_html=True)
    
    st.subheader("Selecciona un tema para cargar su vista completa")
    st.markdown("---")

    if not DASHBOARD_FILES:
        st.warning("⚠️ No se encontraron archivos de dashboard en la carpeta.")
    else:
        cols = st.columns(3)
        for i, (nombre, data) in enumerate(DASHBOARD_FILES.items()):
            with cols[i % 3]:
                btn_label = f"{data['icon']} {nombre}"
                if st.button(btn_label, key=nombre):
                    navigate_to_dashboard(nombre)

    st.write("")
    st.markdown("---")
    st.markdown(
        '<p style="text-align: center; color: #555555; font-size: 14px; margin-top: 20px;">'
        'Cada vista se carga directamente desde el archivo HTML original, garantizando la integridad funcional.</p>',
        unsafe_allow_html=True
    )


# --- VISTA DE DASHBOARD ESPECÍFICO ---
elif st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    clave_actual = st.session_state.selected_dashboard
    archivo_html = DASHBOARD_FILES[clave_actual]['file']
    
    col_back, col_title = st.columns([1, 4])
    with col_back:
        st.button("← Volver a la galería", on_click=navigate_to_home)
    with col_title:
        st.header(f"Vista Activa: {clave_actual}")

    st.markdown("---")
    
    # Slider para ajustar altura (guardado en session_state para persistencia)
    if 'dashboard_height' not in st.session_state:
        st.session_state.dashboard_height = 1000

    altura = st.slider(
        "Ajustar altura del dashboard (px)",
        min_value=600,
        max_value=1500,
        value=st.session_state.dashboard_height,
        step=50,
        key="dashboard_height_slider"
    )
    # Guardar en session_state para que persista al interactuar
    st.session_state.dashboard_height = altura

    # Cargar con spinner
    with st.spinner("Cargando dashboard..."):
        dashboard_html = load_html_file(archivo_html)

    if dashboard_html:
        components.html(
            dashboard_html,
            height=st.session_state.dashboard_height,
            scrolling=True
        )