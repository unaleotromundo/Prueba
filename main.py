import streamlit as st
import json
import base64
from datetime import datetime
import time

# === CONFIGURACIÓN ===
st.set_page_config(
    page_title="FERIA ONLINE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === ESTILOS: FUSIÓN CYBERPUNK + DISEÑO PROFESIONAL ===
st.markdown("""
<style>
/* --- FONDO CYBERPUNK CON PATRÓN SUTIL --- */
[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse at center, #0f0c29 0%, #302b63 30%, #000000 100%);
    overflow: hidden;
    perspective: 1000px;
}

/* --- PARTÍCULAS DINÁMICAS --- */
#dynamic-particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 1;
}

/* --- VARIABLES DE COLOR CYBER (INSPIRADAS EN TU CSS) --- */
:root {
    --primary: #6366f1;
    --cyan: #06b6d4;
    --success: #16a34a;
    --error: #dc2626;
    --text-primary: #f0f6fc;
    --bg-primary: rgba(15, 23, 42, 0.7);
    --border-color: #30363d;
    --shadow-md: 0 4px 8px rgba(0, 0, 0, 0.5);
}

/* --- TARJETAS VIDRIO CYBER --- */
.glass-card {
    background: var(--bg-primary);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(6, 182, 212, 0.4);
    border-radius: 16px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 0 25px rgba(6, 182, 212, 0.3);
    transform-style: preserve-3d;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.glass-card:hover {
    transform: translateY(-8px) rotateX(3deg);
    box-shadow: 0 10px 35px rgba(6, 182, 212, 0.6);
}

/* --- TÍTULOS NEÓN --- */
.neon-title {
    color: white;
    font-family: 'Segoe UI', sans-serif;
    text-shadow:
        0 0 5px #fff,
        0 0 10px #fff,
        0 0 20px var(--cyan),
        0 0 40px var(--cyan);
    font-size: 2.5rem;
    text-align: center;
    margin: 30px 0;
    letter-spacing: 2px;
    font-weight: 800;
}

.section-title {
    color: var(--cyan);
    text-shadow: 0 0 10px rgba(6, 182, 212, 0.7);
    margin-top: 20px;
    font-size: 1.8rem;
    font-weight: 700;
}

/* --- BOTONES CYBER --- */
.stButton > button {
    background: linear-gradient(135deg, var(--primary), var(--cyan));
    color: white;
    font-weight: bold;
    border: none;
    padding: 12px 24px;
    border-radius: 12px;
    font-family: 'Segoe UI', sans-serif;
    cursor: pointer;
    transition: all 0.3s;
    box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
}

.stButton > button:hover {
    transform: scale(1.05) translateY(-2px);
    box-shadow: 0 0 25px rgba(6, 182, 212, 0.8);
}

/* --- INPUTS TERMINAL --- */
input, textarea {
    background: rgba(10, 15, 30, 0.6) !important;
    color: var(--cyan) !important;
    border: 1px solid var(--cyan) !important;
    font-family: 'Courier New', monospace;
}

/* --- OCULTAR SIDEBAR --- */
[data-testid="stSidebar"] {
    display: none;
}

/* --- ÁREAS DE SUBIDA --- */
.upload-area {
    border: 2px dashed var(--cyan);
    border-radius: 12px;
    padding: 25px;
    text-align: center;
    color: var(--cyan);
    background: rgba(0, 20, 30, 0.3);
    margin: 15px 0;
    transition: all 0.3s;
}

.upload-area:hover {
    background: rgba(6, 182, 212, 0.1);
    transform: scale(1.02);
}
</style>

<!-- Partículas dinámicas -->
<div id="dynamic-particles"></div>
<script>
(function() {
    const container = document.getElementById('dynamic-particles');
    const particleCount = 40;
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        const size = Math.random() * 8 + 2;
        const hue = Math.random() * 360;
        particle.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: hsl(${hue}, 100%, 70%);
            border-radius: 50%;
            box-shadow: 0 0 ${15 + size}px hsl(${hue}, 100%, 50%);
            opacity: ${Math.random() * 0.5 + 0.2};
            top: ${Math.random() * 100}vh;
            left: ${Math.random() * 100}vw;
            animation: float ${12 + Math.random() * 18}s infinite ease-in-out;
            z-index: 1;
        `;
        particle.style.setProperty('--delay', `${Math.random() * 8}s`);
        particle.style.animationDelay = `var(--delay)`;
        container.appendChild(particle);
    }

    const style = document.createElement('style');
    style.textContent = `
        @keyframes float {
            0%, 100% { transform: translate(0, 0) rotate(0deg); }
            25% { transform: translate(${Math.random() * 80 - 40}px, ${Math.random() * 80 - 40}px) rotate(8deg); }
            50% { transform: translate(${Math.random() * 80 - 40}px, ${Math.random() * 80 - 40}px) rotate(-8deg); }
            75% { transform: translate(${Math.random() * 80 - 40}px, ${Math.random() * 80 - 40}px) rotate(4deg); }
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

# === FUNCIONES DE EXPORTACIÓN/IMPORTACIÓN ===
def exportar_json():
    if not st.session_state.productos:
        return None
    data = []
    for p in st.session_state.productos:
        data.append({
            "name": p.get("nombre", ""),
            "price": p.get("precio", 0),
            "description": p.get("descripcion", ""),
            "category": p.get("categoria", "otros"),
            "published": True
        })
    return json.dumps(data, indent=2)

def importar_json(json_str):
    try:
        data = json.loads(json_str)
        if not isinstance(data, list):
            st.error("Formato inválido.")
            return False
        nuevos = []
        for item in data:
            nuevos.append({
                "nombre": item.get("name", "Producto sin nombre"),
                "precio": item.get("price", 0),
                "descripcion": item.get("description", ""),
                "categoria": item.get("category", "otros")
            })
        st.session_state.productos.extend(nuevos)
        return True
    except Exception as e:
        st.error(f"Error al importar: {str(e)}")
        return False

# === HEADER ===
st.markdown('<div class="neon-title">FERIA ONLINE</div>', unsafe_allow_html=True)
st.markdown('''
<p style="text-align:center; color:#0ff; font-family:'Segoe UI'; opacity:0.9; font-size:1.2rem; max-width:800px; margin:0 auto 30px;">
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

# === LÓGICA POR MODO ===
if st.session_state.modo == 'inicio':
    st.markdown('<div class="glass-card"><h2 class="section-title">Productos Destacados</h2>', unsafe_allow_html=True)
    if st.session_state.productos:
        cols = st.columns(min(3, len(st.session_state.productos)))
        for i, prod in enumerate(st.session_state.productos[:3]):
            with cols[i]:
                st.markdown(f'''
                <div class="glass-card" style="text-align:center; transform: rotateY({i*8}deg);">
                    <h3 style="color:var(--cyan);">{prod["nombre"]}</h3>
                    <p style="color:#16a34a;">${prod.get("precio", 0):.2f}</p>
                    <p style="font-size:0.9rem; color:#aaa;">{prod.get("categoria", "otros")}</p>
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
    
    # Información del Puesto
    st.markdown("### Información del Puesto")
    st.markdown('<div class="upload-area">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)

    # Mis Productos
    st.markdown("### Mis Productos")
    if st.session_state.productos:
        for p in st.session_state.productos:
            st.markdown(f"- **{p['nombre']}** - ${p.get('precio', 0):.2f} ({p.get('categoria', 'otros')})")
    else:
        st.write("No tienes productos aún.")

    # Agregar Nuevo Producto
    st.markdown("### Agregar Nuevo Producto")
    st.markdown('<div class="upload-area">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)
    col_n1, col_n2, col_n3 = st.columns(3)
    with col_n1:
        nombre_prod = st.text_input("Nombre", key="nombre_prod")
    with col_n2:
        precio_prod = st.number_input("Precio ($)", min_value=0.0, value=0.0, key="precio_prod")
    with col_n3:
        cat_prod = st.text_input("Categoría", value="otros", key="cat_prod")
    desc_prod = st.text_area("Descripción", key="desc_prod")
    if st.button("Agregar Producto") and nombre_prod:
        st.session_state.productos.append({
            "nombre": nombre_prod,
            "precio": precio_prod,
            "descripcion": desc_prod,
            "categoria": cat_prod
        })
        st.experimental_rerun()

    # Elige un Diseño para tu Catálogo
    st.markdown("### Elige un Diseño para tu Catálogo")
    st.write("Selecciona la plantilla que mejor represente a tu marca.")
    if st.button("Crear Catálogo"):
        st.info("Catálogo generado (simulado).")

    # Copia de Seguridad
    st.markdown("### Copia de Seguridad")
    st.write("Exporta tus datos o importa un catálogo existente.")
    
    # Exportar
    if st.button("📤 Exportar datos"):
        json_data = exportar_json()
        if json_data:
            b64 = base64.b64encode(json_data.encode()).decode()
            href = f'<a href="data:file/json;base64,{b64}" download="catalogo-feria-virtual-{datetime.now().strftime("%Y-%m-%d")}.json" class="stButton">⬇️ Descargar JSON</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    # Importar
    uploaded_file = st.file_uploader("📥 Importar catálogo", type="json", key="import_json")
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        if importar_json(content):
            st.success("Catálogo importado correctamente.")
            st.experimental_rerun()

    # Crear Ficha de Producto
    st.markdown("### Crear Ficha de Producto")
    st.write("Selecciona un producto para generar su ficha individual.")
    if st.session_state.productos:
        nombres = [p["nombre"] for p in st.session_state.productos]
        prod_sel = st.selectbox("Producto", nombres)
        if st.button("🖨️ Generar Ficha"):
            st.info(f"Ficha de '{prod_sel}' generada (simulada).")
    else:
        st.write("No hay productos para generar ficha.")

    st.markdown('</div>', unsafe_allow_html=True)

# === PIE DE PÁGINA ===
st.markdown('<p style="text-align:center; color:var(--cyan); opacity:0.6; font-size:0.9rem; margin-top:50px;">© 2024 Feria Online</p>', unsafe_allow_html=True)