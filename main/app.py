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

@app.route('/libros', methods=['GET'])
def libros():
    return render_template('libros.html')

@app.route('/listalibros', methods=['POST'])
def listalibros():
    consulta = request.form.get('titulo', '')
    libros = []
    for libro in all_libros:
        if not consulta or libro['titulo'].lower().startswith(consulta.lower()):
            libros.append(libro)
    return render_template('listalibros.html', libros=libros)



app.run("0.0.0.0",5000,debug=True)