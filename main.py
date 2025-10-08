import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. Configuración Inicial y Estilos ---
st.set_page_config(layout="wide", page_title="Galería de Dashboards 🚀")

# Mapeo de los nombres a mostrar con el nombre real del archivo
DASHBOARD_FILES = {
    "Moderno (Corporate)": {"file": "Dashboard Moderno2.html", "icon": "✨"},
    "Financiero (FinEx)": {"file": "dashboard-financial.html", "icon": "💰"},
    "Industrial (Industry X)": {"file": "dashboard-industrial.html", "icon": "⚙️"},
    "Médico (Medix)": {"file": "dashboard-medical.html", "icon": "⚕️"},
    "Retail/Ventas (Retail View)": {"file": "dashboard-retail.html", "icon": "🛒"},
    "Tecnológico (Synaptic)": {"file": "dashboard-tech.html", "icon": "🤖"},
}

# CSS para un aspecto más limpio y profesional
STYLE_HTML = """
<style>
/* Oculta los elementos por defecto de Streamlit (ej. la etiqueta "Made with Streamlit") */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;} 

/* ----------------- TÍTULO Y BANNER (Efecto Retro-Moderno) ----------------- */
.titulo-3d {
    font-family: 'Poppins', sans-serif;
    font-size: 80px;
    font-weight: 800;
    text-align: center;
    letter-spacing: -2px;
    background: linear-gradient(90deg, #6366f1, #ec4899); /* Degradado vibrante */
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 4px 10px rgba(99, 102, 241, 0.4); /* Sombra suave */
    margin-bottom: 5px;
}

.subtitulo-texto {
    font-size: 20px;
    font-weight: 400;
    color: #a0a3bd; /* Gris suave */
    text-align: center;
    margin-bottom: 40px;
}

/* ----------------- SECCIÓN DE BOTONES (Miniaturas/Galería) ----------------- */
.stContainer {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Estilo para Streamlit Button */
div.stButton > button {
    width: 100%; 
    height: 180px; /* Tamaño de la miniatura */
    border: 1px solid #333333;
    border-radius: 12px;
    padding: 20px;
    background-color: #1a1a1a; /* Fondo oscuro sutil */
    color: white;
    font-family: 'Poppins', sans-serif;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center;
    text-align: center;
    white-space: normal;
    line-height: 1.4;
}

/* Ajusta el texto dentro del botón */
div.stButton > button > div > p {
    font-weight: 600;
    font-size: 17px;
    margin: 5px 0 0 0; /* Espacio después del icono */
    padding: 0;
}

/* Efecto hover profesional */
div.stButton > button:hover {
    background-color: #262626;
    border-color: #6366f1; /* Resaltado con el color primario */
    box-shadow: 0 8px 25px rgba(99, 102, 241, 0.3); /* Efecto de brillo */
    transform: translateY(-5px); /* Pequeño levantamiento */
}

/* Estilo del iframe de visualización */
iframe[title="streamlit_component"] {
    height: 1000px !important;
    width: 100%;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    border: 1px solid #333333;
}
</style>
"""
st.markdown(STYLE_HTML, unsafe_allow_html=True)


# --- 2. Funciones de Lógica y Estado ---

if 'page' not in st.session_state:
    st.session_state.page = 'home'
    # Lanza globos solo la primera vez que se carga la app para el efecto inicial
    st.balloons() 

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
        # Asegurarse de que el script puede acceder a la ruta
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

# --- VISTA PRINCIPAL (HOME) - Muestra las Miniaturas ---
if st.session_state.page == 'home':
    # Título y subtítulo
    st.markdown('<div class="titulo-3d">Galería de Dashboards</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-texto">Plantillas HTML 100% funcionales para Streamlit (Cho)</div>', unsafe_allow_html=True)
    
    st.subheader("Selecciona una Plantilla para ver la Vista Completa")
    st.markdown("---")

    # Crear una cuadrícula de 3 columnas para mostrar 6 miniaturas
    cols = st.columns(3) 
    
    # Iterar y crear botones en la cuadrícula
    for i, (nombre, data) in enumerate(DASHBOARD_FILES.items()):
        # El índice 'i' se usa con el módulo 3 para ciclar entre las 3 columnas
        with cols[i % 3]: 
            # El label del botón solo usa texto plano para evitar el error de Streamlit
            btn_label = f"{data['icon']} {nombre}"
            
            if st.button(btn_label, key=nombre):
                navigate_to_dashboard(nombre)

    st.write("")
    st.info("💡 **Garantía:** El contenido HTML se carga **sin modificar** dentro de un `<iframe>`, preservando su funcionalidad y diseño original.")

# --- VISTA DE DASHBOARD ESPECÍFICO - Muestra el HTML completo ---
elif st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    clave_actual = st.session_state.selected_dashboard
    archivo_html = DASHBOARD_FILES[clave_actual]['file']
    
    # Columna para el botón de regreso, alineado a la izquierda
    col_back, col_title = st.columns([1, 4])
    
    with col_back:
        st.button("⬅️ Volver a la Galería", on_click=navigate_to_home)

    with col_title:
        st.header(f"Visualización: {clave_actual}")

    st.markdown("---")
    
    # Cargar el contenido HTML del disco
    dashboard_html = load_html_file(archivo_html)

    if dashboard_html:
        # Renderizar el contenido HTML (100% fiel y funcional)
        components.html(
            dashboard_html,
            height=1000, 
            scrolling=True
        )