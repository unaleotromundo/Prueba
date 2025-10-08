import streamlit as st
import time

# === CONFIGURACIÓN ===
st.set_page_config(
    page_title="FERIA ONLINE • NEON CYBER",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === ESTILOS (igual que antes) ===
st.markdown("""
<style>
/* ... (todo tu CSS y JS de partículas igual) ... */
</style>

<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">

<div id="dynamic-particles"></div>
<script>
(function() {
    const container = document.getElementById('dynamic-particles');
    const particleCount = 50;
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        const size = Math.random() * 10 + 2;
        const hue = Math.random() * 360;
        particle.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: hsl(${hue}, 100%, 70%);
            border-radius: 50%;
            box-shadow: 0 0 ${20 + size}px hsl(${hue}, 100%, 50%);
            opacity: ${Math.random() * 0.6 + 0.2};
            top: ${Math.random() * 100}vh;
            left: ${Math.random() * 100}vw;
            animation: float ${15 + Math.random() * 20}s infinite ease-in-out;
            z-index: 1;
        `;
        particle.style.setProperty('--delay', `${Math.random() * 10}s`);
        particle.style.animationDelay = `var(--delay)`;
        container.appendChild(particle);
    }

    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px) rotate(10deg); }
            50% { transform: translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px) rotate(-10deg); }
            75% { transform: translate(${Math.random() * 100 - 50}px, ${Math.random() * 100 - 50}px) rotate(5deg); }
        }
    `;
    document.head.appendChild(style);
})();
</script>
""", unsafe_allow_html=True)

# === ESTADO ===
if 'productos' not in st.session_state:
    st.session_state.productos = []
if 'comerciante' not in st.session_state:
    st.session_state.comerciante = None
if 'modo' not in st.session_state:
    st.session_state.modo = 'inicio'

# === HEADER EXACTO ===
st.markdown('<div class="neon-title">FERIA ONLINE</div>', unsafe_allow_html=True)
st.markdown('''
<p style="text-align:center; color:#0ff; font-family:Orbitron; opacity:0.8; font-size:1.2rem; max-width:800px; margin:0 auto 30px;">
Una feria virtual donde los comerciantes pueden mostrar sus productos y los clientes pueden descubrir tesoros locales
</p>
''', unsafe_allow_html=True)

# === NAVEGACIÓN ===
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 Inicio"): st.session_state.modo = 'inicio'
with col2:
    if st.button("👤 Perfil"): st.session_state.modo = 'perfil'
with col3:
    if st.button("🛠️ Gestión"): st.session_state.modo = 'gestion'
with col4:
    if st.button("🆕 Registro"): st.session_state.modo = 'registro'
with col5:
    if st.button("🔓 Acceso"): st.session_state.modo = 'login'

# === LÓGICA ===
if st.session_state.modo == 'inicio':
    st.markdown('<div class="glass-card"><h2 class="section-title">Productos Destacados</h2>', unsafe_allow_html=True)
    if st.session_state.productos:
        cols = st.columns(min(3, len(st.session_state.productos)))
        for i, prod in enumerate(st.session_state.productos[:3]):
            with cols[i]:
                st.markdown(f'''
                <div class="glass-card" style="text-align:center; transform: rotateY({i*10}deg);">
                    <h3 style="color:#0ff;">{prod}</h3>
                    <div style="height:80px; background:linear-gradient(45deg, #0a0, #00a); margin:10px; border-radius:10px;"></div>
                </div>
                ''', unsafe_allow_html=True)
    else:
        st.info("No hay productos aún.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'registro':
    st.markdown('<div class="glass-card"><h2 class="section-title">Registro de Comerciante</h2><p>Crea tu cuenta de comerciante</p>', unsafe_allow_html=True)
    nombre = st.text_input("Nombre del Comerciante", key="reg_nombre")
    email = st.text_input("Correo electrónico", key="reg_email")
    if st.button("Registrarse"):
        if nombre and email:
            st.session_state.comerciante = {"nombre": nombre, "email": email}
            st.success("¡Registro exitoso!")
            time.sleep(1)
            st.session_state.modo = 'gestion'
            st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'login':
    st.markdown('<div class="glass-card"><h2 class="section-title">Acceso Comerciantes</h2><p>Ingresa para gestionar tu puesto</p>', unsafe_allow_html=True)
    email = st.text_input("Tu correo electrónico", key="login_email")
    if st.button("Ingresar"):
        if st.session_state.comerciante and st.session_state.comerciante["email"] == email:
            st.success("Acceso concedido.")
            time.sleep(0.5)
            st.session_state.modo = 'gestion'
            st.experimental_rerun()
        else:
            st.error("Comerciante no registrado.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'perfil':
    st.markdown('<div class="glass-card"><h2 class="section-title">Mi Perfil</h2>', unsafe_allow_html=True)
    if st.session_state.comerciante:
        c = st.session_state.comerciante
        st.markdown(f"**{c['nombre']}**")
        st.markdown(c['email'])
        st.markdown("### Información de contacto")
        st.markdown("### Mi negocio")
        st.markdown("### Estadísticas")
        st.markdown(f"**{len(st.session_state.productos)} productos publicados**")
        st.markdown("### Miembro desde")
        st.write("Enero 2024")
    else:
        st.warning("No has iniciado sesión.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'gestion':
    st.markdown('<div class="glass-card"><h2 class="section-title">Gestión de mi Puesto</h2>', unsafe_allow_html=True)
    
    st.markdown("### Información del Puesto")
    st.markdown('<div style="height:100px; background:#111; border:1px dashed #0ff; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#0ff;">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)

    st.markdown("### Mis Productos")
    if st.session_state.productos:
        for p in st.session_state.productos:
            st.markdown(f"- {p}")
    else:
        st.write("No tienes productos aún.")

    st.markdown("### Agregar Nuevo Producto")
    st.markdown('<div style="height:100px; background:#111; border:1px dashed #0ff; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#0ff; margin-bottom:15px;">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)
    nuevo = st.text_input("Nombre del producto", key="nuevo_prod")
    if st.button("Agregar Producto") and nuevo:
        st.session_state.productos.append(nuevo)
        st.experimental_rerun()

    st.markdown("### Elige un Diseño para tu Catálogo")
    st.write("Selecciona la plantilla que mejor represente a tu marca.")
    if st.button("Crear Catálogo"):
        st.info("Catálogo creado.")

    st.markdown("### Copia de Seguridad")
    st.write("Exporta tus datos o importa un catálogo existente.")
    st.button("Exportar datos")
    st.button("Importar catálogo")

    st.markdown("### Crear Ficha de Producto")
    st.write("Selecciona un producto para generar su ficha individual.")
    if st.session_state.productos:
        prod_sel = st.selectbox("Producto", st.session_state.productos)
        if st.button("Generar Ficha"):
            st.success(f"Ficha de '{prod_sel}' generada.")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<p style="text-align:center; color:#0ff; opacity:0.5; font-size:0.9rem; margin-top:50px;">© 2024 Feria Online</p>', unsafe_allow_html=True)