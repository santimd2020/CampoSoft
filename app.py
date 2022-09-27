from flask import Flask
from routes import *
from flask.views import MethodView
from flask import jsonify,request
from model import Informacion,Vendedor,Producto
from validate import ValidacionCrearVendedor,ValidacionEliminarVendedor,ValidacionActualizarVendedor,ValidacionConsultarVendedor,ValidacionCrearProducto,ValidacionConsultarProducto,ValidacionActualizarProducto,ValidacionEliminarProducto
from constantes import codigos

#Objetos de respuesta
respuesta=codigos

#Objeto conexion general
conexionInfo=Informacion()

#Objetos conexion vendedor
conexionRegVen=Vendedor()
conexionConVen=Vendedor()
conexionConTotVen=Vendedor()
conexionActVen=Vendedor()
conexionEliVen=Vendedor()

#Objetos conexion producto
conexionRegPro=Producto()
conexionConPro=Producto()
conexionConTotPro=Producto()
conexionActPro=Producto()
conexionEliPro=Producto()

app = Flask(__name__)

@app.route('/CampoSoft', methods=['POST'])
def post(self):
    def post(self):
        #Va a llamar la conexiona la base de datos
        estado=conexionInfo.estado()
        if(estado=="000"):
            return jsonify({"estado":("00",""+respuesta["00"],"Estado del servicio: Activo","Estado de la base datos: Activo")},
                               {"CampoSoft":("¡Bienvenido a CampoSoft!","Un Servicio que le permitira registrar sus productos para mejorar sus ventas.",
                               "Autores:",
                               "Santiago Muñoz",
                               "Julian Cardenas",
                               "Agustin Martinez",
                               "Alvaro Perez",
                               "Marco Antonio"
                               )}),200
        #En caso de que retorne un error
        else:
             return jsonify({"estado":("01",""+respuesta["01"],"Estado del servicio: Activo","Estado de la base datos: Inactivo")},
                               {"CampoSoft":("¡Bienvenido a CampoSoft!","Un Servicio que le permitira registrar sus productos para mejorar sus ventas.",
                               "Autores:",
                               "Santiago Muñoz",
                               "Julian Cardenas",
                               "Agustin Martinez",
                               "Alvaro Perez",
                               "Marco Antonio"
                               )},{"¡Atencion!": "Comuniquese con el administrador del sistema"},{"¡Error!":estado}),500






"""
#Ruta general(comprobacion de servicios)
app.add_url_rule(routes["informacion"],view_func=routes["Informacion_controllers"])

#Rutas vendedor
app.add_url_rule(routes["registroVendedor"],view_func=routes["RegistroVendedor_controllers"])
app.add_url_rule(routes["consultarVendedor"],view_func=routes["ConsultarVendedor_controllers"])
app.add_url_rule(routes["consultarTotalVendedor"],view_func=routes["ConsultarTotalVendedor_controllers"])
app.add_url_rule(routes["eliminarVendedor"],view_func=routes["EliminarVendedor_controllers"])
app.add_url_rule(routes["actualizarVendedor"],view_func=routes["ActualizarVendedor_controllers"])

#Rutas producto
app.add_url_rule(routes["registroProducto"],view_func=routes["RegistroProducto_controllers"])
app.add_url_rule(routes["consultarProducto"],view_func=routes["ConsultarProducto_controllers"])
app.add_url_rule(routes["consultarTotalProducto"],view_func=routes["ConsultarTotalProducto_controllers"])
app.add_url_rule(routes["eliminarProducto"],view_func=routes["EliminarProducto_controllers"])
app.add_url_rule(routes["actualizarProducto"],view_func=routes["ActualizarProducto_controllers"])
"""