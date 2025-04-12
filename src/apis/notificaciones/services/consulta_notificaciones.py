from database.database import get_connection

def get_notificacion_data(cliente_id):
    connection = get_connection()
    query = """ SELECT idcliente, nombre, apellido, documento, correo, telefono
            FROM clientes WHERE idcliente = %s"""
    result = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (cliente_id,))
            rows = cursor.fetchall()
            for row in rows:
                result.append({
                    "nombre_cliente": row[1],
                    "apellido_cliente": row[2],
                    "documento_cliente": row[3],
                    "correo_cliente": row[4],
                    "telefono_cliente": row[5]
                })
    except Exception as e:
        raise Exception(f"Error al ejecutar get_notificacion_data: {str(e)}")
    finally:
        connection.close()
    return result