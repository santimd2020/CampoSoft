from flask import Flask
from routes import *

app = Flask(__name__)

@app.route('/CampoSoft', methods=['POST'])
def post(self):
    return app.add_url_rule(routes["informacion"],view_func=routes["Informacion_controllers"])







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
