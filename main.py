import streamlit as st

# -----------------------------------------------
# 1. Configuración de la Página y el Título 3D
# -----------------------------------------------

# Configuración básica de la página
st.set_page_config(
    page_title="Mi Sitio Streamlit",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo CSS para el título (incluye el efecto 3D/sombra y los colores)
estilo_titulo = """
<style>
/* Estilo del Título Principal */
.titulo-3d {
    font-size: 80px;
    font-weight: bold;
    color: #00FFFF; /* CYAN Brillante (base) */
    text-shadow: 
        -4px -4px 0 #0000FF, /* Sombra ligera (simula luz) */
        -2px -2px 0 #0000FF,
        2px 2px 0 #0000AA,  /* Sombra más oscura (efecto profundidad) */
        4px 4px 0 #0000AA;
    line-height: 1.0; /* Asegura un espaciado compacto */
}

/* Estilo del Subtítulo */
.subtitulo-texto {
    font-size: 24px;
    color: #FFFF00; /* AMARILLO Brillante */
    margin-top: 10px; /* Separación del título */
    margin-bottom: 30px;
    font-style: italic;
}
</style>
"""

# Aplicar el estilo CSS a la página
st.markdown(estilo_titulo, unsafe_allow_html=True)

# Imprimir el título y el subtítulo con las clases CSS definidas
st.markdown('<div class="titulo-3d">Mirá cho!</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo-texto">Tenemos estas plantillas</div>', unsafe_allow_html=True)

# -----------------------------------------------
# 2. Contenido Principal del Sitio
# -----------------------------------------------

st.write("---")
st.header("💻 ¡Tu Sitio Web en un solo archivo Python!")

st.markdown("""
Este es el cuerpo principal de tu aplicación web, definido completamente en `app.py`.
Streamlit convierte este código de Python en una página web interactiva.
""")

st.subheader("Menú y Plantillas")

# Ejemplo de estructura simple de un sitio
opcion = st.sidebar.radio(
    "Selecciona una Plantilla:",
    ('Inicio', 'Plantilla Moderna', 'Plantilla Clásica')
)

if opcion == 'Inicio':
    st.info("¡Bienvenido! Explora las opciones en la barra lateral.")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-dark.svg", width=200)

elif opcion == 'Plantilla Moderna':
    st.success("Cargada: Plantilla de Diseño Moderno")
    st.metric(label="Elementos", value="56", delta="Nuevo")

elif opcion == 'Plantilla Clásica':
    st.warning("Cargada: Plantilla Clásica de Negocios")
    st.slider("Configuración", 0, 100, 50)


# Sección de pie de página
st.write("---")
st.caption("Hecho con ❤️ y Streamlit.")

# Lanzar confeti al cargar
st.balloons()