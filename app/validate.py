from marshmallow import Schema, fields, validate

#Validaciones para crear vendedor
class ValidacionCrearVendedor(Schema):
    TIPO_ID = fields.Str(required=True, validate=validate.Length(min=2, max=2), data_key='TIPO_ID')
    NUMERO_ID = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')
    PRIMER_NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='PRIMER_NOMBRE')
    SEGUNDO_NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='SEGUNDO_NOMBRE')
    PRIMER_APELLIDO = fields.Str(required=True, validate=validate.Length(max=25), data_key='PRIMER_APELLIDO')
    SEGUNDO_APELLIDO = fields.Str(required=True, validate=validate.Length(max=25), data_key='SEGUNDO_APELLIDO')
    DIRECCION = fields.Str(required=True, validate=validate.Length(max=90), data_key='DIRECCION')
    EMAIL = fields.Str(required=True, validate=validate.Email(),data_key='EMAIL')

#Validaciones para consultar vendedor
class ValidacionConsultarVendedor(Schema):
    TIPO_ID = fields.Str(required=True, validate=validate.Length(min=2, max=2), data_key='TIPO_ID')
    NUMERO_ID = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')

#Validaciones para actualizar vendedor
class ValidacionActualizarVendedor(Schema):
    TIPO_ID = fields.Str(required=True, validate=validate.Length(min=2, max=2), data_key='TIPO_ID')
    NUMERO_ID = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')
    PRIMER_NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='PRIMER_NOMBRE')
    SEGUNDO_NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='SEGUNDO_NOMBRE')
    PRIMER_APELLIDO = fields.Str(required=True, validate=validate.Length(max=25), data_key='PRIMER_APELLIDO')
    SEGUNDO_APELLIDO = fields.Str(required=True, validate=validate.Length(max=25), data_key='SEGUNDO_APELLIDO')
    DIRECCION = fields.Str(required=True, validate=validate.Length(max=90), data_key='DIRECCION')
    EMAIL = fields.Str(required=True, validate=validate.Email(),data_key='EMAIL')

#Validaciones para eliminar vendedor
class ValidacionEliminarVendedor(Schema):
    TIPO_ID = fields.Str(required=True, validate=validate.Length(min=2, max=2), data_key='TIPO_ID')
    NUMERO_ID = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')

#Validaciones para crear producto
class ValidacionCrearProducto(Schema):
    TIPO_ID = fields.Str(required=True, validate=validate.Length(min=2, max=2), data_key='TIPO_ID')
    NUMERO_ID = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')
    NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='NOMBRE_PRODUCTO')
    DESCRIPCION = fields.Str(required=True, validate=validate.Length(max=256), data_key='DESCRIPCION_PRODUCTO')
    VALOR_TOTAL = fields.Float(required=True,data_key='VALOR_TOTAL_PRODUCTO')
    DIRECCION = fields.Str(required=True, validate=validate.Length(max=90), data_key='DIRECCION_PRODUCTO')
    TELEFONO = fields.Str(required=True,validate=validate.Length(max=90),data_key='TELEFONO_PRODUCTO')

#Validaciones para consultar producto
class ValidacionConsultarProducto(Schema):
    ID_VENDEDOR = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')
    NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='NOMBRE_PRODUCTO')

#Validaciones para actualizar producto
class ValidacionActualizarProducto(Schema):
    NUMERO_ID = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')
    NOMBRE = fields.Str(required=True, validate=validate.Length(max=25), data_key='NOMBRE_PRODUCTO')
    DESCRIPCION = fields.Str(required=True, validate=validate.Length(max=256), data_key='DESCRIPCION_PRODUCTO')
    VALOR_TOTAL = fields.Float(required=True,data_key='VALOR_TOTAL_PRODUCTO')
    DIRECCION = fields.Str(required=True, validate=validate.Length(max=90), data_key='DIRECCION_PRODUCTO')
    TELEFONO = fields.Str(required=True,validate=validate.Length(max=90),data_key='TELEFONO_PRODUCTO')

#Validaciones para eliminar producto
class ValidacionEliminarProducto(Schema):
    NUMERO_ID=fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='NUMERO_ID')
    NOMBRE=fields.Str(required=True, validate=validate.Length(max=25), data_key='NOMBRE_PRODUCTO')