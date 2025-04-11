from database.database import get_connection
from ..models.entities.Empleados import Empleado

class EmpleadoModel:
    #Si queremos mostrar los empleados
    @classmethod
    def get_all_empleados(cls):
        try:
            connection = get_connection()
            empleados_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idempleado, nombre, apellido, cargo, telefono, idhotel
                    FROM empleados
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    empleado = Empleado(
                        id_empleado=row[0],
                        nombre_empleado=row[1],
                        apellido_empleado=row[2],
                        cargo_empleado=row[3],
                        telefono_empleado=row[4],
                        idhotel_empleado=row[5]
                    )
                    empleados_list.append(empleado.to_JSON())
            connection.close()
            return empleados_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_empleado_by_id(cls, empleado_id):
        try:
            connection = get_connection()
            empleado_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idempleado, nombre, apellido, cargo, telefono, idhotel
                FROM empleados
                WHERE idempleado = %s""", (empleado_id,))
                row = cursor.fetchone()
                if row is not None:
                    empleado = Empleado(
                     id_empleado=row[0],
                        nombre_empleado=row[1],
                        apellido_empleado=row[2],
                        cargo_empleado=row[3],
                        telefono_empleado=row[4],
                        idhotel_empleado=row[5]
                    )
                    empleado_json = empleado.to_JSON()
            connection.close()
            return empleado_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar empleados
    @classmethod
    def add_empleado(cls, empleado: Empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO empleados (
                    idempleado, nombre, apellido, cargo, telefono, idhotel)
                    VALUES (%s,%s,%s,%s,%s,%s)""",
                    (   empleado.id_empleado,
                        empleado.nombre_empleado,
                        empleado.apellido_empleado,
                        empleado.cargo_empleado,
                        empleado.telefono_empleado,
                        empleado.idhotel_empleado)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un empleado
    @classmethod
    def update_empleado(cls, empleado:Empleado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE empleados
                    SET nombre = %s,
                    apellido = %s,
                    cargo = %s,
                    telefono = %s,
                    idhotel = %s
                    WHERE idempleado = %s
                """,(
                    empleado.nombre_empleado,
                    empleado.apellido_empleado,
                    empleado.cargo_empleado,
                    empleado.telefono_empleado,
                    empleado.idhotel_empleado,
                    empleado.id_empleado
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_empleado(cls, empleado: Empleado):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM empleados
                    WHERE idempleado = %s
                """, (empleado.id_empleado,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)