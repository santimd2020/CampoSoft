from flask import Flask,jsonify,request
from flask_cors import CORS
from app.controllers import Informacion
from app.constantes import codigos

app = Flask(__name__)

CORS(app)

#Objetos de respuesta
respuesta=codigos

#Objeto conexion general
conexionInfo=Informacion()

@app.route('/CampoSoft',methods=['POST'])
def estado():
    estado=conexionInfo.consultar()
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
        print(estado)
        return jsonify({"estado":("01",""+respuesta["01"],"Estado del servicio: Activo","Estado de la base datos: Inactivo")},
                               {"CampoSoft":("¡Bienvenido a CampoSoft!","Un Servicio que le permitira registrar sus productos para mejorar sus ventas.",
                               "Autores:",
                               "Santiago Muñoz",
                               "Julian Cardenas",
                               "Agustin Martinez",
                               "Alvaro Perez",
                               "Marco Antonio"
                               )},{"¡Atencion!": "Comuniquese con el administrador del sistema"},{"¡Error!":estado}),500

@app.route('/prueba',methods=['POST'])
def prueba():
    return jsonify({'status': 'ok'}), 200