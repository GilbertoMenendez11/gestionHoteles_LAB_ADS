from database.database import get_connection
from .entities.Clientes import Cliente

class ClienteModel:
    #Si queremos mostrar los clientes
    @classmethod
    def get_all_clientes(cls):
        try:
            connection = get_connection()
            clientes_list = []
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT idcliente, nombre, apellido, documento, correo, telefono
                    FROM clientes
                    ORDER BY nombre ASC
                """)
                resultset = cursor.fetchall()
                for row in resultset:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre_cliente=row[1],
                        apellido_cliente=row[2],
                        documento_cliente=row[3],
                        correo_cliente=row[4],
                        telefono_cliente=row[5]
                    )
                    clientes_list.append(cliente.to_JSON())
            connection.close()
            return clientes_list
        except Exception as ex:
            raise Exception(ex)
    #Si queremos hacer una busqueda por id
    @classmethod
    def get_cliente_by_id(cls, cliente_id):
        try:
            connection = get_connection()
            cliente_json = None
            with connection.cursor() as cursor:
                cursor.execute("""
                SELECT idcliente, nombre, apellido, documento, correo, telefono
                FROM clientes
                WHERE idcliente = %s""", (cliente_id,))
                row = cursor.fetchone()
                if row is not None:
                    cliente = Cliente(
                     id_cliente=row[0],
                        nombre_cliente=row[1],
                        apellido_cliente=row[2],
                        documento_cliente=row[3],
                        correo_cliente=row[4],
                        telefono_cliente=row[5]
                    )
                    cliente_json = cliente.to_JSON()
            connection.close()
            return cliente_json
        except Exception as ex:
            raise Exception(ex)
    #Si queremos insertar clientes
    @classmethod
    def add_cliente(cls, cliente: Cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO clientes (
                    idcliente, nombre, apellido, documento, correo, telefono)
                    VALUES (%s,%s,%s,%s,%s,%s)""",
                    (   cliente.id_cliente,
                        cliente.nombre_cliente,
                        cliente.apellido_cliente,
                        cliente.documento_cliente,
                        cliente.correo_cliente,
                        cliente.telefono_cliente)
                )
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
    #Si queremos actualizar un cliente
    @classmethod
    def update_cliente(cls, cliente:Cliente):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE clientes
                    SET nombre = %s,
                    apellido = %s,
                    documento = %s,
                    correo = %s,
                    telefono = %s
                    WHERE idcliente = %s
                """,(
                    cliente.nombre_cliente,
                    cliente.apellido_cliente,
                    cliente.documento_cliente,
                    cliente.correo_cliente,
                    cliente.telefono_cliente,
                    cliente.id_cliente
                ))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as  ex:
            raise Exception(ex)
    #Si queremos Eliminar 
    @classmethod
    def delete_cliente(cls, cliente: Cliente):
        try:
            connection= get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""
                    DELETE FROM clientes
                    WHERE idcliente = %s
                """, (cliente.id_cliente,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)