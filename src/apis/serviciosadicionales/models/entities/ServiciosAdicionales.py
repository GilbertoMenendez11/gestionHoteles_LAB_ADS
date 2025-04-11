from utils.DateFormat import DateFormat

class Servicio:
    def __init__(self, id_servicio, nombre_servicio, descripcion_servicio, precio_servicio):
        self.id_servicio = id_servicio
        self.nombre_servicio = nombre_servicio
        self.descripcion_servicio = descripcion_servicio
        self.precio_servicio = precio_servicio

    def to_JSON(self):
        return{
            "idservicio": self.id_servicio,
            "nombre": self.nombre_servicio,
            "descripcion": self.descripcion_servicio,
            "precio": self.precio_servicio,
        } 