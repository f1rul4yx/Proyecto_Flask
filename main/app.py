from flask import Flask, render_template

app = Flask(__name__)

# FUNCIONES



# RUTAS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generic')
def generic():
    return render_template('generic.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

app.run("0.0.0.0",5000,debug=True)
