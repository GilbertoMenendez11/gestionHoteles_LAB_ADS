from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.LimpiezasModels import LimpiezaModel
from ..models.entities.Limpiezas import Limpieza

main = Blueprint('limpiezas_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_limpiezas():
    try:
        limpiezas = LimpiezaModel.get_all_limpiezas()
        if limpiezas:
            return jsonify(limpiezas), 200
        else:
            return jsonify({"message": "No se encontraron limpiezas"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_limpieza_by_id(id):
    try:
        limpieza = LimpiezaModel.get_limpieza_by_id(id)
        if limpieza:
            return jsonify(limpieza)
        else:
            return jsonify({"error": "limpieza no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_limpieza():
    try:
        data = request.get_json()
        required_fields = ['fecha_limpieza', 'observaciones_limpieza', 'idhabitacion_limpieza', 'idempleado_limpieza']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        limpieza_id = str(uuid.uuid4())
        limpieza = Limpieza(
            id_limpieza=limpieza_id,
            fecha_limpieza=data.get('fecha_limpieza'),
            observaciones_limpieza=data.get('observaciones_limpieza'),
            idhabitacion_limpieza=data.get('idhabitacion_limpieza'),
            idempleado_limpieza=data.get('idempleado_limpieza')
        )
        LimpiezaModel.add_limpieza(limpieza)
        return jsonify({"message": "limpieza agregado", "id": limpieza_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_limpieza(id):
    try:
        data = request.get_json()
        existing_limpieza = LimpiezaModel.get_limpieza_by_id(id)
        if not existing_limpieza:
            return jsonify({"error": "limpieza no encontrado"}), 404
        required_fields = ['fecha_limpieza', 'observaciones_limpieza','idhabitacion_limpieza', 'idempleado_limpieza']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        limpieza = Limpieza(
            id_limpieza=id,
            fecha_limpieza=data.get('fecha_limpieza'),
            observaciones_limpieza=data.get('observaciones_limpieza'),
            idhabitacion_limpieza=data.get('idhabitacion_limpieza'),
            idempleado_limpieza=data.get('idempleado_limpieza')
        )
        affected_rows = LimpiezaModel.update_limpieza(limpieza)
        if affected_rows == 1:
            return jsonify({"message": "limpieza actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el limpieza"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_limpieza(id):
    try:
        limpieza = Limpieza(
            id_limpieza=id,
            fecha_limpieza="",
            observaciones_limpieza="",
            idhabitacion_limpieza="",
            idempleado_limpieza=""
        )
        affected_rows = LimpiezaModel.delete_limpieza(limpieza)
        if affected_rows == 1:
            return jsonify({"message": f"limpieza {id} eliminado"}), 200
        else:
            return jsonify({"error": "limpieza no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

