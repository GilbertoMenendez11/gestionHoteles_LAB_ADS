from utils.DateFormat import DateFormat

class Telefono:
    def __init__(self, id_telefono, nombre_telefono, numero_telefono, fecha_creacion_telefono):
        self.id_telefono = id_telefono
        self.nombre_telefono = nombre_telefono
        self.numero_telefono = numero_telefono
        self.fecha_creacion_telefono = DateFormat.convert_date(fecha_creacion_telefono)

    def to_JSON(self):
        return{
            "id_telefono": self.id_telefono,
            "nombre": self.nombre_telefono,
            "numero": self.numero_telefono,
            "fecha_creacion": self.fecha_creacion_telefono
        } 