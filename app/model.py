from async_timeout import timeout
import psycopg2
#Clase que permite hacer un testeto de la conexion a la base de datos.
class Informacion:
    #Funcion que permite testeeo de la conexion a la base de datos.
    def estado(self):
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5433", connect_timeout=29)
            cursor = conexion.cursor()
            conexion.commit()
            estado="000"
        except Exception as error:
            estado = str(error)
            print("¡Error de conexion con la base datos!:",error)
        finally:
            if(estado=="000"):
                cursor.close()
                conexion.close() 
        return estado

#Clase que va a controlar las funcionas a realizar sobre el vendedor.
class Vendedor:
    #Funcion para insertar datos dentro de la tabla VENDEDOR
    def insertar(self,TIPO_ID,NUMERO_ID,PRIMER_NOMBRE,SEGUNDO_NOMBRE,PRIMER_APELLIDO,SEGUNDO_APELLIDO,DIRECCION,EMAIL):
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            cursor = conexion.cursor()
            sql = "INSERT INTO VENDEDOR VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            datos = (TIPO_ID, NUMERO_ID, PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO,SEGUNDO_APELLIDO,DIRECCION,EMAIL)
            cursor.execute(sql, datos)
            conexion.commit()
            insertar ="000"
        except Exception as error:
            insertar=str(error)
            print("Error tecnico:",error)
        finally:
            if(insertar=="000"):
                cursor.close()
                conexion.close() 
        return insertar

    #Funcion para consultar datos dentro de la tabla VENDEDOR
    def consultar(self,TIPO_ID,NUMERO_ID):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "select 'TIPO_ID: '||TIPO_ID,'NUMERO_ID: '||NUMERO_ID,'PRIMER_NOMBRE: '||PRIMER_NOMBRE,'SEGUNDO_NOMBRE: '||SEGUNDO_NOMBRE,'PRIMER_APELLIDO: '||PRIMER_APELLIDO,'SEGUNDO_APELLIDO: '||SEGUNDO_APELLIDO,'DIRECCION: '||DIRECCION,'EMAIL: '||EMAIL from vendedor WHERE TIPO_ID=%s AND NUMERO_ID=%s"
            datos = (TIPO_ID, NUMERO_ID)
            cursor.execute(sql,datos)
            diccionario = cursor.fetchall() 
            conexion.commit()
            #Organizamiento de la respuesta
            if(len(diccionario)==0):
                consulta="000"
            else:
                consulta="003"
        except Exception as error:
            if(validarConexion==None):
                consulta=str(error)
                print("Error tecnico:",error)
            else:
                consulta=str(error)
                print("Error tecnico:",error)
        finally:
            if(consulta=="000"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            elif(consulta=="003"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            else: return consulta    

    #Funcion para consultar todos datos dentro de la tabla VENDEDOR
    def consultarTotal(self):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "select 'TIPO_ID: '||TIPO_ID,'NUMERO_ID: '||NUMERO_ID,'PRIMER_NOMBRE: '||PRIMER_NOMBRE,'SEGUNDO_NOMBRE: '||SEGUNDO_NOMBRE,'PRIMER_APELLIDO: '||PRIMER_APELLIDO,'SEGUNDO_APELLIDO: '||SEGUNDO_APELLIDO,'DIRECCION: '||DIRECCION,'EMAIL: '||EMAIL from vendedor;"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            conexion.commit()
            if(len(diccionario)==0):
                consulta="000"
            else:
                consulta="003"
        except Exception as error:
            if(validarConexion==None):
                consulta=str(error)
                print("Error tecnico:",error)
            else:
                consulta=str(error)
                print("Error tecnico:",error)
        finally:
            if(consulta=="000"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            elif(consulta=="003"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            else: return consulta

    #Funcion para eliminar datos de la tabla VENDEDOR
    def eliminar(self,TIPO_ID,NUMERO_ID):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "DELETE FROM VENDEDOR WHERE TIPO_ID=%s and NUMERO_ID=%s"
            datos = (TIPO_ID, NUMERO_ID)
            cursor.execute(sql,datos)
            conexion.commit()
            eliminar='000'
        except Exception as error:
            if(validarConexion==None):
                eliminar=str(error)
                print("Error tecnico:",error)
            else:
                eliminar=str(error)
                print("Error tecnico:",error)
        finally:
             if(eliminar=="000"):
                cursor.close()
                conexion.close()
        return eliminar

    #Funcion para actualizar datos de la tabla VENDEDOR
    def update(self, TIPO_ID,NUMERO_ID,PRIMER_NOMBRE,SEGUNDO_NOMBRE,PRIMER_APELLIDO,SEGUNDO_APELLIDO,DIRECCION,EMAIL):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "UPDATE VENDEDOR SET PRIMER_NOMBRE=%s, SEGUNDO_NOMBRE=%s, PRIMER_APELLIDO=%s, SEGUNDO_APELLIDO=%s, DIRECCION=%s, EMAIL=%s where TIPO_ID=%s AND NUMERO_ID=%s"
            datos = (PRIMER_NOMBRE, SEGUNDO_NOMBRE, PRIMER_APELLIDO,SEGUNDO_APELLIDO,DIRECCION,EMAIL,TIPO_ID, NUMERO_ID)
            cursor.execute(sql,datos)
            conexion.commit()
            update='000'
        except Exception as error:
            if(validarConexion==None):
                update=str(error)
                print("Error tecnico:",error)
            else:
                update=str(error)
                print("Error tecnico:",error)
        finally:
            if(update=="000"):
                cursor.close()
                conexion.close()
        return update

#Clase que va a controlar las funcionas a realizar sobre el producto.
class Producto:
    #Funcion para insertar datos dentro de la tabla VENDEDOR
    def insertar(self,ID_VENDEDOR,NOMBRE,DESCRIPCION,VALOR_TOTAL,DIRECCION,TELEFONO):
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            cursor = conexion.cursor()
            sql = "INSERT INTO PRODUCTO VALUES(%s,%s,%s,%s,%s,%s)"
            datos = (ID_VENDEDOR,NOMBRE,DESCRIPCION,VALOR_TOTAL,DIRECCION,TELEFONO)
            cursor.execute(sql, datos)
            conexion.commit()
            insertar ="000"
        except Exception as error:
            insertar=str(error)
            print("Error tecnico:",error)
        finally:
            if(insertar=="000"):
                cursor.close()
                conexion.close() 
        return insertar

    #Funcion para consultar datos dentro de la tabla producto
    def consultar(self,ID_VENDEDOR,NOMBRE):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "select'NUMERO ID: '||A.NUMERO_ID,'NOMBRES: '||A.PRIMER_NOMBRE||''||A.SEGUNDO_NOMBRE,'APELLIDOS: '||A.PRIMER_APELLIDO||''||A.SEGUNDO_APELLIDO,'DIRECCION VENDEDOR: '||A.DIRECCION,'EMAIL VENDEDOR: '||A.EMAIL,'NOMBRE PRODUCTO: '||B.NOMBRE,'DESCRIPCION PRODUCTO: '||B.DESCRIPCION,'DIRECCION PRODUCTO: '||B.DESCRIPCION,'TELEFONO PRODUCTO: '||B.TELEFONO,'VALOR PRODUCTO: '||B.VALOR_TOTAL from vendedor A,producto B WHERE  B.ID_VENDEDOR=%s AND  B.NOMBRE=%s AND  B.ID_VENDEDOR=A.NUMERO_ID;"
            datos = (ID_VENDEDOR, NOMBRE)
            cursor.execute(sql,datos)
            diccionario = cursor.fetchall() 
            conexion.commit()
            print(diccionario)
            #Organizamiento de la respuesta
            if(len(diccionario)==0):
                consulta="000"
            else:
                consulta="003"
        except Exception as error:
            if(validarConexion==None):
                consulta=str(error)
                print("Error tecnico:",error)
            else:
                consulta=str(error)
                print("Error tecnico:",error)
        finally:
            if(consulta=="000"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            elif(consulta=="003"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            else: return consulta    

    #Funcion para consultar todos datos dentro de la tabla VENDEDOR
    def consultarTotal(self):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "select'NUMERO ID: '||A.NUMERO_ID,'NOMBRES: '||A.PRIMER_NOMBRE||' '||A.SEGUNDO_NOMBRE,'APELLIDOS: '||A.PRIMER_APELLIDO||' '||A.SEGUNDO_APELLIDO,'DIRECCION VENDEDOR: '||A.DIRECCION,'EMAIL VENDEDOR: '||A.EMAIL,'NOMBRE PRODUCTO: '||B.NOMBRE,'DESCRIPCION PRODUCTO: '||B.DESCRIPCION,'DIRECCION PRODUCTO: '||B.DESCRIPCION,'TELEFONO PRODUCTO: '||B.TELEFONO,'VALOR PRODUCTO: '||B.VALOR_TOTAL from vendedor A,producto B WHERE B.ID_VENDEDOR=A.NUMERO_ID;"
            cursor.execute(sql)
            diccionario = cursor.fetchall()
            conexion.commit()
            if(len(diccionario)==0):
                consulta="000"
            else:
                consulta="003"
        except Exception as error:
            if(validarConexion==None):
                consulta=str(error)
                print("Error tecnico:",error)
            else:
                consulta=str(error)
                print("Error tecnico:",error)
        finally:
            if(consulta=="000"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            elif(consulta=="003"):
                cursor.close()
                conexion.close()
                return consulta,diccionario
            else: return consulta

    #Funcion para eliminar datos de la tabla VENDEDOR
    def eliminar(self,ID_VENDEDOR,NOMBRE):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "DELETE FROM PRODUCTO WHERE ID_VENDEDOR=%s and NOMBRE=%s"
            datos = (ID_VENDEDOR, NOMBRE)
            cursor.execute(sql,datos)
            conexion.commit()
            eliminar='000'
        except Exception as error:
            if(validarConexion==None):
                eliminar=str(error)
                print("Error tecnico:",error)
            else:
                eliminar=str(error)
                print("Error tecnico:",error)
        finally:
             if(eliminar=="000"):
                cursor.close()
                conexion.close()
        return eliminar

    #Funcion para actualizar datos de la tabla VENDEDOR
    def update(self,NUMERO_ID, NOMBRE, DESCRIPCION, VALOR_TOTAL,DIRECCION,TELEFONO):
        validarConexion=None
        try:
            conexion = psycopg2.connect(database="persona", user="postgres", password="12345678",host="campsoft.cubqdb8xhzud.us-east-1.rds.amazonaws.com", port="5432")
            validarConexion="000"
            cursor = conexion.cursor()
            sql = "UPDATE PRODUCTO SET DESCRIPCION=%s, VALOR_TOTAL=%s, DIRECCION=%s, TELEFONO=%s where ID_VENDEDOR=%s AND NOMBRE=%s;"
            datos = (DESCRIPCION, VALOR_TOTAL, DIRECCION,TELEFONO,NUMERO_ID,NOMBRE)
            cursor.execute(sql,datos)
            conexion.commit()
            update='000'
        except Exception as error:
            if(validarConexion==None):
                update=str(error)
                print("Error tecnico:",error)
            else:
                update=str(error)
                print("Error tecnico:",error)
        finally:
            if(update=="000"):
                cursor.close()
                conexion.close()
        return update