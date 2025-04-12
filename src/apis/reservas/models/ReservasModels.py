from database.database import get_connection
from .entities.Reservas import Reserva

class ReservaModel:
    #Si queremos mostrar los reservas
    @classmethod
    def get_all_reservas(cls):
        try:
            connection = get_connection()
            reservas_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idreserva, fechainicio, fechafin, estado, idcliente, idhabitacion
                    FROM reservas
                    ORDER BY fechainicio ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    reserva = Reserva(
                        id_reserva=row[0],
                        fechainicio_reserva=row[1],
                        fechafin_reserva=row[2],
                        estado_reserva=row[3],
                        idcliente_reserva=row[4],
                        idhabitacion_reserva=row[5]
                    )
                    reservas_list.append(reserva.to_JSON())
            connection.close()
            return reservas_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_reserva_by_id(cls, reserva_id):
        try:
            connection = get_connection()
            reserva_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idreserva, fechainicio, fechafin, estado, idcliente, idhabitacion
                FROM reservas
                WHERE idreserva = %s""", (reserva_id,))
                row = cursor.fetchone()
                if row is not None:
                    reserva = Reserva(
                     id_reserva=row[0],
                        fechainicio_reserva=row[1],
                        fechafin_reserva=row[2],
                        estado_reserva=row[3],
                        idcliente_reserva=row[4],
                        idhabitacion_reserva=row[5]
                    )
                    reserva_json = reserva.to_JSON()
            connection.close()
            return reserva_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar reservas
    @classmethod
    def add_reserva(cls, reserva: Reserva):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO reservas (
                    idreserva, fechainicio, fechafin, estado, idcliente, idhabitacion)
                    VALUES (%s,%s,%s,%s,%s, %s)""",
                    (   reserva.id_reserva,
                        reserva.fechainicio_reserva,
                        reserva.fechafin_reserva,
                        reserva.estado_reserva,
                        reserva.idcliente_reserva,
                        reserva.idhabitacion_reserva)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un reserva
    @classmethod
    def update_reserva(cls, reserva:Reserva):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE reservas
                    SET fechainicio = %s,
                    fechafin = %s,
                    estado = %s,
                    idcliente = %s,
                    idhabitacion = %s
                    WHERE idreserva = %s
                """,(
                    reserva.fechainicio_reserva,
                    reserva.fechafin_reserva,
                    reserva.estado_reserva,
                    reserva.idcliente_reserva,
                    reserva.idhabitacion_reserva,
                    reserva.id_reserva
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_reserva(cls, reserva: Reserva):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM reservas
                    WHERE idreserva = %s
                """, (reserva.id_reserva,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)