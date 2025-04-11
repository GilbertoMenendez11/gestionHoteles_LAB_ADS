from utils.DateFormat import DateFormat

class Reserva:
    def __init__(self, id_reserva, fechainicio_reserva, fechafin_reserva, estado_reserva, idcliente_reserva, idhabitacion_reserva):
        self.id_reserva = id_reserva
        self.fechainicio_reserva = fechainicio_reserva
        self.fechafin_reserva = fechafin_reserva
        self.estado_reserva = estado_reserva
        self.idcliente_reserva = idcliente_reserva
        self.idhabitacion_reserva = idhabitacion_reserva

    def to_JSON(self):
        return{
            "idreserva": self.id_reserva,
            "fechainicio": self.fechainicio_reserva,
            "fechafin": self.fechafin_reserva,
            "estado": self.estado_reserva,
            "idcliente": self.idcliente_reserva,
            "idhabitacion": self.idhabitacion_reserva,
        } 