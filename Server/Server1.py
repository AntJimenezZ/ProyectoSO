from flask import Flask
from base_app import BaseApp

app = Flask(__name__)

# Usar la clase BaseApp para configurar las rutas y la lógica
BaseApp(app)

@app.route('/')
def hello():
    return "Servidor Flask 1"

if __name__ == '__main__':
    app.run(debug=True, port=8081)
