from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.ServiciosAdicionalesModels import ServiciosAdicionalesModel
from ..models.entities.ServiciosAdicionales import Servicio

main = Blueprint('servicios_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_servicios():
    try:
        servicios = ServiciosAdicionalesModel.get_all_servicios()
        if servicios:
            return jsonify(servicios), 200
        else:
            return jsonify({"message": "No se encontraron servicios"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_servicio_by_id(id):
    try:
        servicio = ServiciosAdicionalesModel.get_servicio_by_id(id)
        if servicio:
            return jsonify(servicio)
        else:
            return jsonify({"error": "servicio no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_servicio():
    try:
        data = request.get_json()
        required_fields = ['nombre_servicio', 'descripcion_servicio', 'precio_servicio']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        servicio_id = str(uuid.uuid4())
        servicio = Servicio(
            id_servicio=servicio_id,
            nombre_servicio=data.get('nombre_servicio'),
            descripcion_servicio=data.get('descripcion_servicio'),
            precio_servicio=data.get('precio_servicio')
        )
        ServiciosAdicionalesModel.add_servicio(servicio)
        return jsonify({"message": "servicio agregado", "id": servicio_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_servicio(id):
    try:
        data = request.get_json()
        existing_servicio = ServiciosAdicionalesModel.get_servicio_by_id(id)
        if not existing_servicio:
            return jsonify({"error": "servicio no encontrado"}), 404
        required_fields = ['nombre_servicio', 'descripcion_servicio', 'precio_servicio']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        servicio = Servicio(
            id_servicio=id,
            nombre_servicio=data.get('nombre_servicio'),
            descripcion_servicio=data.get('descripcion_servicio'),
            precio_servicio=data.get('precio_servicio')
        )
        affected_rows = ServiciosAdicionalesModel.update_servicio(servicio)
        if affected_rows == 1:
            return jsonify({"message": "servicio actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el servicio"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_servicio(id):
    try:
        servicio = Servicio(
            id_servicio=id,
            nombre_servicio="",
            descripcion_servicio="",
            precio_servicio=""
        )
        affected_rows = ServiciosAdicionalesModel.delete_servicio(servicio)
        if affected_rows == 1:
            return jsonify({"message": f"servicio {id} eliminado"}), 200
        else:
            return jsonify({"error": "servicio no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

