from flask import Flask, Blueprint, request, jsonify
from models.VentaProducto import VentaProducto, VentaProductoSchema
from config.bd import app, bd, ma

ruta_venta_produco = Blueprint("ruta_venta_produco", __name__)

ventaProducto_schema = VentaProductoSchema()
ventaProductors_schema = VentaProductoSchema(many=True)

@ruta_venta_produco.route("/guardarVentaProducto", methods=['POST'])
def saveVentaProducto():
    id_producto = request.json['id_producto']
    nuevo_venta_producto = VentaProducto(id_producto)
    bd.session.add(nuevo_venta_producto)
    bd.session.commit()
    return ventaProducto_schema.jsonify(nuevo_venta_producto)

@ruta_venta_produco.route("/eliminarVentaProducto", methods=['DELETE'])
def eliminarVendedor():
    id = request.json['id']
    venta_produco = VentaProducto.query.get(id)
    if venta_produco is None:
        return jsonify({"mensaje": "No se encontró la Venta_produco"})
    bd.session.delete(venta_produco)
    bd.session.commit()
    return jsonify({"message": "Venta_produco eliminado"}), 200

@ruta_venta_produco.route("/guardarCotizacion", methods=['POST'])
def guardarCotizacion():
    data = request.json
    cliente = data['cliente']
    producto = data['producto']
    cantidad = data['cantidad']
    # Aquí puedes guardar la cotización en la base de datos si es necesario.
    # Por ahora, vamos a devolver los datos como si se hubieran guardado.
    cotizacion = {
        'cliente': cliente,
        'producto': producto,
        'cantidad': cantidad
    }
    return jsonify(cotizacion), 201

app.register_blueprint(ruta_venta_produco)
