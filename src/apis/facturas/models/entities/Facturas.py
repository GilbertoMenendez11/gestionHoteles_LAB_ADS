from utils.DateFormat import DateFormat

class Factura:
    def __init__(self, id_factura, fechaemision_factura, total_factura, idservicio_factura, idreserva_factura):
        self.id_factura = id_factura
        self.fechaemision_factura = DateFormat.convert_date(fechaemision_factura)
        self.total_factura = total_factura
        self.idservicio_factura = idservicio_factura
        self.idreserva_factura = idreserva_factura

    def to_JSON(self):
        return{
            "idfactura": self.id_factura,
            "fechaemision": self.fechaemision_factura,
            "total": self.total_factura,
            "idservicio": self.idservicio_factura,
            "idreserva": self.idreserva_factura
        } 