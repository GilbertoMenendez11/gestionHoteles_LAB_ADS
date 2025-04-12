from database.database import get_connection
from ..models.entities.Habitaciones import Habitacion

class habitacionModel:
    #Si queremos mostrar los habitaiones
    @classmethod
    def get_all_habitaiones(cls):
        try:
            connection = get_connection()
            habitaiones_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idhabitacion, numero, tipo, cargo, precionoche, idhotel
                    FROM habitaiones
                    ORDER BY numero ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    habitacion = Habitacion(
                        id_habitacion=row[0],
                        numero_habitacion=row[1],
                        tipo_habitacion=row[2],
                        cargo_habitacion=row[3],
                        precionoche_habitacion=row[4],
                        idhotel_habitacion=row[5]
                    )
                    habitaiones_list.append(habitacion.to_JSON())
            connection.close()
            return habitaiones_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_habitacion_by_id(cls, habitacion_id):
        try:
            connection = get_connection()
            habitacion_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idhabitacion, numero, tipo, cargo, precionoche, idhotel
                FROM habitaiones
                WHERE idhabitacion = %s""", (habitacion_id,))
                row = cursor.fetchone()
                if row is not None:
                    habitacion = Habitacion(
                     id_habitacion=row[0],
                        numero_habitacion=row[1],
                        tipo_habitacion=row[2],
                        cargo_habitacion=row[3],
                        precionoche_habitacion=row[4],
                        idhotel_habitacion=row[5]
                    )
                    habitacion_json = habitacion.to_JSON()
            connection.close()
            return habitacion_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar habitaiones
    @classmethod
    def add_habitacion(cls, habitacion: Habitacion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO habitaiones (
                    idhabitacion, numero, tipo, cargo, precionoche, idhotel)
                    VALUES (%s,%s,%s,%s,%s,%s)""",
                    (   habitacion.id_habitacion,
                        habitacion.numero_habitacion,
                        habitacion.tipo_habitacion,
                        habitacion.cargo_habitacion,
                        habitacion.precionoche_habitacion,
                        habitacion.idhotel_habitacion)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un habitacion
    @classmethod
    def update_habitacion(cls, habitacion:Habitacion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE habitaiones
                    SET numero = %s,
                    tipo = %s,
                    cargo = %s,
                    precionoche = %s,
                    idhotel = %s
                    WHERE idhabitacion = %s
                """,(
                    habitacion.numero_habitacion,
                    habitacion.tipo_habitacion,
                    habitacion.cargo_habitacion,
                    habitacion.precionoche_habitacion,
                    habitacion.idhotel_habitacion,
                    habitacion.id_habitacion
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_habitacion(cls, habitacion: Habitacion):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM habitaiones
                    WHERE idhabitacion = %s
                """, (habitacion.id_habitacion,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)