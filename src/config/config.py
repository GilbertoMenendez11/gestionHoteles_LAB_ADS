from decouple import config

#Define la clave secreta desde el archivo .env o variable de entorno
class Config:
    SECRET_KEY = config('SECRET_KEY')

#Actividad el modo debug para el entorno de desarrollo
class DevolopmentConfig(Config):
    DEBUG = True

#Diccionario para mapear nombres de entorno a sus configuraciones
app_config={
    'development': DevolopmentConfig
}