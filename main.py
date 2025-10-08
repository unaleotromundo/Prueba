from flask import Flask, render_template_string, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_feria_online'

# Datos simulados
comerciantes = {}
productos = []

# Plantilla base (común a todas las páginas)
base_template = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Feria Online</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: #f9f9f9; }
        .container { max-width: 900px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        nav a { margin-right: 15px; text-decoration: none; color: #007BFF; font-weight: bold; }
        .section { margin: 20px 0; padding: 15px; border: 1px solid #eee; border-radius: 6px; background: #fafafa; }
        .flash { color: green; font-weight: bold; margin: 10px 0; }
        input, button { padding: 8px; margin: 5px 0; width: 100%; max-width: 300px; }
        ul { padding-left: 20px; }
        h1 { color: #2c3e50; }
        h2 { color: #3498db; }
        h3 { color: #2980b9; }
        .dropzone {
            border: 2px dashed #ccc;
            border-radius: 6px;
            padding: 30px;
            text-align: center;
            margin: 10px 0;
            color: #777;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Conecta tu pequeño negocio con el mundo</h1>
        <p>Una feria virtual donde los comerciantes pueden mostrar sus productos y los clientes pueden descubrir tesoros locales</p>

        <nav>
            <a href="{{ url_for('index') }}">Inicio</a>
            <a href="{{ url_for('perfil') }}">Mi Perfil</a>
            <a href="{{ url_for('gestion') }}">Gestión de mi Puesto</a>
            <a href="{{ url_for('registro') }}">Registro de Comerciante</a>
            <a href="{{ url_for('login') }}">Acceso Comerciantes</a>
        </nav>

        {% with messages = get_flashed_messages() %}
          {% if messages %}
            {% for message in messages %}
              <p class="flash">{{ message }}</p>
            {% endfor %}
          {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    content = '''
    {% extends "base" %}
    {% block content %}
    <h2>Productos Destacados</h2>
    <div class="section">
        {% if productos_destacados %}
            <ul>
            {% for p in productos_destacados %}
                <li>{{ p.nombre }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No hay productos destacados aún.</p>
        {% endif %}
    </div>
    {% endblock %}
    '''
    return render_template_string(base_template + content, productos_destacados=productos[:4])

@app.route('/perfil')
def perfil():
    comerciante = {
        'nombre': 'Nombre del Comerciante',
        'email': 'correo@ejemplo.com',
        'miembro_desde': 'Enero 2024',
        'productos_publicados': len(productos)
    }
    content = '''
    {% extends "base" %}
    {% block content %}
    <div class="section">
        <h2>Mi Perfil</h2>
        <p><strong>{{ comerciante.nombre }}</strong></p>
        <p>{{ comerciante.email }}</p>

        <h3>Información de contacto</h3>
        <h3>Mi negocio</h3>
        <h3>Estadísticas</h3>
        <p>{{ comerciante.productos_publicados }} productos publicados</p>
        <h3>Miembro desde</h3>
        <p>{{ comerciante.miembro_desde }}</p>
    </div>
    {% endblock %}
    '''
    return render_template_string(base_template + content, comerciante=comerciante)

@app.route('/gestion')
def gestion():
    content = '''
    {% extends "base" %}
    {% block content %}
    <h2>Gestión de mi Puesto</h2>

    <div class="section">
        <h3>Información del Puesto</h3>
        <div class="dropzone">Actualizar foto de perfil<br>Haz clic o arrastra una imagen aquí</div>
    </div>

    <div class="section">
        <h3>Mis Productos</h3>
        {% if productos %}
            <ul>
            {% for p in productos %}
                <li>{{ p.nombre }}</li>
            {% endfor %}
            </ul>
        {% else %}
            <p>No tienes productos aún.</p>
        {% endif %}

        <h4>Agregar Nuevo Producto</h4>
        <div class="dropzone">Haz clic o arrastra una imagen aquí</div>
        <form method="POST" action="{{ url_for('agregar_producto') }}">
            <input type="text" name="nombre_producto" placeholder="Nombre del producto" required>
            <button type="submit">Agregar Producto</button>
        </form>
    </div>

    <div class="section">
        <h3>Elige un Diseño para tu Catálogo</h3>
        <p>Selecciona la plantilla que mejor represente a tu marca.</p>
        <button>Crear Catálogo</button>
    </div>

    <div class="section">
        <h3>Copia de Seguridad</h3>
        <button>Exportar datos</button>
        <button>Importar catálogo</button>
    </div>

    <div class="section">
        <h3>Crear Ficha de Producto</h3>
        <p>Selecciona un producto para generar su ficha individual.</p>
    </div>
    {% endblock %}
    '''
    return render_template_string(base_template + content, productos=productos)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        comerciantes[email] = {'nombre': nombre, 'email': email}
        flash('¡Registro exitoso! Ahora puedes acceder.')
        return redirect(url_for('login'))
    
    content = '''
    {% extends "base" %}
    {% block content %}
    <div class="section">
        <h2>Registro de Comerciante</h2>
        <h3>Crea tu cuenta de comerciante</h3>
        <form method="POST">
            <input type="text" name="nombre" placeholder="Nombre completo" required>
            <input type="email" name="email" placeholder="correo@ejemplo.com" required>
            <button type="submit">Registrarse</button>
        </form>
    </div>
    {% endblock %}
    '''
    return render_template_string(base_template + content)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        if email in comerciantes:
            flash('Acceso concedido.')
            return redirect(url_for('gestion'))
        else:
            flash('Comerciante no registrado.')
    
    content = '''
    {% extends "base" %}
    {% block content %}
    <div class="section">
        <h2>Acceso Comerciantes</h2>
        <p>Ingresa para gestionar tu puesto</p>
        <form method="POST">
            <input type="email" name="email" placeholder="correo@ejemplo.com" required>
            <button type="submit">Ingresar</button>
        </form>
    </div>
    {% endblock %}
    '''
    return render_template_string(base_template + content)

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form.get('nombre_producto', 'Producto sin nombre')
    productos.append({'nombre': nombre})
    return redirect(url_for('gestion'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)