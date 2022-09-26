from controllers import ActualizarProducto, ConsultarProducto, ConsultarTotalProducto, EliminarProducto, Informacion, RegistroProducto,RegistroVendedor,ConsultarVendedor,ConsultarTotalVendedor,ActualizarVendedor,EliminarVendedor
routes = {
    "informacion": "/CampoSoft", "Informacion_controllers": Informacion.as_view("informacion_app"),
    "registroVendedor": "/Registro/Vendedor", "RegistroVendedor_controllers": RegistroVendedor.as_view("RegistroVendedor_app"),
    "consultarVendedor": "/Consultar/Vendedor", "ConsultarVendedor_controllers": ConsultarVendedor.as_view("ConsultarVendedor_app"),
    "consultarTotalVendedor": "/ConsultarTotal/Vendedor", "ConsultarTotalVendedor_controllers": ConsultarTotalVendedor.as_view("ConsultarTotalVendedor_app"),
    "eliminarVendedor": "/Eliminar/Vendedor", "EliminarVendedor_controllers": EliminarVendedor.as_view("EliminarVendedor_app"),
    "actualizarVendedor": "/Actualizar/Vendedor", "ActualizarVendedor_controllers": ActualizarVendedor.as_view("ActualizarVendedor_app"),
    "registroProducto": "/Registro/Producto", "RegistroProducto_controllers": RegistroProducto.as_view("RegistroProducto_app"),
    "consultarProducto": "/Consultar/Producto", "ConsultarProducto_controllers": ConsultarProducto.as_view("ConsultarProducto_app"),
    "consultarTotalProducto": "/ConsultarTotal/Producto", "ConsultarTotalProducto_controllers": ConsultarTotalProducto.as_view("ConsultarTotalProducto_app"),
    "eliminarProducto": "/Eliminar/Producto", "EliminarProducto_controllers": EliminarProducto.as_view("EliminarProducto_app"),
    "actualizarProducto": "/Actualizar/Producto", "ActualizarProducto_controllers": ActualizarProducto.as_view("ActualizarProducto_app")
}
