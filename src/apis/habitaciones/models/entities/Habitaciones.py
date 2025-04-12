from utils.DateFormat import DateFormat

class Empleado:
    def __init__(self, id_empleado, nombre_empleado, apellido_empleado, cargo_empleado, telefono_empleado, idhotel_empleado):
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.apellido_empleado = apellido_empleado
        self.cargo_empleado = cargo_empleado
        self.telefono_empleado = telefono_empleado
        self.idhotel_empleado = idhotel_empleado

    def to_JSON(self):
        return{
            "idempleado": self.id_empleado,
            "nombre": self.nombre_empleado,
            "apellido": self.apellido_empleado,
            "cargo": self.cargo_empleado,
            "telefono": self.telefono_empleado,
            "idhotel": self.idhotel_empleado,
        } 