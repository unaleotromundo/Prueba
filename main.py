import streamlit as st
import time
import random

# === CONFIGURACIÓN ===
st.set_page_config(
    page_title="FERIA ONLINE • NEON CYBER",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === ESTILOS AVANZADOS: FONDO 3D, PARTÍCULAS DINÁMICAS, VIDRIO ===
st.markdown("""
<style>
/* Fondo espacial con profundidad */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at center, #0b0b1a 0%, #000000 100%);
    overflow: hidden;
    perspective: 1000px;
}

/* Partículas dinámicas generadas por JS */
#dynamic-particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}

/* Estilo "vidrio" para tarjetas */
.glass-card {
    background: rgba(10, 15, 30, 0.4);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 0 30px rgba(0, 255, 255, 0.2);
    transform-style: preserve-3d;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.glass-card:hover {
    transform: translateY(-10px) rotateX(5deg);
    box-shadow: 0 10px 40px rgba(0, 255, 255, 0.5);
}

/* Títulos neón */
.neon-title {
    color: #fff;
    font-family: 'Orbitron', monospace;
    text-shadow:
        0 0 5px #fff,
        0 0 10px #fff,
        0 0 20px #0ff,
        0 0 40px #0ff;
    font-size: 2.8rem;
    text-align: center;
    margin: 30px 0;
    letter-spacing: 3px;
}

.section-title {
    color: #0ff;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.7);
    margin-top: 20px;
}

/* Botones cyber */
.stButton > button {
    background: linear-gradient(90deg, #0ff, #0a0);
    color: black;
    font-weight: bold;
    border: none;
    padding: 12px 24px;
    border-radius: 30px;
    font-family: 'Orbitron', monospace;
    letter-spacing: 1px;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.6);
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(0, 255, 255, 0.9);
}

/* Inputs estilo terminal */
input, textarea {
    background: rgba(0, 20, 30, 0.6) !important;
    color: #0ff !important;
    border: 1px solid #0ff !important;
    font-family: 'Courier New', monospace;
}

/* Ocultar sidebar por defecto */
[data-testid="stSidebar"] {
    display: none;
}
</style>

<!-- Fuente futurista -->
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">

<!-- Partículas dinámicas con JavaScript -->
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

# === ESTADO DE LA APP ===
if 'productos' not in st.session_state:
    st.session_state.productos = []
if 'comerciante' not in st.session_state:
    st.session_state.comerciante = None
if 'modo' not in st.session_state:
    st.session_state.modo = 'inicio'

# === HEADER FUTURISTA ===
st.markdown('<div class="neon-title">FERIA ONLINE • NEON CYBER</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#0ff; font-family:Orbitron; opacity:0.8;">Conecta tu pequeño negocio con el mundo</p>', unsafe_allow_html=True)

# === NAVEGACIÓN DINÁMICA ===
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("🏠 Inicio"):
        st.session_state.modo = 'inicio'
with col2:
    if st.button("👤 Perfil"):
        st.session_state.modo = 'perfil'
with col3:
    if st.button("🛠️ Gestión"):
        st.session_state.modo = 'gestion'
with col4:
    if st.button("🆕 Registro"):
        st.session_state.modo = 'registro'
with col5:
    if st.button("🔓 Acceso"):
        st.session_state.modo = 'login'

# === LÓGICA POR MODO ===
if st.session_state.modo == 'inicio':
    st.markdown('<div class="glass-card"><h2 class="section-title">🌌 Productos Destacados</h2>', unsafe_allow_html=True)
    if st.session_state.productos:
        cols = st.columns(min(3, len(st.session_state.productos)))
        for i, prod in enumerate(st.session_state.productos[:3]):
            with cols[i]:
                st.markdown(f'''
                <div class="glass-card" style="text-align:center; transform: rotateY({i*10}deg);">
                    <h3 style="color:#0ff;">{prod}</h3>
                    <div style="height:80px; background:linear-gradient(45deg, #0a0, #00a); margin:10px; border-radius:10px;"></div>
                    <p>✨ Producto virtual</p>
                </div>
                ''', unsafe_allow_html=True)
    else:
        st.info("No hay productos aún. ¡Regístrate y agrega los tuyos!")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'registro':
    st.markdown('<div class="glass-card"><h2 class="section-title">🆕 Registro de Comerciante</h2><p>Crea tu identidad digital en la red</p>', unsafe_allow_html=True)
    nombre = st.text_input("Nombre del Comerciante", key="reg_nombre")
    email = st.text_input("Correo Corporativo", key="reg_email")
    if st.button("🚀 Crear Cuenta"):
        if nombre and email:
            st.session_state.comerciante = {"nombre": nombre, "email": email}
            st.success("✅ ¡Cuenta creada! Bienvenido a la red.")
            time.sleep(1)
            st.session_state.modo = 'gestion'
            st.experimental_rerun()
        else:
            st.error("⚠️ Completa todos los campos.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'login':
    st.markdown('<div class="glass-card"><h2 class="section-title">🔓 Acceso Comerciantes</h2><p>Ingresa tu identidad para gestionar tu puesto</p>', unsafe_allow_html=True)
    email = st.text_input("Tu Correo", key="login_email")
    if st.button("🔓 Ingresar"):
        if st.session_state.comerciante and st.session_state.comerciante["email"] == email:
            st.success("✅ Acceso concedido.")
            time.sleep(0.5)
            st.session_state.modo = 'gestion'
            st.experimental_rerun()
        else:
            st.error("❌ Identidad no reconocida en la red.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'perfil':
    st.markdown('<div class="glass-card"><h2 class="section-title">👤 Mi Perfil Digital</h2>', unsafe_allow_html=True)
    if st.session_state.comerciante:
        c = st.session_state.comerciante
        st.markdown(f"**Nombre:** {c['nombre']}")
        st.markdown(f"**Red ID:** {c['email']}")
        st.markdown("### 📡 Información de contacto")
        st.markdown("### 🏪 Mi negocio")
        st.markdown("### 📊 Estadísticas")
        st.metric("Productos Publicados", len(st.session_state.productos))
        st.markdown("### 🗓️ Miembro desde")
        st.write("Mayo 2024 • Nodo: FERIA-01")
    else:
        st.warning("⚠️ No estás autenticado. Ve a 'Acceso'.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'gestion':
    st.markdown('<div class="glass-card"><h2 class="section-title">🛠️ Gestión de mi Puesto Virtual</h2>', unsafe_allow_html=True)
    
    # Simulación de "foto de perfil 3D"
    st.markdown("### 🖼️ Información del Puesto")
    st.markdown('<div style="height:120px; background:linear-gradient(135deg, #1a1a2e, #16213e); border-radius:15px; display:flex; align-items:center; justify-content:center; color:#0ff;">[Vista 3D del Puesto]</div>', unsafe_allow_html=True)

    # Productos
    st.markdown("### 📦 Mis Productos")
    for p in st.session_state.productos:
        st.markdown(f"- {p}")

    # Agregar producto
    st.markdown("### ➕ Agregar Nuevo Producto")
    nuevo = st.text_input("Nombre del producto", key="nuevo_prod")
    if st.button("💾 Guardar en la Nube"):
        if nuevo:
            st.session_state.productos.append(nuevo)
            st.success(f"✅ '{nuevo}' sincronizado con la red.")
            st.experimental_rerun()

    # Catálogo 3D
    st.markdown("### 🎨 Elige un Diseño para tu Catálogo")
    if st.button("🌌 Generar Catálogo en Realidad Aumentada (Simulado)"):
        st.balloons()
        st.info("📦 Catálogo exportado como 'catalogo_neon.glb' (simulado)")

    # Copia de seguridad
    st.markdown("### 💾 Copia de Seguridad")
    st.button("📤 Exportar Datos")
    st.button("📥 Importar Catálogo")

    # Ficha de producto
    st.markdown("### 📄 Crear Ficha de Producto")
    if st.session_state.productos:
        prod_sel = st.selectbox("Selecciona un producto", st.session_state.productos)
        if st.button("🖨️ Generar Ficha 3D"):
            st.markdown(f'<div class="glass-card" style="text-align:center;"><h3>FICHA: {prod_sel}</h3><div style="height:150px; background:radial-gradient(circle, #00a, #000); margin:15px; border-radius:10px;"></div><p>Formato: GLB • Listo para RA</p></div>', unsafe_allow_html=True)
    else:
        st.write("No hay productos para generar ficha.")

    st.markdown('</div>', unsafe_allow_html=True)

# === PIE DE PÁGINA ===
st.markdown('<p style="text-align:center; color:#0ff; opacity:0.5; font-size:0.9rem; margin-top:50px;">FERIA ONLINE • Red descentralizada v1.0 • © 2024</p>', unsafe_allow_html=True)