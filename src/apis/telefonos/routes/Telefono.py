from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.TelefonosModels import TelefonoModel
from ..models.entities.Telefonos import Telefono
from datetime import datetime

main = Blueprint('telefono_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_telefono():
    try:
        telefono = TelefonoModel.get_all_telefono()
        if telefono:
            return jsonify(telefono), 200
        else:
            return jsonify({"message": "No se encontraron el telefono"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_telefono_by_id(id):
    try:
        telefono = TelefonoModel.get_telefono_by_id(id)
        if telefono:
            return jsonify(telefono)
        else:
            return jsonify({"error": "Telefono no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_telefono():
    try:
        data = request.get_json()
        required_fields = ['nombre_telefono', 'numero_telefono', 'fecha_creacion_telefono']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        telefono_id = str(uuid.uuid4())
        #Convertir la fecha en formato dd/mm/yyyy
        fecha_creacion_str = data.get('telefono_creacion_telefono',
                                    datetime.now().strftime('%d/%m/%Y'))
        fecha_creacion_obj = datetime.strptime(fecha_creacion_str, '%d/%m/%Y')
        telefono = Telefono(
            id_telefono=telefono_id,
            nombre_telefono=data.get('nombre_telefono'),
            numero_telefono=data.get('numero_telefono'),
            fecha_creacion_telefono=fecha_creacion_obj
        )
        TelefonoModel.add_telefono(telefono)
        return jsonify({"message": "Telefono agregado", "id": telefono_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_telefono(id):
    try:
        data = request.get_json()
        existing_telefono = TelefonoModel.get_telefono_by_id(id)
        if not existing_telefono:
            return jsonify({"error": "Telefono no encontrado"}), 404
        required_fields = ['nombre_telefono', 'numero_telefono', 'fecha_creacion_telefono']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        fecha_creacion_srt = data.get('fecha_creacion_telefono')
        fecha_creacion_obj = datetime.strptime(fecha_creacion_srt, '%d/%m/%Y')
        telefono = Telefono(
            id_telefono=id,
            nombre_telefono=data.get('nombre_telefono'),
            numero_telefono=data.get('numero_telefono'),
            fecha_creacion_telefono=fecha_creacion_obj
        )
        affected_rows = TelefonoModel.update_telefono(telefono)
        if affected_rows == 1:
            return jsonify({"message": "Telefono actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el Telefono"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_telefono(id):
    try:
        telefono = Telefono(
            id_telefono=id,
            nombre_telefono="",
            numero_telefono="",
            fecha_creacion_telefono=datetime.now()
        )
        affected_rows = TelefonoModel.delete_telefono(telefono)
        if affected_rows == 1:
            return jsonify({"message": f"Telefono {id} eliminada"}), 200
        else:
            return jsonify({"error": "Telefono no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

