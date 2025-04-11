from utils.DateFormat import DateFormat

class Pago:
    def __init__(self, id_pago, monto_pago, fechapago_pago, metodopago_pago, idfactura_pago):
        self.id_pago = id_pago
        self.monto_pago = monto_pago
        self.fechapago_pago = fechapago_pago
        self.metodopago_pago = metodopago_pago
        self.idfactura_pago = idfactura_pago

    def to_JSON(self):
        return{
            "idpago": self.id_pago,
            "monto": self.monto_pago,
            "fechapago": self.fechapago_pago,
            "metodopago": self.metodopago_pago,
            "idfactura": self.idfactura_pago,
        } 