from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.HabitacionesModels import HabitacionModel
from ..models.entities.Habitaciones import Habitacion

main = Blueprint('habitaciones_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_habitaciones():
    try:
        habitaciones = HabitacionModel.get_all_habitaciones()
        if habitaciones:
            return jsonify(habitaciones), 200
        else:
            return jsonify({"message": "No se encontraron habitaciones"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_habitacion_by_id(id):
    try:
        habitacion = HabitacionModel.get_habitacion_by_id(id)
        if habitacion:
            return jsonify(habitacion)
        else:
            return jsonify({"error": "habitacion no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_habitacion():
    try:
        data = request.get_json()
        required_fields = ['numero_habitacion', 'tipo_habitacion', 'precionoche_habitacion', 'estado_habitacion', 'idhotel_habitacion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        habitacion_id = str(uuid.uuid4())
        habitacion = Habitacion(
            id_habitacion=habitacion_id,
            numero_habitacion=data.get('numero_habitacion'),
            tipo_habitacion=data.get('tipo_habitacion'),
            precionoche_habitacion=data.get('precionoche_habitacion'),
            estado_habitacion=data.get('estado_habitacion'),
            idhotel_habitacion=data.get('idhotel_habitacion')
        )
        HabitacionModel.add_habitacion(habitacion)
        return jsonify({"message": "habitacion agregado", "id": habitacion_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_habitacion(id):
    try:
        data = request.get_json()
        existing_habitacion = HabitacionModel.get_habitacion_by_id(id)
        if not existing_habitacion:
            return jsonify({"error": "habitacion no encontrado"}), 404
        required_fields = ['numero_habitacion', 'tipo_habitacion', 'precionoche_habitacion','estado_habitacion', 'idhotel_habitacion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        habitacion = Habitacion(
            id_habitacion=id,
            numero_habitacion=data.get('numero_habitacion'),
            tipo_habitacion=data.get('tipo_habitacion'),
            precionoche_habitacion=data.get('precionoche_habitacion'),
            estado_habitacion=data.get('estado_habitacion'),
            idhotel_habitacion=data.get('idhotel_habitacion')
        )
        affected_rows = HabitacionModel.update_habitacion(habitacion)
        if affected_rows == 1:
            return jsonify({"message": "habitacion actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el habitacion"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_habitacion(id):
    try:
        habitacion = Habitacion(
            id_habitacion=id,
            numero_habitacion="",
            tipo_habitacion="",
            precionoche_habitacion="",
            estado_habitacion="",
            idhotel_habitacion=""
        )
        affected_rows = HabitacionModel.delete_habitacion(habitacion)
        if affected_rows == 1:
            return jsonify({"message": f"habitacion {id} eliminado"}), 200
        else:
            return jsonify({"error": "habitacion no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

