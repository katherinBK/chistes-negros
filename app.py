from flask import Flask,jsonify
import requests
import json

app = Flask(__name__)
#Arreglo que contiene los chistes
chistes = {
    "mujeres": [
        {"id": 1, "titulo": "el chiste", "chiste": "un chiste"},
        {"id": 2, "titulo": "otro chiste", "chiste": "otro chiste"}
    ],
    "gordos": [
        {"id": 1, "titulo": "el chiste", "chiste": "un chiste"},
        {"id": 2, "titulo": "otro chiste", "chiste": "otro chiste"}
    ]
}

@app.route('/', methods =['GET'])
def get_books():
    #funcion para devolvder el contenido de "chistes" en formato json
    return jsonify (chistes)

#funcion dentro de flask para correr el API
if __name__ == '__main__':
    app.run(debug=True)