from database.database import get_connection
from .entities.Telefonos import Telefono

class TelefonoModel:
    #Si queremos mostrar los telefonos
    @classmethod
    def get_all_telefono(cls):
        try:
            connection = get_connection()
            telefono_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id_telefono, nombre, numero_telefono, fecha_creacion
                    FROM telefonos
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    telefono = Telefono(
                        id_telefono=row[0],
                        nombre_telefono=row[1],
                        numero_telefono=row[2],
                        fecha_creacion_telefono=row[3]
                    )
                    telefono_list.append(telefono.to_JSON())
            connection.close()
            return telefono_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_telefono_by_id(cls, telefono_id):
        try:
            connection = get_connection()
            telefono_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT id_telefono, nombre, numero_telefono, fecha_creacion
                FROM telefonos
                WHERE id_telefono = %s""", (telefono_id,))
                row = cursor.fetchone()
                if row is not None:
                    telefono = Telefono(
                        id_telefono=row[0],
                        nombre_telefono=row[1],
                        numero_telefono=row[2],
                        fecha_creacion_telefono=row[3]
                    )
                    telefono_json = telefono.to_JSON()
            connection.close()
            return telefono_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar un telefono
    @classmethod
    def add_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO telefonos (
                    id_telefono, nombre, numero_telefono, fecha_creacion)
                    VALUES (%s,%s,%s,%s)""",
                    (   telefono.id_telefono,
                        telefono.nombre_telefono,
                        telefono.numero_telefono,
                        telefono.fecha_creacion_telefono
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un telefono
    @classmethod
    def update_telefono(cls, telefono: Telefono):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE telefonos
                    SET nombre = %s,
                    numero_telefono = %s,
                    fecha_creacion = %s
                    WHERE id_telefono = %s
                """,(
                    telefono.nombre_telefono,
                    telefono.numero_telefono,
                    telefono.fecha_creacion_telefono,
                    telefono.id_telefono
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_telefono(cls, telefono: Telefono):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM telefonos
                    WHERE id_telefono = %s
                """, (telefono.id_telefono,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)