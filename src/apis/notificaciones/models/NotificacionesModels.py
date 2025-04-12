from database.database import get_connection
from .entities.Notificaciones import Notificacion

class NotificacionModel:
    #Si queremos mostrar las notificaciones
    @classmethod
    def get_all_notificacion(cls):
        try:
            connection = get_connection()
            notificacion_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT id, id_cliente, fecha_envio, estado
                    FROM notificaciones
                    ORDER BY id_cliente ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    notificacion = Notificacion(
                        id_notificacion=row[0],
                        id_cliente=row[1],
                        fecha_envio_notificacion=row[2],
                        estado_notificacion=row[3]
                    )
                    notificacion_list.append(notificacion.to_JSON())
            connection.close()
            return notificacion_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_notificacion_by_id(cls, notificacion_id):
        try:
            connection = get_connection()
            notificacion_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT id, id_cliente, fecha_envio, estado
                FROM notificaciones
                WHERE id = %s""", (notificacion_id,))
                row = cursor.fetchone()
                if row is not None:
                    notificacion = Notificacion(
                        id_notificacion=row[0],
                        id_cliente=row[1],
                        fecha_envio_notificacion=row[2],
                        estado_notificacion=row[3]
                    )
                    notificacion_json = notificacion.to_JSON()
            connection.close()
            return notificacion_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar un telefono
    @classmethod
    def add_notificacion(cls, notificacion: Notificacion):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO notificaciones (
                    id, id_cliente, fecha_envio, estado)
                    VALUES (%s,%s,%s,%s)""",
                    (   notificacion.id_notificacion,
                        notificacion.id_cliente,
                        notificacion.fecha_envio_notificacion,
                        notificacion.estado_notificacion
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
