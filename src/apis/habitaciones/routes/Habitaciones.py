from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.HabitacionesModels import HabitacionModel
from ..models.entities.Habitaciones import Habitacion

main = Blueprint('empleados_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_empleados():
    try:
        empleados = HabitacionModel.get_all_empleados()
        if empleados:
            return jsonify(empleados), 200
        else:
            return jsonify({"message": "No se encontraron empleados"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_empleado_by_id(id):
    try:
        empleado = HabitacionModel.get_empleado_by_id(id)
        if empleado:
            return jsonify(empleado)
        else:
            return jsonify({"error": "empleado no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_empleado():
    try:
        data = request.get_json()
        required_fields = ['nombre_empleado', 'apellido_empleado', 'cargo_empleado', 'telefono_empleado', 'idhotel_empleado']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        empleado_id = str(uuid.uuid4())
        empleado = Habitacion(
            id_empleado=empleado_id,
            nombre_empleado=data.get('nombre_empleado'),
            apellido_empleado=data.get('apellido_empleado'),
            cargo_empleado=data.get('cargo_empleado'),
            telefono_empleado=data.get('telefono_empleado'),
            idhotel_empleado=data.get('idhotel_empleado')
        )
        HabitacionModel.add_empleado(empleado)
        return jsonify({"message": "Empleado agregado", "id": empleado_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_empleado(id):
    try:
        data = request.get_json()
        existing_empleado = HabitacionModel.get_empleado_by_id(id)
        if not existing_empleado:
            return jsonify({"error": "Empleado no encontrado"}), 404
        required_fields = ['nombre_empleado', 'apellido_empleado', 'cargo_empleado','telefono_empleado', 'idhotel_empleado']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        empleado = Habitacion(
            id_empleado=id,
            nombre_empleado=data.get('nombre_empleado'),
            apellido_empleado=data.get('apellido_empleado'),
            cargo_empleado=data.get('cargo_empleado'),
            telefono_empleado=data.get('telefono_empleado'),
            idhotel_empleado=data.get('idhotel_empleado')
        )
        affected_rows = HabitacionModel.update_empleado(empleado)
        if affected_rows == 1:
            return jsonify({"message": "Empleado actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el empleado"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_empleado(id):
    try:
        empleado = Habitacion(
            id_empleado=id,
            nombre_empleado="",
            apellido_empleado="",
            cargo_empleado="",
            telefono_empleado="",
            idhotel_empleado=""
        )
        affected_rows = HabitacionModel.delete_empleado(empleado)
        if affected_rows == 1:
            return jsonify({"message": f"Empleado {id} eliminado"}), 200
        else:
            return jsonify({"error": "Empleado no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

