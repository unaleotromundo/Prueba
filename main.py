import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. Configuración Inicial y Estilos ---
st.set_page_config(layout="wide", page_title="Galería Cho")

# Mapeo de los nombres a mostrar con el nombre real del archivo
DASHBOARD_FILES = {
    "Moderno (Corporate)": {"file": "Dashboard Moderno2.html", "icon": "✨"},
    "Financiero (FinEx)": {"file": "dashboard-financial.html", "icon": "💰"},
    "Industrial (Industry X)": {"file": "dashboard-industrial.html", "icon": "⚙️"},
    "Médico (Medix)": {"file": "dashboard-medical.html", "icon": "⚕️"},
    "Retail/Ventas (Retail View)": {"file": "dashboard-retail.html", "icon": "🛒"},
    "Tecnológico (Synaptic)": {"file": "dashboard-tech.html", "icon": "🤖"},
}

# CSS para el título y las miniaturas/botones
STYLE_HTML = """
<style>
/* ----------------- TÍTULO Y BANNER ----------------- */
.titulo-3d {
    font-size: 80px;
    font-weight: bold;
    color: #00FFFF; /* CYAN Brillante (base) */
    text-shadow: 
        -4px -4px 0 #0000FF, /* Sombra para efecto 3D */
        -2px -2px 0 #0000FF,
        2px 2px 0 #0000AA,
        4px 4px 0 #0000AA;
    line-height: 1.0;
}

.subtitulo-texto {
    font-size: 24px;
    color: #FFFF00; /* AMARILLO Brillante */
    margin-top: 10px; 
    margin-bottom: 40px;
    font-style: italic;
    font-weight: 500;
}

/* ----------------- BOTONES DE PLANTILLA (Miniaturas) ----------------- */

/* Estilo para Streamlit Button */
div.stButton > button {
    width: 100%; 
    height: 160px; /* Tamaño de la miniatura */
    border: 3px solid #00FFFF;
    border-radius: 10px;
    padding: 10px;
    background-color: #1a1a1a;
    color: white;
    font-size: 18px;
    transition: all 0.2s ease;
    box-shadow: 0 4px 12px rgba(0, 255, 255, 0.2);
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center;
    text-align: center;
    white-space: normal;
    line-height: 1.3;
}

/* Ajusta el texto dentro del botón */
div.stButton > button > div > p {
    font-weight: 600;
    font-size: 18px;
    margin: 0;
    padding: 0;
}

/* Efecto hover */
div.stButton > button:hover {
    background-color: #000033;
    border-color: #FFFF00; 
    box-shadow: 0 6px 16px rgba(255, 255, 0, 0.4);
    transform: translateY(-2px);
}

/* Estilo para la vista de dashboard */
iframe[title="streamlit_component"] {
    height: 1000px !important;
    width: 100%;
    border: none;
}
</style>
"""
st.markdown(STYLE_HTML, unsafe_allow_html=True)


# --- 2. Funciones de Lógica y Estado ---

if 'page' not in st.session_state:
    st.session_state.page = 'home'
    # Solo lanza globos la primera vez que se carga la app
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
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"Error: El archivo '{filename}' no se encontró. Asegúrate de que esté en la misma carpeta que main.py.")
        return None
    except Exception as e:
        st.error(f"Error al leer el archivo '{filename}': {e}")
        return None

# --- 3. Renderizado del Contenido ---

# --- VISTA PRINCIPAL (HOME) - Muestra las Miniaturas ---
if st.session_state.page == 'home':
    # Título y subtítulo
    st.markdown('<div class="titulo-3d">Mirá cho!</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo-texto">Galería de Plantillas HTML 100% Funcionales</div>', unsafe_allow_html=True)
    
    st.header("Selecciona una Plantilla para ver la Vista Completa")

    # Crear una cuadrícula de 3 columnas para mostrar 6 miniaturas
    cols = st.columns(3) 
    
    # Iterar y crear botones en la cuadrícula
    for i, (nombre, data) in enumerate(DASHBOARD_FILES.items()):
        # El índice 'i' se usa con el módulo 3 para ciclar entre las 3 columnas
        with cols[i % 3]: 
            # El label del botón solo usa texto plano, el estilo (icono y tamaño) viene del CSS
            btn_label = f"{data['icon']} {nombre}"
            
            if st.button(btn_label, key=nombre):
                navigate_to_dashboard(nombre)

    st.write("---")
    st.info("Al hacer clic, se cargará el contenido HTML **original e inmodificado** en un iframe para garantizar su completa funcionalidad.")

# --- VISTA DE DASHBOARD ESPECÍFICO - Muestra el HTML completo ---
elif st.session_state.page == 'dashboard_view' and st.session_state.selected_dashboard:
    
    # Obtener la clave de la selección
    clave_actual = st.session_state.selected_dashboard
    archivo_html = DASHBOARD_FILES[clave_actual]['file']

    # Botón para volver a la galería
    st.button("⬅️ Volver a la Galería de Miniaturas", on_click=navigate_to_home)

    st.title(f"Vista Completa: {clave_actual}")
    st.write("---")
    
    # Cargar el contenido HTML del disco
    dashboard_html = load_html_file(archivo_html)

    if dashboard_html:
        # Renderizar el contenido HTML (100% fiel y funcional)
        components.html(
            dashboard_html,
            height=1000, 
            scrolling=True
        )