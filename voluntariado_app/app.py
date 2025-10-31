from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista temporal de proyectos (simula una base de datos)
proyectos_data = [
    {
        "nombre": "Reforestación Urbana",
        "objetivo": "Plantar 100 árboles en parques locales",
        "fecha_inicio": "2025-10-01",
        "voluntarios": 12,
        "progreso": 75,
        "estado": "Activo"
    },
    {
        "nombre": "Limpieza de Playas",
        "objetivo": "Recolectar residuos plásticos",
        "fecha_inicio": "2025-09-15",
        "voluntarios": 25,
        "progreso": 90,
        "estado": "Finalizado"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proyectos', methods=['GET', 'POST'])
def proyectos():
    # Si se envía el formulario
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        objetivo = request.form.get('objetivo')
        fecha_inicio = request.form.get('fecha_inicio')

        # Crear nuevo proyecto y añadirlo a la lista
        nuevo_proyecto = {
            "nombre": nombre,
            "objetivo": objetivo,
            "fecha_inicio": fecha_inicio,
            "voluntarios": 0,
            "progreso": 0,
            "estado": "Activo"
        }
        proyectos_data.append(nuevo_proyecto)

        # Redirigir para evitar reenvíos del formulario
        return redirect(url_for('proyectos'))

    # Mostrar la tabla de proyectos
    return render_template('proyectos.html', proyectos=proyectos_data)

# ---- Otras rutas ----
@app.route('/ongs')
def ongs():
    return render_template('ongs.html')

@app.route('/voluntarios')
def voluntarios():
    return render_template('voluntarios.html')

@app.route('/certificados')
def certificados():
    return render_template('certificados.html')

@app.route('/reportes')
def reportes():
    return render_template('reportes.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/voluntario')
def voluntario():
    return render_template('voluntario.html')

@app.route('/coordinador')
def coordinador():
    return render_template('coordinador.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(debug=True)
