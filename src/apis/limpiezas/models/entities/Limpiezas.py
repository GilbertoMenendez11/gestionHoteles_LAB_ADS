from utils.DateFormat import DateFormat

class Limpieza:
    def __init__(self, id_limpieza, fecha_limpieza, observaciones_limpieza, idhabitacion_limpieza, idempleado_limpieza):
        self.id_limpieza = id_limpieza
        self.fecha_limpieza = fecha_limpieza
        self.observaciones_limpieza = observaciones_limpieza
        self.idhabitacion_limpieza = idhabitacion_limpieza
        self.idempleado_limpieza = idempleado_limpieza

    def to_JSON(self):
        return{
            "idlimpieza": self.id_limpieza,
            "fecha": self.fecha_limpieza,
            "observaciones": self.observaciones_limpieza,
            "idhabitacion": self.idhabitacion_limpieza,
            "idempleado": self.idempleado_limpieza,
        } 