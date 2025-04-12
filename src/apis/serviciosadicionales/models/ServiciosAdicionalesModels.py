from database.database import get_connection
from .entities.ServiciosAdicionales import Servicio

class ServiciosAdicionalesModel:
    #Si queremos mostrar los servicios
    @classmethod
    def get_all_servicios(cls):
        try:
            connection = get_connection()
            servicios_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idservicio, nombre, descripcion, precio
                    FROM serviciosadicionales
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    servicio = Servicio(
                        id_servicio=row[0],
                        nombre_servicio=row[1],
                        descripcion_servicio=row[2],
                        precio_servicio=row[3]
                    )
                    servicios_list.append(servicio.to_JSON())
            connection.close()
            return servicios_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_servicio_by_id(cls, servicio_id):
        try:
            connection = get_connection()
            servicio_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idservicio, nombre, descripcion, precio
                FROM serviciosadicionales
                WHERE idservicio = %s""", (servicio_id,))
                row = cursor.fetchone()
                if row is not None:
                    servicio = Servicio(
                     id_servicio=row[0],
                        nombre_servicio=row[1],
                        descripcion_servicio=row[2],
                        precio_servicio=row[3]
                    )
                    servicio_json = servicio.to_JSON()
            connection.close()
            return servicio_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar servicios
    @classmethod
    def add_servicio(cls, servicio: Servicio):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO serviciosadicionales (
                    idservicio, nombre, descripcion, precio)
                    VALUES (%s,%s,%s,%s)""",
                    (   servicio.id_servicio,
                        servicio.nombre_servicio,
                        servicio.descripcion_servicio,
                        servicio.precio_servicio)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un servicio
    @classmethod
    def update_servicio(cls, servicio:Servicio):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE serviciosadicionales
                    SET nombre = %s,
                    descripcion = %s,
                    precio = %s
                    WHERE idservicio = %s
                """,(
                    servicio.nombre_servicio,
                    servicio.descripcion_servicio,
                    servicio.precio_servicio,
                    servicio.id_servicio
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_servicio(cls, servicio: Servicio):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM serviciosadicionales
                    WHERE idservicio = %s
                """, (servicio.id_servicio,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)