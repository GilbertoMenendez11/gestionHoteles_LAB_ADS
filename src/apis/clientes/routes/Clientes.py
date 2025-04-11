from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.ClientesModels import ClienteModel
from ..models.entities.Clientes import Cliente

main = Blueprint('clientes_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_clientes():
    try:
        clientes = ClienteModel.get_all_clientes()
        if clientes:
            return jsonify(clientes), 200
        else:
            return jsonify({"message": "No se encontraron clientes"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_cliente_by_id(id):
    try:
        cliente = ClienteModel.get_cliente_by_id(id)
        if cliente:
            return jsonify(cliente)
        else:
            return jsonify({"error": "cliente no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_cliente():
    try:
        data = request.get_json()
        required_fields = ['nombre_cliente', 'apellido_cliente', 'documento_cliente', 'correo_cliente', 'telefono_cliente']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        cliente_id = str(uuid.uuid4())
        cliente = Cliente(
            id_cliente=cliente_id,
            nombre_cliente=data.get('nombre_cliente'),
            apellido_cliente=data.get('apellido_cliente'),
            documento_cliente=data.get('documento_cliente'),
            correo_cliente=data.get('correo_cliente'),
            telefono_cliente=data.get('telefono_cliente')
        )
        ClienteModel.add_cliente(cliente)
        return jsonify({"message": "cliente agregado", "id": cliente_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_cliente(id):
    try:
        data = request.get_json()
        existing_cliente = ClienteModel.get_cliente_by_id(id)
        if not existing_cliente:
            return jsonify({"error": "cliente no encontrado"}), 404
        required_fields = ['nombre_cliente', 'apellido_cliente', 'documento_cliente','correo_cliente', 'telefono_cliente']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        cliente = Cliente(
            id_cliente=id,
            nombre_cliente=data.get('nombre_cliente'),
            apellido_cliente=data.get('apellido_cliente'),
            documento_cliente=data.get('documento_cliente'),
            correo_cliente=data.get('correo_cliente'),
            telefono_cliente=data.get('telefono_cliente')
        )
        affected_rows = ClienteModel.update_cliente(cliente)
        if affected_rows == 1:
            return jsonify({"message": "cliente actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el cliente"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_cliente(id):
    try:
        cliente = Cliente(
            id_cliente=id,
            nombre_cliente="",
            apellido_cliente="",
            documento_cliente="",
            correo_cliente="",
            telefono_cliente=""
        )
        affected_rows = ClienteModel.delete_cliente(cliente)
        if affected_rows == 1:
            return jsonify({"message": f"cliente {id} eliminado"}), 200
        else:
            return jsonify({"error": "cliente no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

