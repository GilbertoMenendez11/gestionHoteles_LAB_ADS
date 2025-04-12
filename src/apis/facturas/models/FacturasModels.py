from database.database import get_connection
from .entities.Facturas import Factura

class FacturaModel:
    #Si queremos mostrar las facturas
    @classmethod
    def get_all_factura(cls):
        try:
            connection = get_connection()
            facturas_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idfactura, fechaemision, total, idservicio, idreserva
                    FROM facturas
                    ORDER BY fechaemision ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    factura = Factura(
                        id_factura=row[0],
                        fechaemision_factura=row[1],
                        total_factura=row[2],
                        idservicio_factura=row[3],
                        idreserva_factura=row[4]
                    )
                    facturas_list.append(factura.to_JSON())
            connection.close()
            return facturas_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_factura_by_id(cls, factura_id):
        try:
            connection = get_connection()
            factura_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idfactura, fechaemision, total, idservicio, idreserva
                FROM facturas
                WHERE idfactura = %s""", (factura_id,))
                row = cursor.fetchone()
                if row is not None:
                    factura = Factura(
                        id_factura=row[0],
                        fechaemision_factura=row[1],
                        total_factura=row[2],
                        idservicio_factura=row[3],
                        idreserva_factura=row[4]
                    )
                    factura_json = factura.to_JSON()
            connection.close()
            return factura_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar una factura
    @classmethod
    def add_factura(cls, factura: Factura):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO facturas (
                    idfactura, fechaemision, total, idservicio, idreserva)
                    VALUES (%s,%s,%s,%s,%s)""",
                    (   factura.id_factura,
                        factura.fechaemision_factura,
                        factura.total_factura,
                        factura.idservicio_factura,
                        factura.idreserva_factura
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un cliente
    @classmethod
    def update_factura(cls, factura: Factura):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE facturas
                    SET fechaemision = %s,
                    total = %s,
                    idservicio = %s,
                    idreserva = %s
                    WHERE idfactura = %s
                """,(
                    factura.fechaemision_factura,
                    factura.total_factura,
                    factura.idservicio_factura,
                    factura.idreserva_factura,
                    factura.id_factura
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_factura(cls, factura: Factura):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM facturas
                    WHERE idfactura = %s
                """, (factura.id_factura,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)