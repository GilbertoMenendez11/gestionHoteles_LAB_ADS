from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.FacturasModels import FacturaModel
from ..models.entities.Facturas import Factura
from datetime import datetime

main = Blueprint('facturas_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_factura():
    try:
        facturas = FacturaModel.get_all_factura()
        if facturas:
            return jsonify(facturas), 200
        else:
            return jsonify({"message": "No se encontraron las facturas"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_factura_by_id(id):
    try:
        factura = FacturaModel.get_factura_by_id(id)
        if factura:
            return jsonify(factura)
        else:
            return jsonify({"error": "Factura no encontrata"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_factura():
    try:
        data = request.get_json()
        required_fields = ['fechaemision_factura', 'total_factura', 'idservicio_factura', 'idreserva_factura']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        factura_id = str(uuid.uuid4())
        #Convertir la fecha en formato dd/mm/yyyy
        fechaemision_str = data.get('fechaemision_factura',
                                    datetime.now().strftime('%d/%m/%Y'))
        fechaemision_obj = datetime.strptime(fechaemision_str, '%d/%m/%Y')
        factura = Factura(
            id_factura=factura_id,
            fechaemision_factura=fechaemision_obj,
            total_factura=data.get('total_factura'),
            idservicio_factura=data.get('idservicio_factura'),
            idreserva_factura=data.get('idreserva_factura')
        )
        FacturaModel.add_factura(factura)
        return jsonify({"message": "Factura agregada", "id": factura_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_factura(id):
    try:
        data = request.get_json()
        existing_factura = FacturaModel.get_factura_by_id(id)
        if not existing_factura:
            return jsonify({"error": "Factura no encontrada"}), 404
        required_fields = ['fechaemision_factura', 'total_factura', 'idservicio_factura', 'idreserva_factura']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        fechaemision_srt = data.get('fechaemision_factura')
        fechaemision_obj = datetime.strptime(fechaemision_srt, '%d/%m/%Y')
        factura = Factura(
            id_factura=id,
            fechaemision_factura=fechaemision_obj,
            total_factura=data.get('total_factura'),
            idservicio_factura=data.get('idservicio_factura'),
            idreserva_factura=data.get('idreserva_factura')
        )
        affected_rows = FacturaModel.update_factura(factura)
        if affected_rows == 1:
            return jsonify({"message": "Factura actualizada correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar la factura"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_factura(id):
    try:
        factura = Factura(
            id_factura=id,
            fechaemision_factura=datetime.now(),
            total_factura="",
            idservicio_factura="",
            idreserva_factura=""
        )
        affected_rows = FacturaModel.delete_factura(factura)
        if affected_rows == 1:
            return jsonify({"message": f"Factura {id} eliminada"}), 200
        else:
            return jsonify({"error": "Factura no encontrada"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

