import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Feria Online",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos con partículas (igual que en tu ejemplo)
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"],
    [data-testid="stHeader"],
    .main {
        background-color: black !important;
        color: white !important;
    }

    #particles-js {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }

    .particle {
        position: absolute;
        width: 20px;
        height: 20px;
        background: white;
        border-radius: 50%;
        box-shadow: 0 0 15px 5px cyan;
        animation: floatUp 10s infinite ease-in;
    }

    @keyframes floatUp {
        0% { transform: translateY(100vh) translateX(0); opacity: 0; }
        10% { opacity: 1; }
        90% { opacity: 1; }
        100% { transform: translateY(-100px) translateX(50px); opacity: 0; }
    }

    .section {
        background: rgba(0, 0, 0, 0.7);
        padding: 25px;
        border-radius: 15px;
        margin: 20px 0;
        border: 1px solid #0ff;
        box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
        position: relative;
        z-index: 10;
    }

    h1, h2, h3 {
        color: white;
        text-shadow: 0 0 8px cyan;
    }

    .stButton > button {
        background: #0ff;
        color: black;
        border: none;
        font-weight: bold;
        border-radius: 5px;
    }

    input, textarea {
        background: #111 !important;
        color: white !important;
        border: 1px solid #0ff !important;
    }
    </style>

    <div id="particles-js">
        <div class="particle" style="left: 5%; animation-delay: 0s;"></div>
        <div class="particle" style="left: 25%; animation-delay: 2s; width: 25px; height: 25px; box-shadow: 0 0 20px 8px #ff00ff;"></div>
        <div class="particle" style="left: 45%; animation-delay: 4s; width: 18px; height: 18px; box-shadow: 0 0 18px 6px #ff9900;"></div>
        <div class="particle" style="left: 65%; animation-delay: 1s; width: 22px; height: 22px; box-shadow: 0 0 22px 7px #00ff99;"></div>
        <div class="particle" style="left: 85%; animation-delay: 3s; width: 30px; height: 30px; box-shadow: 0 0 25px 10px white;"></div>
    </div>
""", unsafe_allow_html=True)

# Estado de la app (simulando "base de datos" en memoria)
if 'productos' not in st.session_state:
    st.session_state.productos = []
if 'comerciante' not in st.session_state:
    st.session_state.comerciante = None

# Barra lateral para navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio("Ir a:", [
    "Inicio",
    "Registro de Comerciante",
    "Acceso Comerciantes",
    "Mi Perfil",
    "Gestión de mi Puesto"
])

# ===== PÁGINA: Inicio =====
if pagina == "Inicio":
    st.markdown('<div class="section"><h1>Conecta tu pequeño negocio con el mundo</h1></div>', unsafe_allow_html=True)
    st.markdown('<p style="color:white; text-align:center;">Una feria virtual donde los comerciantes pueden mostrar sus productos y los clientes pueden descubrir tesoros locales</p>', unsafe_allow_html=True)

    st.markdown('<div class="section"><h2>Productos Destacados</h2>', unsafe_allow_html=True)
    if st.session_state.productos:
        for p in st.session_state.productos[:4]:
            st.markdown(f"<p>• {p}</p>", unsafe_allow_html=True)
    else:
        st.write("No hay productos destacados aún.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== PÁGINA: Registro =====
elif pagina == "Registro de Comerciante":
    st.markdown('<div class="section"><h2>Registro de Comerciante</h2><h3>Crea tu cuenta de comerciante</h3>', unsafe_allow_html=True)
    nombre = st.text_input("Nombre completo")
    email = st.text_input("Correo electrónico")
    if st.button("Registrarse"):
        if nombre and email:
            st.session_state.comerciante = {"nombre": nombre, "email": email}
            st.success("¡Registro exitoso! Ahora puedes acceder desde 'Acceso Comerciantes'.")
        else:
            st.error("Por favor, completa todos los campos.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== PÁGINA: Acceso =====
elif pagina == "Acceso Comerciantes":
    st.markdown('<div class="section"><h2>Acceso Comerciantes</h2><p>Ingresa para gestionar tu puesto</p>', unsafe_allow_html=True)
    email = st.text_input("Tu correo electrónico")
    if st.button("Ingresar"):
        if st.session_state.comerciante and st.session_state.comerciante["email"] == email:
            st.success("Acceso concedido.")
        else:
            st.error("Comerciante no registrado.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== PÁGINA: Mi Perfil =====
elif pagina == "Mi Perfil":
    st.markdown('<div class="section"><h2>Mi Perfil</h2>', unsafe_allow_html=True)
    if st.session_state.comerciante:
        c = st.session_state.comerciante
        st.markdown(f"<p><strong>{c['nombre']}</strong></p>", unsafe_allow_html=True)
        st.write(c["email"])
        st.markdown("<h3>Información de contacto</h3>", unsafe_allow_html=True)
        st.markdown("<h3>Mi negocio</h3>", unsafe_allow_html=True)
        st.markdown("<h3>Estadísticas</h3>", unsafe_allow_html=True)
        st.write(f"{len(st.session_state.productos)} productos publicados")
        st.markdown("<h3>Miembro desde</h3>", unsafe_allow_html=True)
        st.write("Mayo 2024")
    else:
        st.warning("No has iniciado sesión. Ve a 'Acceso Comerciantes'.")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== PÁGINA: Gestión =====
elif pagina == "Gestión de mi Puesto":
    st.markdown('<div class="section"><h2>Gestión de mi Puesto</h2>', unsafe_allow_html=True)

    st.markdown('<h3>Información del Puesto</h3>', unsafe_allow_html=True)
    st.markdown('<div style="border:1px dashed #0ff; padding:20px; text-align:center; color:#0ff;">Actualizar foto de perfil<br>Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)

    st.markdown('<h3>Mis Productos</h3>', unsafe_allow_html=True)
    if st.session_state.productos:
        for p in st.session_state.productos:
            st.write(f"• {p}")
    else:
        st.write("No tienes productos aún.")

    st.markdown('<h4>Agregar Nuevo Producto</h4>', unsafe_allow_html=True)
    st.markdown('<div style="border:1px dashed #0ff; padding:20px; text-align:center; color:#0ff;">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)
    nuevo_producto = st.text_input("Nombre del producto")
    if st.button("Agregar Producto") and nuevo_producto:
        st.session_state.productos.append(nuevo_producto)
        st.experimental_rerun()

    st.markdown('<h3>Elige un Diseño para tu Catálogo</h3>', unsafe_allow_html=True)
    st.write("Selecciona la plantilla que mejor represente a tu marca.")
    if st.button("Crear Catálogo"):
        st.info("Catálogo generado (simulado).")

    st.markdown('<h3>Copia de Seguridad</h3>', unsafe_allow_html=True)
    st.button("Exportar datos")
    st.button("Importar catálogo")

    st.markdown('<h3>Crear Ficha de Producto</h3>', unsafe_allow_html=True)
    st.write("Selecciona un producto para generar su ficha individual.")

    st.markdown('</div>', unsafe_allow_html=True)