from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.PagosModels import PagoModel
from ..models.entities.Pagos import Pago

main = Blueprint('pagos_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_pagos():
    try:
        pagos = PagoModel.get_all_pagos()
        if pagos:
            return jsonify(pagos), 200
        else:
            return jsonify({"message": "No se encontraron pagos"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_pago_by_id(id):
    try:
        pago = PagoModel.get_pago_by_id(id)
        if pago:
            return jsonify(pago)
        else:
            return jsonify({"error": "pago no encontrato"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_pago():
    try:
        data = request.get_json()
        required_fields = ['monto_pago', 'fechapago_pago', 'metodopago_pago', 'idfactura_pago']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        pago_id = str(uuid.uuid4())
        pago = Pago(
            id_pago=pago_id,
            monto_pago=data.get('monto_pago'),
            fechapago_pago=data.get('fechapago_pago'),
            metodopago_pago=data.get('metodopago_pago'),
            idfactura_pago=data.get('idfactura_pago')
        )
        PagoModel.add_pago(pago)
        return jsonify({"message": "pago agregado", "id": pago_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_pago(id):
    try:
        data = request.get_json()
        existing_pago = PagoModel.get_pago_by_id(id)
        if not existing_pago:
            return jsonify({"error": "pago no encontrado"}), 404
        required_fields = ['monto_pago', 'fechapago_pago','metodopago_pago', 'idfactura_pago']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        pago = Pago(
            id_pago=id,
            monto_pago=data.get('monto_pago'),
            fechapago_pago=data.get('fechapago_pago'),
            metodopago_pago=data.get('metodopago_pago'),
            idfactura_pago=data.get('idfactura_pago')
        )
        affected_rows = PagoModel.update_pago(pago)
        if affected_rows == 1:
            return jsonify({"message": "pago actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el pago"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_pago(id):
    try:
        pago = Pago(
            id_pago=id,
            monto_pago="",
            fechapago_pago="",
            metodopago_pago="",
            idfactura_pago=""
        )
        affected_rows = PagoModel.delete_pago(pago)
        if affected_rows == 1:
            return jsonify({"message": f"pago {id} eliminado"}), 200
        else:
            return jsonify({"error": "pago no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

