from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Bienvenido al sistema'

@app.route('/saludo')
def saludo():
    return 'Hola aprendiz ADSO'

@app.route('/inventario')  
def inventario():
    return 'Sistema inventario activo'

@app.route('/usuario')
def usuario():
    return 'Sistema usuario activo'


app.run(debug=True)