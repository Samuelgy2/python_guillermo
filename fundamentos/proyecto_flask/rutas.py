from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola mundo con flask'

app.run(debug=True)