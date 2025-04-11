from flask import Blueprint, jsonify, request
import uuid #que lo usaremos para generarlos en postgres
from ..models.HotelesModels import HotelModel
from ..models.entities.Hoteles import Hotel

main = Blueprint('hoteles_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_hoteles():
    try:
        hoteles = HotelModel.get_all_hoteles()
        if hoteles:
            return jsonify(hoteles), 200
        else:
            return jsonify({"message": "No se encontraron hoteles"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_hotel_by_id(id):
    try:
        hotel = HotelModel.get_hotel_by_id(id)
        if hotel:
            return jsonify(hotel)
        else:
            return jsonify({"error": "hotel no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_hotel():
    try:
        data = request.get_json()
        required_fields = ['nombre_hotel', 'direccion_hotel', 'telefono_hotel', 'correo_hotel', 'categoria_hotel']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        hotel_id = str(uuid.uuid4())
        hotel = Hotel(
            id_hotel=hotel_id,
            nombre_hotel=data.get('nombre_hotel'),
            direccion_hotel=data.get('direccion_hotel'),
            telefono_hotel=data.get('telefono_hotel'),
            correo_hotel=data.get('correo_hotel'),
            categoria_hotel=data.get('categoria_hotel')
        )
        HotelModel.add_hotel(hotel)
        return jsonify({"message": "hotel agregado", "id": hotel_id}), 201
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo metodo PUT
@main.route('/update/<id>', methods=['PUT'])
def update_hotel(id):
    try:
        data = request.get_json()
        existing_hotel = HotelModel.get_hotel_by_id(id)
        if not existing_hotel:
            return jsonify({"error": "hotel no encontrado"}), 404
        required_fields = ['nombre_hotel', 'direccion_hotel', 'telefono_hotel','correo_hotel', 'categoria_hotel']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {', '.join(missing_fields)}"}), 400
        hotel = Hotel(
            id_hotel=id,
            nombre_hotel=data.get('nombre_hotel'),
            direccion_hotel=data.get('direccion_hotel'),
            telefono_hotel=data.get('telefono_hotel'),
            correo_hotel=data.get('correo_hotel'),
            categoria_hotel=data.get('categoria_hotel')
        )
        affected_rows = HotelModel.update_hotel(hotel)
        if affected_rows == 1:
            return jsonify({"message": "hotel actualizado correctamente"}), 200
        else:
            return jsonify({"error": "No se pudo actualizar el hotel"}), 400
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Haciendo el metodo DELETE
@main.route('/delete/<id>', methods=['DELETE'])
def delete_hotel(id):
    try:
        hotel = Hotel(
            id_hotel=id,
            nombre_hotel="",
            direccion_hotel="",
            telefono_hotel="",
            correo_hotel="",
            categoria_hotel=""
        )
        affected_rows = HotelModel.delete_hotel(hotel)
        if affected_rows == 1:
            return jsonify({"message": f"hotel {id} eliminado"}), 200
        else:
            return jsonify({"error": "hotel no encontrado"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

