from database.database import get_connection
from ..models.entities.Habitaciones import Habitacion

class HabitacionModel:
    #Si queremos mostrar los habitaciones
    @classmethod
    def get_all_habitaciones(cls):
        try:
            connection = get_connection()
            habitaciones_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idhabitacion, numero, tipo, precionoche, estado, idhotel
                    FROM habitaciones
                    ORDER BY numero ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    habitacion = Habitacion(
                        id_habitacion=row[0],
                        numero_habitacion=row[1],
                        tipo_habitacion=row[2],
                        precionoche_habitacion=row[3],
                        estado_habitacion=row[4],
                        idhotel_habitacion=row[5]
                    )
                    habitaciones_list.append(habitacion.to_JSON())
            connection.close()
            return habitaciones_list
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
                SELECT idhabitacion, numero, tipo, precionoche, estado, idhotel
                FROM habitaciones
                WHERE idhabitacion = %s""", (habitacion_id,))
                row = cursor.fetchone()
                if row is not None:
                    habitacion = Habitacion(
                     id_habitacion=row[0],
                        numero_habitacion=row[1],
                        tipo_habitacion=row[2],
                        precionoche_habitacion=row[3],
                        estado_habitacion=row[4],
                        idhotel_habitacion=row[5]
                    )
                    habitacion_json = habitacion.to_JSON()
            connection.close()
            return habitacion_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar habitaciones
    @classmethod
    def add_habitacion(cls, habitacion: Habitacion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO habitaciones (
                    idhabitacion, numero, tipo, precionoche, estado, idhotel)
                    VALUES (%s,%s,%s,%s,%s,%s)""",
                    (   habitacion.id_habitacion,
                        habitacion.numero_habitacion,
                        habitacion.tipo_habitacion,
                        habitacion.precionoche_habitacion,
                        habitacion.estado_habitacion,
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
                    UPDATE habitaciones
                    SET numero = %s,
                    tipo = %s,
                    precionoche = %s,
                    estado = %s,
                    idhotel = %s
                    WHERE idhabitacion = %s
                """,(
                    habitacion.numero_habitacion,
                    habitacion.tipo_habitacion,
                    habitacion.precionoche_habitacion,
                    habitacion.estado_habitacion,
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
                    DELETE FROM habitaciones
                    WHERE idhabitacion = %s
                """, (habitacion.id_habitacion,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)