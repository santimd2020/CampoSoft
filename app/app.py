from flask import Flask, jsonify, request, render_template, Response
from flask_cors import CORS

app = Flask(__name__)

# configuracion de la api cloudinary, se ingresan las credenciales dadas por la api


CORS(app)


# metodo que tiene un id como parametro, permitiendo la consulta de un ejercicio en especifico mediante ese id

@app.route('/consultaPrueba', methods=['GET', 'POST'])
def consultaPruebas():
    return jsonify({'status': 'Si funciona'}),200