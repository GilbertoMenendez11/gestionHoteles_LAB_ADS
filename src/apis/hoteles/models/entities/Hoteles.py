from utils.DateFormat import DateFormat

class Hotel:
    def __init__(self, id_hotel, nombre_hotel, direccion_hotel, telefono_hotel, correo_hotel, categoria_hotel):
        self.id_hotel = id_hotel
        self.nombre_hotel = nombre_hotel
        self.direccion_hotel = direccion_hotel
        self.telefono_hotel = telefono_hotel
        self.correo_hotel = correo_hotel
        self.categoria_hotel = categoria_hotel

    def to_JSON(self):
        return{
            "idhotel": self.id_hotel,
            "nombre": self.nombre_hotel,
            "direccion": self.direccion_hotel,
            "telefono": self.telefono_hotel,
            "correo": self.correo_hotel,
            "categoria": self.categoria_hotel,
        } 