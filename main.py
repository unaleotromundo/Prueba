import streamlit as st
import json
import time
from datetime import datetime

# === CONFIGURACIÓN ===
st.set_page_config(
    page_title="FERIA ONLINE",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# === ESTILOS MEJORADOS CON SOPORTE CLARO/OSCURO ===
def render_styles(theme):
    bg_primary = "#ffffff" if theme == "light" else "#161b22"
    bg_secondary = "#f6f8fa" if theme == "light" else "#0d1117"
    text_primary = "#0d1117" if theme == "light" else "#f0f6fc"
    border_color = "#d0d7de" if theme == "light" else "#30363d"
    primary = "#6366f1"
    cyan = "#06b6d4"
    success = "#16a34a"
    
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: {bg_secondary};
        color: {text_primary};
    }}
    .card {{
        background: {bg_primary};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 25px;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
    }}
    .section-title {{
        color: {primary};
        font-size: 2rem;
        font-weight: 700;
        margin: 20px 0;
    }}
    .btn {{
        background: linear-gradient(135deg, {primary}, {cyan});
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: bold;
        cursor: pointer;
        margin: 5px 0;
        display: inline-block;
    }}
    .btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
    }}
    input, textarea {{
        background: {bg_primary} !important;
        color: {text_primary} !important;
        border: 1px solid {border_color} !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }}
    .theme-toggle {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 100;
        background: {bg_primary};
        color: {text_primary};
        border: 1px solid {border_color};
        width: 50px;
        height: 50px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }}
    .upload-area {{
        border: 2px dashed {border_color};
        border-radius: 12px;
        padding: 25px;
        text-align: center;
        color: {text_primary};
        background: {bg_secondary};
        margin: 15px 0;
    }}
    .product-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }}
    .product-card {{
        background: {bg_primary};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 15px;
        text-align: center;
    }}
    .product-price {{
        color: {success};
        font-weight: bold;
        font-size: 1.2rem;
        margin: 8px 0;
    }}
    </style>
    """, unsafe_allow_html=True)

# === INICIALIZAR ESTADO ===
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

if 'comerciantes' not in st.session_state:
    st.session_state.comerciantes = {
        "c1": {"id": "c1", "nombre": "María Artesanías", "email": "maria@feria.com"},
        "c2": {"id": "c2", "nombre": "Carlos Juguetes", "email": "carlos@feria.com"},
        "c3": {"id": "c3", "nombre": "Lucía Gastronomía", "email": "lucia@feria.com"},
        "c4": {"id": "c4", "nombre": "Andrés Tecnología", "email": "andres@feria.com"},
    }

if 'productos' not in st.session_state:
    st.session_state.productos = [
        {"id": "p1", "nombre": "Mandala de Madera", "precio": 1200, "descripcion": "Artesanía en madera fina", "categoria": "artesania", "vendedor_id": "c1"},
        {"id": "p2", "nombre": "Collar de Semillas", "precio": 800, "descripcion": "Hecho a mano con semillas naturales", "categoria": "artesania", "vendedor_id": "c1"},
        {"id": "p3", "nombre": "Muñeco de Trapo", "precio": 1500, "descripcion": "Juguete artesanal para niños", "categoria": "juguetes", "vendedor_id": "c2"},
        {"id": "p4", "nombre": "Rompecabezas Madera", "precio": 2000, "descripcion": "100 piezas, diseño ecológico", "categoria": "juguetes", "vendedor_id": "c2"},
        {"id": "p5", "nombre": "Mermelada Arándanos", "precio": 600, "descripcion": "Hecha en casa, sin conservantes", "categoria": "gastronomia", "vendedor_id": "c3"},
        {"id": "p6", "nombre": "Pan Artesanal", "precio": 400, "descripcion": "Horno de barro, masa madre", "categoria": "gastronomia", "vendedor_id": "c3"},
        {"id": "p7", "nombre": "Cargador Solar", "precio": 3500, "descripcion": "Para celular y tablet", "categoria": "tecnologia", "vendedor_id": "c4"},
        {"id": "p8", "nombre": "Lámpara LED", "precio": 2800, "descripcion": "Regulable, diseño moderno", "categoria": "tecnologia", "vendedor_id": "c4"},
        {"id": "p9", "nombre": "Caja de Regalo", "precio": 900, "descripcion": "Personalizable con tus diseños", "categoria": "artesania", "vendedor_id": "c1"},
        {"id": "p10", "nombre": "Títere de Dedo", "precio": 700, "descripcion": "Ideal para contar cuentos", "categoria": "juguetes", "vendedor_id": "c2"},
        {"id": "p11", "nombre": "Aceite de Oliva", "precio": 1100, "descripcion": "Primera presión en frío", "categoria": "gastronomia", "vendedor_id": "c3"},
        {"id": "p12", "nombre": "Power Bank", "precio": 2200, "descripcion": "10000 mAh, carga rápida", "categoria": "tecnologia", "vendedor_id": "c4"},
        {"id": "p13", "nombre": "Portavelas Cerámica", "precio": 1300, "descripcion": "Hecho a mano, esmaltado", "categoria": "artesania", "vendedor_id": "c1"},
        {"id": "p14", "nombre": "Rompecabezas 3D", "precio": 2500, "descripcion": "Torre Eiffel en madera", "categoria": "juguetes", "vendedor_id": "c2"},
        {"id": "p15", "nombre": "Dulce de Leche", "precio": 550, "descripcion": "Receta tradicional", "categoria": "gastronomia", "vendedor_id": "c3"},
        {"id": "p16", "nombre": "Soporte para Celular", "precio": 950, "descripcion": "Ajustable, base antideslizante", "categoria": "tecnologia", "vendedor_id": "c4"},
        {"id": "p17", "nombre": "Bolso de Tela", "precio": 1400, "descripcion": "Estampado con serigrafía", "categoria": "artesania", "vendedor_id": "c1"},
        {"id": "p18", "nombre": "Juego de Memoria", "precio": 1800, "descripcion": "Ilustraciones originales", "categoria": "juguetes", "vendedor_id": "c2"},
        {"id": "p19", "nombre": "Miel de Abejas", "precio": 750, "descripcion": "Pura, de colmenas locales", "categoria": "gastronomia", "vendedor_id": "c3"},
        {"id": "p20", "nombre": "Cable USB Reforzado", "precio": 650, "descripcion": "Trenzado, 2 metros", "categoria": "tecnologia", "vendedor_id": "c4"},
    ]

if 'modo' not in st.session_state:
    st.session_state.modo = 'inicio'
if 'comerciante_actual' not in st.session_state:
    st.session_state.comerciante_actual = None

# === FUNCIONES DE UTILIDAD ===
def exportar_json():
    if not st.session_state.productos:
        return None
    return json.dumps(st.session_state.productos, indent=2, ensure_ascii=False)

def importar_json(data_str):
    try:
        data = json.loads(data_str)
        if isinstance(data, list):
            st.session_state.productos = data
            return True
    except:
        pass
    return False

def productos_del_comerciante(cid):
    return [p for p in st.session_state.productos if p.get("vendedor_id") == cid]

# === RENDERIZAR ESTILOS ===
render_styles(st.session_state.theme)

# === HEADER ===
st.markdown('<div style="text-align:center; margin:30px 0;"><h1>FERIA ONLINE</h1><p>Una feria virtual donde los comerciantes pueden mostrar sus productos y los clientes pueden descubrir tesoros locales</p></div>', unsafe_allow_html=True)

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

# === BOTÓN DE CAMBIO DE TEMA ===
theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
if st.button(theme_icon, key="theme_toggle", help="Cambiar tema"):
    st.session_state.theme = "dark" if st.session_state.theme == "light" else "light"
    st.experimental_rerun()

# === LÓGICA POR MODO ===
if st.session_state.modo == 'inicio':
    st.markdown('<div class="card"><h2 class="section-title">Productos Destacados</h2>', unsafe_allow_html=True)
    destacados = st.session_state.productos[:8]
    cols = st.columns(4)
    for i, p in enumerate(destacados):
        with cols[i % 4]:
            vendedor = st.session_state.comerciantes.get(p["vendedor_id"], {})
            st.markdown(f'''
            <div class="product-card">
                <h4>{p["nombre"]}</h4>
                <div class="product-price">${p["precio"]}</div>
                <p style="font-size:0.9em; color:gray;">{vendedor.get("nombre", "Vendedor")}</p>
                <p style="font-size:0.85em;">{p["categoria"]}</p>
            </div>
            ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'registro':
    st.markdown('<div class="card"><h2 class="section-title">Registro de Comerciante</h2><p>Crea tu cuenta de comerciante</p>', unsafe_allow_html=True)
    nombre = st.text_input("Nombre del Comerciante")
    email = st.text_input("Correo electrónico")
    if st.button("Registrarse"):
        if nombre and email:
            cid = f"c{len(st.session_state.comerciantes)+1}"
            st.session_state.comerciantes[cid] = {
                "id": cid,
                "nombre": nombre,
                "email": email
            }
            st.success("¡Registro exitoso!")
            time.sleep(1)
            st.session_state.modo = 'login'
            st.experimental_rerun()
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'login':
    st.markdown('<div class="card"><h2 class="section-title">Acceso Comerciantes</h2><p>Ingresa para gestionar tu puesto</p>', unsafe_allow_html=True)
    email = st.text_input("Tu correo electrónico")
    if st.button("Ingresar"):
        for cid, c in st.session_state.comerciantes.items():
            if c["email"] == email:
                st.session_state.comerciante_actual = c
                st.success("Acceso concedido.")
                time.sleep(0.5)
                st.session_state.modo = 'gestion'
                st.experimental_rerun()
        st.error("Comerciante no registrado.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'perfil':
    st.markdown('<div class="card"><h2 class="section-title">Mi Perfil</h2>', unsafe_allow_html=True)
    if st.session_state.comerciante_actual:
        c = st.session_state.comerciante_actual
        st.markdown(f"**{c['nombre']}**")
        st.markdown(c['email'])
        st.markdown("### Información de contacto")
        st.markdown("### Mi negocio")
        st.markdown("### Estadísticas")
        mis_productos = productos_del_comerciante(c["id"])
        st.markdown(f"**{len(mis_productos)} productos publicados**")
        st.markdown("### Miembro desde")
        st.write("Enero 2024")
    else:
        st.warning("No has iniciado sesión.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.modo == 'gestion':
    if not st.session_state.comerciante_actual:
        st.warning("Debes iniciar sesión primero.")
        st.session_state.modo = 'login'
        st.experimental_rerun()
    
    c = st.session_state.comerciante_actual
    mis_productos = productos_del_comerciante(c["id"])
    
    st.markdown(f'<div class="card"><h2 class="section-title">Gestión de mi Puesto - {c["nombre"]}</h2>', unsafe_allow_html=True)
    
    # Información del Puesto
    st.markdown("### Información del Puesto")
    st.markdown('<div class="upload-area">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)

    # Mis Productos
    st.markdown("### Mis Productos")
    if mis_productos:
        for p in mis_productos:
            st.markdown(f"- **{p['nombre']}** - ${p['precio']} ({p['categoria']})")
    else:
        st.write("No tienes productos aún.")

    # Agregar Nuevo Producto
    st.markdown("### Agregar Nuevo Producto")
    st.markdown('<div class="upload-area">Haz clic o arrastra una imagen aquí</div>', unsafe_allow_html=True)
    col_n1, col_n2, col_n3 = st.columns(3)
    with col_n1:
        nombre_prod = st.text_input("Nombre")
    with col_n2:
        precio_prod = st.number_input("Precio ($)", min_value=0, value=0)
    with col_n3:
        cat_prod = st.selectbox("Categoría", ["artesania", "juguetes", "gastronomia", "tecnologia", "otros"])
    desc_prod = st.text_area("Descripción")
    if st.button("Agregar Producto") and nombre_prod:
        nuevo_id = f"p{len(st.session_state.productos)+1}"
        st.session_state.productos.append({
            "id": nuevo_id,
            "nombre": nombre_prod,
            "precio": precio_prod,
            "descripcion": desc_prod,
            "categoria": cat_prod,
            "vendedor_id": c["id"]
        })
        st.success("Producto agregado.")
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
        if json_data:  # ✅ CORREGIDO: condición completa
            b64 = base64.b64encode(json_data.encode()).decode()
            href = f'<a href="data:file/json;base64,{b64}" download="catalogo-feria-virtual-{datetime.now().strftime("%Y-%m-%d")}.json" class="btn">⬇️ Descargar JSON</a>'
            st.markdown(href, unsafe_allow_html=True)
    
    # Importar
    uploaded_file = st.file_uploader("📥 Importar catálogo", type="json")
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        if importar_json(content):
            st.success("Catálogo importado.")
            st.experimental_rerun()

    # Crear Ficha de Producto
    st.markdown("### Crear Ficha de Producto")
    st.write("Selecciona un producto para generar su ficha individual.")
    if mis_productos:
        prod_nombres = {p["nombre"]: p["id"] for p in mis_productos}
        sel = st.selectbox("Producto", list(prod_nombres.keys()))
        if st.button("🖨️ Generar Ficha"):
            st.info(f"Ficha de '{sel}' generada.")
    else:
        st.write("No hay productos para generar ficha.")

    st.markdown('</div>', unsafe_allow_html=True)

# === PIE DE PÁGINA ===
st.markdown('<p style="text-align:center; margin-top:50px; opacity:0.7;">© 2024 Feria Online</p>', unsafe_allow_html=True)