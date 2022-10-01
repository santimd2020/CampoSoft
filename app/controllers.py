from flask import jsonify,request
from app.model import Informacion,Vendedor,Producto
from app.validate import ValidacionCrearVendedor,ValidacionEliminarVendedor,ValidacionActualizarVendedor,ValidacionConsultarVendedor,ValidacionCrearProducto,ValidacionConsultarProducto,ValidacionActualizarProducto,ValidacionEliminarProducto
from app.constantes import codigos

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

#Objetos reglas vendedor
ReglaRegistroVendedor=ValidacionCrearVendedor()
ReglaConsultarVendedor=ValidacionConsultarVendedor()
ReglaActulizarVendedor=ValidacionActualizarVendedor()
ReglaEliminaVendedor=ValidacionEliminarVendedor()

#Objetos reglas producto
ReglaRegistroProducto=ValidacionCrearProducto()
ReglaConsultarProducto=ValidacionConsultarProducto()
ReglaActulizarProducto=ValidacionActualizarProducto()
ReglaEliminaProducto=ValidacionEliminarProducto()

#Clase de informacion comprueba el estado del servicio
class Informacion:
    def consultar(self):
        #Va a llamar la conexiona la base de datos
        estado=conexionInfo.estado()
        return estado
 
#Clase que permite crear el vendedor  
class RegistroVendedor():
    def post(self):
        try:
            #Se realizan validaciones de campos a registrar.
            content=request.get_json()
            error=ReglaRegistroVendedor.load(content)
        
            TIPO_ID=content.get("TIPO_ID")
            NUMERO_ID=content.get("NUMERO_ID")
            PRIMER_NOMBRE=content.get("PRIMER_NOMBRE")
            SEGUNDO_NOMBRE=content.get("SEGUNDO_NOMBRE")
            PRIMER_APELLIDO=content.get("PRIMER_APELLIDO")
            SEGUNDO_APELLIDO=content.get("SEGUNDO_APELLIDO")
            DIRECCION=content.get("DIRECCION")
            EMAIL=content.get("EMAIL")

            #Se consulta si ya existe el ID
            consulta = conexionConVen.consultar(TIPO_ID, NUMERO_ID)
            if(consulta[0]=="000"):
                #Si no existe, lo inserta
                insertar = conexionRegVen.insertar(TIPO_ID, NUMERO_ID, PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO,SEGUNDO_APELLIDO,DIRECCION,EMAIL)
                if(insertar=="000"):
                    return jsonify({"Estado":("00",""+respuesta["00"])}),200
                #En caso de que retorne un error
                else:
                    return jsonify({"Estado":("05",""+respuesta["05"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":insertar}),500  
            elif(consulta[0]=="003"):
                return jsonify({"Estado":("03",""+respuesta["03"])}),409  
             
            elif(consulta[0]=="001"):
                return jsonify({"Estado":("01",""+respuesta["01"])}),409  
            
            else:
                return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite consultar el vendedor  
class ConsultarVendedor():
    def get(self):
        try:
            #Se realizan validacion para eliminae.
            content=request.get_json()
            error=ReglaConsultarVendedor.load(content)
        
            TIPO_ID=content.get("TIPO_ID")
            NUMERO_ID=content.get("NUMERO_ID")

            #Se consulta si existe en la base datos
            consulta = conexionConVen.consultar(TIPO_ID, NUMERO_ID)
            if(consulta[0]=="003"):
                return jsonify({"Estado":("00",""+respuesta["00"])},{"Vendedor":consulta[1]}),200
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            #En caso de que no exista
            else:
                return jsonify({"Estado":("08",""+respuesta["08"])}),200     
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

 #Clase que permite consultar el vendedor  
class ConsultarTotalVendedor():
    def get(self):
        try:
            #Se consulta si existe en la base datos
            consulta = conexionConTotVen.consultarTotal()
            if(consulta[0]=="003"):
                return jsonify({"Estado":("00",""+respuesta["00"])},{"Vendedores":consulta[1]}),200
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            #En caso de que no exista
            else:
                return jsonify({"Estado":("09",""+respuesta["09"])}),200     
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite actualizar el vendedor  
class ActualizarVendedor():
    def put(self):
        try:
            #Se realizan validacion para actualizar.
            content=request.get_json()
            error=ReglaActulizarVendedor.load(content)
        
            TIPO_ID=content.get("TIPO_ID")
            NUMERO_ID=content.get("NUMERO_ID")
            PRIMER_NOMBRE=content.get("PRIMER_NOMBRE")
            SEGUNDO_NOMBRE=content.get("SEGUNDO_NOMBRE")
            PRIMER_APELLIDO=content.get("PRIMER_APELLIDO")
            SEGUNDO_APELLIDO=content.get("SEGUNDO_APELLIDO")
            DIRECCION=content.get("DIRECCION")
            EMAIL=content.get("EMAIL")

            #Se consulta si existe en la base datos
            consulta = conexionConVen.consultar(TIPO_ID, NUMERO_ID)
            if(consulta[0]=="000"):
                #Si no existe
                return jsonify({"Estado":("07",""+respuesta["07"])}),409
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            else:
                update = conexionActVen.update(TIPO_ID, NUMERO_ID, PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO,SEGUNDO_APELLIDO,DIRECCION,EMAIL)
                if(update=="000"):
                    return jsonify({"Estado":("00",""+respuesta["00"])}),200
                else:
                    print(update)
                    return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":update}),500
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite eliminar el vendedor  
class EliminarVendedor():
    def delete(self):
        try:
            #Se realizan validacion para eliminae.
            content=request.get_json()
            error=ReglaEliminaVendedor.load(content)
        
            TIPO_ID=content.get("TIPO_ID")
            NUMERO_ID=content.get("NUMERO_ID")

            #Se consulta si existe en la base datos
            consulta = conexionConVen.consultar(TIPO_ID, NUMERO_ID)
            if(consulta[0]=="000"):
                #Si no existe
                return jsonify({"Estado":("06",""+respuesta["06"])}),409
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            else:
                eliminar = conexionRegVen.eliminar(TIPO_ID, NUMERO_ID)
                if(eliminar=="000"):
                    return jsonify({"Estado":("00",""+respuesta["00"])}),200
                else:
                    print(eliminar)
                    return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":eliminar}),500
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite crear el producto  
class RegistroProducto():
    def post(self):
        try:
            #Se realizan validaciones de campos a registrar.
            content=request.get_json()
            error=ReglaRegistroProducto.load(content)

            TIPO_ID=content.get("TIPO_ID")
            NUMERO_ID=content.get("NUMERO_ID")
            NOMBRE=content.get("NOMBRE_PRODUCTO")
            DESCRIPCION=content.get("DESCRIPCION_PRODUCTO")
            VALOR_TOTAL=content.get("VALOR_TOTAL_PRODUCTO")
            DIRECCION=content.get("DIRECCION_PRODUCTO")
            TELEFONO=content.get("TELEFONO_PRODUCTO")

            #Se consulta si ya existe el vendedor
            consulta = conexionConVen.consultar(TIPO_ID,NUMERO_ID)
            if(consulta[0]=="003"):
                #Si existe, se consulta si ya el producto
                consulta = conexionConPro.consultar(NUMERO_ID, NOMBRE)
                if(consulta[0]=="000"):
                    insertar = conexionRegPro.insertar(NUMERO_ID,NOMBRE,DESCRIPCION,VALOR_TOTAL,DIRECCION,TELEFONO)
                    if(insertar=="000"):
                        return jsonify({"Estado":("00",""+respuesta["00"])}),200
                    #En caso de que retorne un error
                    else:
                        return jsonify({"Estado":("10",""+respuesta["10"])}),409
                #En caso de que retorne un error
                elif(len(consulta)>4):
                    return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
                #En caso de que no exista
                else:
                    return jsonify({"Estado":("10",""+respuesta["10"])}),200         
            elif(consulta[0]=="008"):
                return jsonify({"Estado":("08",""+respuesta["08"])}),409  
             
            elif(consulta[0]=="001"):
                return jsonify({"Estado":("01",""+respuesta["01"])}),409  
            
            else:
                return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite consultar el vendedor  
class ConsultarProducto():
    def get(self):
        try:
            #Se realizan validacion consultar
            content=request.get_json()
            error=ReglaConsultarProducto.load(content)
        
            NUMERO_ID=content.get("NUMERO_ID")
            NOMBRE=content.get("NOMBRE_PRODUCTO")

            #Se consulta si existe en la base datos
            consulta = conexionConPro.consultar(NUMERO_ID, NOMBRE)
            if(consulta[0]=="003"):
                return jsonify({"Estado":("00",""+respuesta["00"])},{"Vendedor":consulta[1]}),200
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            #En caso de que no exista
            else:
                return jsonify({"Estado":("08",""+respuesta["08"])}),200     
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

 #Clase que permite consultar el vendedor  
class ConsultarTotalProducto():
    def get(self):
        try:
            #Se consulta si existe en la base datos
            consulta = conexionConTotPro.consultarTotal()
            if(consulta[0]=="003"):
                return jsonify({"Estado":("00",""+respuesta["00"])},{"Productos diponibles":consulta[1]}),200
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            #En caso de que no exista
            else:
                return jsonify({"Estado":("09",""+respuesta["09"])}),200     
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite actualizar el vendedor  
class ActualizarProducto():
    def put(self):
        try:
            #Se realizan validacion para actualizar.
            content=request.get_json()
            error=ReglaActulizarProducto.load(content)
        
            NUMERO_ID=content.get("NUMERO_ID")
            NOMBRE=content.get("NOMBRE_PRODUCTO")
            DESCRIPCION=content.get("DESCRIPCION_PRODUCTO")
            VALOR_TOTAL=content.get("VALOR_TOTAL_PRODUCTO")
            DIRECCION=content.get("DIRECCION_PRODUCTO")
            TELEFONO=content.get("TELEFONO_PRODUCTO")

            #Se consulta si existe en la base datos
            consulta = conexionConPro.consultar(NUMERO_ID, NOMBRE)
            if(consulta[0]=="000"):
                #Si no existe
                return jsonify({"Estado":("07",""+respuesta["07"])}),409
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            else:
                update = conexionActPro.update(NUMERO_ID, NOMBRE, DESCRIPCION, VALOR_TOTAL,DIRECCION,TELEFONO)
                if(update=="000"):
                    return jsonify({"Estado":("00",""+respuesta["00"])}),200
                else:
                    print(update)
                    return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":update}),500
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409

#Clase que permite eliminar el vendedor  
class EliminarProducto():
    def delete(self):
        try:
            #Se realizan validacion para eliminae.
            content=request.get_json()
            error=ReglaEliminaProducto.load(content)
        
            NUMERO_ID=content.get("NUMERO_ID")
            NOMBRE=content.get("NOMBRE_PRODUCTO")

            #Se consulta si existe en la base datos
            consulta = conexionConPro.consultar(NUMERO_ID,NOMBRE)
            if(consulta[0]=="000"):
                #Si no existe
                return jsonify({"Estado":("06",""+respuesta["06"])}),409
            #En caso de que retorne un error
            elif(len(consulta)>4):
                 return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":consulta}),500
            else:
                eliminar = conexionRegPro.eliminar(NUMERO_ID, NOMBRE)
                if(eliminar=="000"):
                    return jsonify({"Estado":("00",""+respuesta["00"])}),200
                else:
                    print(eliminar)
                    return jsonify({"Estado":("04",""+respuesta["04"]),"¡Atencion!": "Comuniquese con el administrador del sistema","¡Error!":eliminar}),500
        except Exception as error:
            tojson = str(error)
            return jsonify({"Estado":("02",""+respuesta["02"]),"¡Error!":tojson}),409