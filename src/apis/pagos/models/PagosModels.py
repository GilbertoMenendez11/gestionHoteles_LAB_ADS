from database.database import get_connection
from .entities.Pagos import Pago

class PagoModel:
    #Si queremos mostrar los pagos
    @classmethod
    def get_all_pagos(cls):
        try:
            connection = get_connection()
            pagos_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idpago, monto, fechapago, metodopago, idfactura
                    FROM pagos
                    ORDER BY monto ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    pago = Pago(
                        id_pago=row[0],
                        monto_pago=row[1],
                        fechapago_pago=row[2],
                        metodopago_pago=row[3],
                        idfactura_pago=row[4]
                    )
                    pagos_list.append(pago.to_JSON())
            connection.close()
            return pagos_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_pago_by_id(cls, pago_id):
        try:
            connection = get_connection()
            pago_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idpago, monto, fechapago, metodopago, idfactura
                FROM pagos
                WHERE idpago = %s""", (pago_id,))
                row = cursor.fetchone()
                if row is not None:
                    pago = Pago(
                     id_pago=row[0],
                        monto_pago=row[1],
                        fechapago_pago=row[2],
                        metodopago_pago=row[3],
                        idfactura_pago=row[4]
                    )
                    pago_json = pago.to_JSON()
            connection.close()
            return pago_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar pagos
    @classmethod
    def add_pago(cls, pago: Pago):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO pagos (
                    idpago, monto, fechapago, metodopago, idfactura)
                    VALUES (%s,%s,%s,%s,%s)""",
                    (   pago.id_pago,
                        pago.monto_pago,
                        pago.fechapago_pago,
                        pago.metodopago_pago,
                        pago.idfactura_pago)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un pago
    @classmethod
    def update_pago(cls, pago:Pago):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE pagos
                    SET monto = %s,
                    fechapago = %s,
                    metodopago = %s,
                    idfactura = %s
                    WHERE idpago = %s
                """,(
                    pago.monto_pago,
                    pago.fechapago_pago,
                    pago.metodopago_pago,
                    pago.idfactura_pago,
                    pago.id_pago
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_pago(cls, pago: Pago):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM pagos
                    WHERE idpago = %s
                """, (pago.id_pago,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)