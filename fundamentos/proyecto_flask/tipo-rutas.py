from flask import Flask

app = Flask(__name__)

@app.route('/contacto')
def contacto():
    return('pagina contacto')

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'pagina del usuario: {nombre}'

app.run(debug=True)