from database.database import get_connection
from ..models.entities.Hoteles import Hotel

class HotelModel:
    #Si queremos mostrar los hoteles
    @classmethod
    def get_all_hoteles(cls):
        try:
            connection = get_connection()
            hoteles_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idhotel, nombre, direccion, telefono, correo, categoria
                    FROM hoteles
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    hotel = Hotel(
                        id_hotel=row[0],
                        nombre_hotel=row[1],
                        direccion_hotel=row[2],
                        telefono_hotel=row[3],
                        correo_hotel=row[4],
                        categoria_hotel=row[5]
                    )
                    hoteles_list.append(hotel.to_JSON())
            connection.close()
            return hoteles_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_hotel_by_id(cls, hotel_id):
        try:
            connection = get_connection()
            hotel_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idhotel, nombre, direccion, telefono, correo, categoria
                FROM hoteles
                WHERE idhotel = %s""", (hotel_id,))
                row = cursor.fetchone()
                if row is not None:
                    hotel = Hotel(
                     id_hotel=row[0],
                        nombre_hotel=row[1],
                        direccion_hotel=row[2],
                        telefono_hotel=row[3],
                        correo_hotel=row[4],
                        categoria_hotel=row[5]
                    )
                    hotel_json = hotel.to_JSON()
            connection.close()
            return hotel_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar hotels
    @classmethod
    def add_hotel(cls, hotel: Hotel):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO hoteles (
                    idhotel, nombre, direccion, telefono, correo, categoria)
                    VALUES (%s,%s,%s,%s,%s,%s)""",
                    (   hotel.id_hotel,
                        hotel.nombre_hotel,
                        hotel.direccion_hotel,
                        hotel.telefono_hotel,
                        hotel.correo_hotel,
                        hotel.categoria_hotel)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un hotel
    @classmethod
    def update_hotel(cls, hotel:Hotel):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE hoteles
                    SET nombre = %s,
                    direccion = %s,
                    telefono = %s,
                    correo = %s,
                    categoria = %s
                    WHERE idhotel = %s
                """,(
                    hotel.nombre_hotel,
                    hotel.direccion_hotel,
                    hotel.telefono_hotel,
                    hotel.correo_hotel,
                    hotel.categoria_hotel,
                    hotel.id_hotel
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_hotel(cls, hotel: Hotel):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM hoteles
                    WHERE idhotel = %s
                """, (hotel.id_hotel,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)