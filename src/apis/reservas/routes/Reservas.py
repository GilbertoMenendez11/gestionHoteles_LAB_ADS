from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.ReservasModels import ReservaModel
from ..models.entities.Reservas import Reserva

main = Blueprint('reservas_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_reservas():
    try:
        reservas = ReservaModel.get_all_reservas()
        if reservas:
            return jsonify(reservas), 200
        else:
            return jsonify({"message": "No se encontraron reservas"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_reserva_by_id(id):
    try:
        reserva = ReservaModel.get_reserva_by_id(id)
        if reserva:
            return jsonify(reserva)
        else:
            return jsonify({"error": "reserva no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_reserva():
    try:
        data = request.get_json()
        required_fields = ['fechainicio_reserva', 'fechafin_reserva', 'estado_reserva', 'idcliente_reserva', 'idhabitacion_reserva']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        reserva_id = str(uuid.uuid4())
        reserva = Reserva(
            id_reserva=reserva_id,
            fechainicio_reserva=data.get('fechainicio_reserva'),
            fechafin_reserva=data.get('fechafin_reserva'),
            estado_reserva=data.get('estado_reserva'),
            idcliente_reserva=data.get('idcliente_reserva'),
            idhabitacion_reserva=data.get('idhabitacion_reserva')
          
        )
        ReservaModel.add_reserva(reserva)
        return jsonify({"message": "reserva agregado", "id": reserva_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_reserva(id):
    try:
        data = request.get_json()
        existing_reserva = ReservaModel.get_reserva_by_id(id)
        if not existing_reserva:
            return jsonify({"error": "reserva no encontrado"}), 404
        required_fields = ['fechainicio_reserva', 'fechafin_reserva','estado_reserva', 'idcliente_reserva', 'idhabitacion_reserva']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        reserva = Reserva(
            id_reserva=id,
            fechainicio_reserva=data.get('fechainicio_reserva'),
            fechafin_reserva=data.get('fechafin_reserva'),
            estado_reserva=data.get('estado_reserva'),
            idcliente_reserva=data.get('idcliente_reserva'),
            idhabitacion_reserva=data.get('idhabitacion_reserva')

        )
        affected_rows = ReservaModel.update_reserva(reserva)
        if affected_rows == 1:
            return jsonify({"message": "reserva actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la reserva"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_reserva(id):
    try:
        reserva = Reserva(
            id_reserva=id,
            fechainicio_reserva="",
            fechafin_reserva="",
            estado_reserva="",
            idcliente_reserva="",
            idhabitacion_reserva=""
        )
        affected_rows = ReservaModel.delete_reserva(reserva)
        if affected_rows == 1:
            return jsonify({"message": f"reserva {id} eliminado"}), 200
        else:
            return jsonify({"error": "reserva no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

