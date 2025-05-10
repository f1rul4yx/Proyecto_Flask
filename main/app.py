from flask import Flask, render_template, request, abort
import json

app = Flask(__name__)



# FUNCIONES

# Cargar JSON
with open('static/libros.json') as archivo:
    all_libros = json.load(archivo)



# RUTAS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libros', methods=['GET', 'POST'])
def libros():
    libros = []
    consulta = ''
    busqueda = False
    if request.method == 'POST':
        busqueda = True
        consulta = request.form.get('titulo', '')
        for libro in all_libros:
            if not consulta or libro['titulo'].lower().startswith(consulta.lower()):
                libros.append(libro)
    return render_template('libros.html', libros=libros, consulta=consulta, busqueda=busqueda)

@app.route('/libro/<int:id>')
def libro(id):
    libro_encontrado = None
    for libro in all_libros:
        if libro['id'] == id:
            libro_encontrado = libro            
    if libro_encontrado is None:
        abort(404)
    return render_template('libro.html', libro=libro_encontrado)



app.run("0.0.0.0",5000,debug=True)