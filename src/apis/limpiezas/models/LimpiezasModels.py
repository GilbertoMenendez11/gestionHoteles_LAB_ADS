from database.database import get_connection
from ..models.entities.Limpiezas import Limpieza

class LimpiezaModel:
    #Si queremos mostrar los limpiezas
    @classmethod
    def get_all_limpiezas(cls):
        try:
            connection = get_connection()
            limpiezas_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idlimpieza, fecha, observaciones, idhabitacion, idempleado
                    FROM limpiezas
                    ORDER BY fecha ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    limpieza = Limpieza(
                        id_limpieza=row[0],
                        fecha_limpieza=row[1],
                        observaciones_limpieza=row[2],
                        idhabitacion_limpieza=row[3],
                        idempleado_limpieza=row[4]
                    )
                    limpiezas_list.append(limpieza.to_JSON())
            connection.close()
            return limpiezas_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_limpieza_by_id(cls, limpieza_id):
        try:
            connection = get_connection()
            limpieza_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idlimpieza, fecha, observaciones, idhabitacion, idempleado
                FROM limpiezas
                WHERE idlimpieza = %s""", (limpieza_id,))
                row = cursor.fetchone()
                if row is not None:
                    limpieza = Limpieza(
                     id_limpieza=row[0],
                        fecha_limpieza=row[1],
                        observaciones_limpieza=row[2],
                        idhabitacion_limpieza=row[3],
                        idempleado_limpieza=row[4]
                    )
                    limpieza_json = limpieza.to_JSON()
            connection.close()
            return limpieza_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar limpiezas
    @classmethod
    def add_limpieza(cls, limpieza: Limpieza):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO limpiezas (
                    idlimpieza, fecha, observaciones, idhabitacion, idempleado)
                    VALUES (%s,%s,%s,%s,%s)""",
                    (   limpieza.id_limpieza,
                        limpieza.fecha_limpieza,
                        limpieza.observaciones_limpieza,
                        limpieza.idhabitacion_limpieza,
                        limpieza.idempleado_limpieza)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un limpieza
    @classmethod
    def update_limpieza(cls, limpieza:Limpieza):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE limpiezas
                    SET fecha = %s,
                    observaciones = %s,
                    idhabitacion = %s,
                    idempleado = %s
                    WHERE idlimpieza = %s
                """,(
                    limpieza.fecha_limpieza,
                    limpieza.observaciones_limpieza,
                    limpieza.idhabitacion_limpieza,
                    limpieza.idempleado_limpieza,
                    limpieza.id_limpieza
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_limpieza(cls, limpieza: Limpieza):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM limpiezas
                    WHERE idlimpieza = %s
                """, (limpieza.id_limpieza,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)