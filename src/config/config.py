from decouple import config

#Define la clave secreta desde el archivo .env o variable de entorno
class Config:
    SECRET_KEY = config('SECRET_KEY')
    TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
    TWILIO_WHATSAPP_NUMBER = config('TWILIO_WHATSAPP_NUMBER')

#Actividad el modo debug para el entorno de desarrollo
class DevolopmentConfig(Config):
    DEBUG = True

#Diccionario para mapear nombres de entorno a sus configuraciones
app_config={
    'development': DevolopmentConfig
}