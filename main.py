import streamlit as st
import streamlit.components.v1 as components
import os

# --- Configuración Inicial ---
st.set_page_config(layout="wide")

# Mapeo de los nombres a mostrar con el nombre real del archivo
DASHBOARD_FILES = {
    "Moderno": "Dashboard Moderno2.html",
    "Financiero": "dashboard-financial.html",
    "Industrial": "dashboard-industrial.html",
    "Médico": "dashboard-medical.html",
    "Retail": "dashboard-retail.html",
    "Tecnológico": "dashboard-tech.html",
}

def load_html_file(filename):
    """
    Función para cargar el contenido de un archivo HTML.
    Se espera que el archivo esté en la misma carpeta que este script.
    """
    try:
        # 'r' para modo lectura, 'encoding' para manejar correctamente caracteres especiales
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"Error: El archivo '{filename}' no se encontró. Asegúrate de que esté en la misma carpeta que main.py.")
        return None
    except Exception as e:
        st.error(f"Error al leer el archivo '{filename}': {e}")
        return None

# --- Interfaz de la Aplicación Streamlit ---

st.sidebar.title("Selector de Dashboards 📊")
st.sidebar.markdown("---")

# Selección del dashboard
selected_dashboard_name = st.sidebar.selectbox(
    "Elige un Dashboard:",
    list(DASHBOARD_FILES.keys())
)

st.title(f"Visualización: {selected_dashboard_name}")
st.markdown("---")

# Obtener el nombre de archivo correspondiente
selected_filename = DASHBOARD_FILES[selected_dashboard_name]

# Cargar el contenido del HTML
html_content = load_html_file(selected_filename)

if html_content:
    # Injectar CSS para asegurar que el componente HTML ocupe el espacio adecuado
    st.markdown("""
        <style>
            /* Ajusta el padding superior e inferior del Streamlit App */
            .stApp {
                padding-top: 0px;
                padding-bottom: 0px;
            }
            /* Ajusta el iframe para que tenga una altura más adaptable al contenido */
            iframe[title="streamlit_component"] {
                height: 1000px !important; /* Altura inicial fija para mejor visualización */
                width: 100%;
                border: none;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Renderizar el HTML
    components.html(
        html_content, 
        height=1000, # Altura de reserva
        scrolling=True # Permitir scroll si el contenido es más largo
    )