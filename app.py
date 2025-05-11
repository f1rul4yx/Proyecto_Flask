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
    # Extraer géneros únicos
    generos = []
    for libro in all_libros:
        if libro['genero'] not in generos:
            generos.append(libro['genero'])
    generos.sort()  # Ordenar los géneros alfabéticamente
    
    libros = []
    consulta = ''
    genero_seleccionado = ''
    busqueda = False
    if request.method == 'POST':
        busqueda = True
        consulta = request.form.get('titulo', '')
        genero_seleccionado = request.form.get('genero', '')
        for libro in all_libros:
            # Verificar coincidencia con el título
            coincide_titulo = True
            if consulta:  # Si hay una consulta, verificar si está en el título
                if not libro['titulo'].lower().startswith(consulta.lower()):
                    coincide_titulo = False
            
            # Verificar coincidencia con el género
            coincide_genero = True
            if genero_seleccionado:  # Si hay un género seleccionado, verificar si coincide
                if libro['genero'] != genero_seleccionado:
                    coincide_genero = False
            
            # Añadir el libro si coincide con ambos criterios
            if coincide_titulo and coincide_genero:
                libros.append(libro)
    
    return render_template('libros.html', libros=libros, consulta=consulta, generos=generos, busqueda=busqueda, genero_seleccionado=genero_seleccionado)

@app.route('/libro/<int:id>')
def libro(id):
    libro_encontrado = None
    for libro in all_libros:
        if libro['id'] == id:
            libro_encontrado = libro            
    if libro_encontrado is None:
        abort(404)
    return render_template('libro.html', libro=libro_encontrado)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True)
