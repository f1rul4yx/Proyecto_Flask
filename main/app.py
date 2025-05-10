from flask import Flask, render_template
import json

app = Flask(__name__)

# FUNCIONES

# Cargar JSON
with open('static/libros.json') as archivo:
    libros = json.load(archivo)

# RUTAS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/libros', methods=['GET'])
def libros():
    return render_template('libros.html')

@app.route('/listalibros', methods=['POST'])
def listalibros():
    return render_template('listalibros.html')

app.run("0.0.0.0",5000,debug=True)