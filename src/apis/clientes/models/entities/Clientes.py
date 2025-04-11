from utils.DateFormat import DateFormat

class Cliente:
    def __init__(self, id_cliente, nombre_cliente, apellido_cliente, documento_cliente, correo_cliente, telefono_cliente):
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.apellido_cliente = apellido_cliente
        self.documento_cliente = documento_cliente
        self.correo_cliente = correo_cliente
        self.telefono_cliente = telefono_cliente

    def to_JSON(self):
        return{
            "idcliente": self.id_cliente,
            "nombre": self.nombre_cliente,
            "apellido": self.apellido_cliente,
            "documento": self.documento_cliente,
            "correo": self.correo_cliente,
            "telefono": self.telefono_cliente,
        } 