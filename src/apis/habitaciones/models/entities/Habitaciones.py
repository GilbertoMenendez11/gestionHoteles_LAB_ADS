from utils.DateFormat import DateFormat

class Habitacion:
    def __init__(self, id_habitacion, numero_habitacion, tipo_habitacion, precionoche_habitacion, estado_habitacion, idhotel_habitacion):
        self.id_habitacion = id_habitacion
        self.numero_habitacion = numero_habitacion
        self.tipo_habitacion = tipo_habitacion
        self.precionoche_habitacion = precionoche_habitacion
        self.estado_habitacion = estado_habitacion
        self.idhotel_habitacion = idhotel_habitacion

    def to_JSON(self):
        return{
            "idhabitacion": self.id_habitacion,
            "numero": self.numero_habitacion,
            "tipo": self.tipo_habitacion,
            "precionoche": self.precionoche_habitacion,
            "estado": self.estado_habitacion,
            "idhotel": self.idhotel_habitacion,
        } 