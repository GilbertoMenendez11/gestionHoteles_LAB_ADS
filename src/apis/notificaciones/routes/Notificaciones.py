from flask import Blueprint, jsonify, request

from datetime import datetime
import uuid #que lo usaremos para generarlos en postgres
from ..models.entities.Notificaciones import Notificacion
from ..models.NotificacionesModels import NotificacionModel
from ...telefonos.models.TelefonosModels import TelefonoModel
from ..services.servicesTwilio import send_whatsapp_message
from ..services.consulta_notificaciones import get_notificacion_data

main = Blueprint('notificacion_blueprint', __name__)

@main.route('/', methods=['GET'])
def get_notificacion():
    try:
        notificacion = NotificacionModel.get_all_notificacion()
        if notificacion:
            return jsonify(notificacion), 200
        else:
            return jsonify({"message": "No se encontraron la notificacion"}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Filtrar por ID
@main.route('/<id>', methods=['GET'])
def get_notificacion_by_id(id):
    try:
        notificacion = NotificacionModel.get_notificacion_by_id(id)
        if notificacion:
            return jsonify(notificacion)
        else:
            return jsonify({"error": "notificacion no encontrata"}), 404
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
#Con el metodo POST
@main.route('/add', methods=['POST'])
def add_notificacion():
    try:
        data = request.get_json()
        required_fields = ['id_cliente', 'fecha_envio_notificacion', 'estado_notificacion']
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            return jsonify({"error": f"Faltan campos obligatorios: {','.join(missing_fields)}"}), 400
        
        id_cliente=data.get('id_cliente')
        fecha_envio_str=data.get('fecha_envio_notificacion')
        estado_notificacion=data.get('estado_notificacion')
        try:
            fecha_envio_notificacion = datetime.strptime(fecha_envio_str, "%Y-%m-%d")
        except Exception:
            return jsonify({
                "error": "Formato de fecha_envio invalido, se requiere YYYY-MM-DD"
            }), 400
        notificacion_id = str(uuid.uuid4())
        notificacion = Notificacion(
            id_notificacion=notificacion_id,
            id_cliente=id_cliente,
            fecha_envio_notificacion=fecha_envio_notificacion,
            estado_notificacion=estado_notificacion)
        affected_rows = NotificacionModel.add_notificacion(notificacion)
        if affected_rows !=1:
            return jsonify({"error": "No se puede agregar la notificacion"}), 500
        client_data = get_notificacion_data(id_cliente)
        if client_data:
            client_info = client_data[0]
            message_body = (
                "Notificación para el cliente:\n"
                "Nombre: " + client_info.get('nombre_cliente', '') + " " + client_info.get('apellido_cliente', '') + "\n"
                "Documento: " + client_info.get('documento_cliente', '') + "\n"
                "Correo: " + client_info.get('correo_cliente', '') + "\n"
                "Teléfono: " + client_info.get('telefono_cliente', '') + "\n"
                "Fecha de envío: " + fecha_envio_str + "\n"
                "Estado: " + estado_notificacion)
        else:
            message_body = "No se encontraron datos del cliente para esta notificación."
        telefonos = TelefonoModel.get_all_telefono()
        if not telefonos:
            return jsonify({"error": "No se encontraron destinatarios registrados"}), 400
        send_results = {}
        for tel in telefonos:
            numero = str(tel.get("numero_telefono", "")).strip()
            if not numero:
                send_results["Numero no definido"] = {
                    "status": "Error",
                    "error": "Numero de telefono vacio"
                }
                continue
            if not numero.startswith('+'):
                phone_number = "+503" + numero
            else:
                phone_number = numero
            try:
                sid = send_whatsapp_message(phone_number,message_body)
                send_results[phone_number] = {"status": "Enviado", "sid": sid}
            except Exception as e:
                send_results[phone_number] = {"status": "Error", "error": str(e)}
        return jsonify({
            "Id_notificacion": notificacion_id,
            "message": "Notificacion agregada y mensajes enviado",
            "send_results": send_results
        }), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
