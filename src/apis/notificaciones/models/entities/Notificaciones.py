from utils.DateFormat import DateFormat

class Notificacion:
    def __init__(self, id_notificacion, id_cliente, fecha_envio_notificacion, estado_notificacion):
        self.id_notificacion = id_notificacion
        self.id_cliente = id_cliente
        self.fecha_envio_notificacion = DateFormat.convert_date(fecha_envio_notificacion)
        self.estado_notificacion = estado_notificacion

    def to_JSON(self):
        return{
            "id": self.id_notificacion,
            "id_cliente": self.id_cliente,
            "fecha_envio": self.fecha_envio_notificacion,
            "estado": self.estado_notificacion
        } 