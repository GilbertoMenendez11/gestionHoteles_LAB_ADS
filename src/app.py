from flask import Flask
from flask_cors import CORS
from config.config import app_config

from apis.empleados.routes import Empleados

#Crear una instancia de la aplicacion flask 
app = Flask(__name__)

#Habilitar CORS para todas las rutas y origenes
#Esto permite que el frontend realice solitudes a la API
CORS(app)

#Definir un manejador de errores para rutas no encontradas
def paginaNoEncontrada(error):
    return "<h1>Página no encontrada</h1>", 404

def errorServidor(error):
    return "<h1>Error intero del servidor</h1>", 500

@app.route('/')
def principal():
    return "<h1>Bienvenido a mi aplicacion con Falsk</h1>"

if __name__ == '__main__':
    #Cargamos las configuracion para el entorno 'development'
    app.config.from_object(app_config['development'])

    app.register_blueprint(Empleados.main, url_prefix="/api/empleados")

    #Registramos el manejador de error 404
    app.register_error_handler(404, paginaNoEncontrada)
    app.register_error_handler(500, errorServidor)

    #Iniciamos el servidor de flask, escuchando en el puerto 5000.
    app.run(host='0.0.0.0', port=5000, debug=True)

