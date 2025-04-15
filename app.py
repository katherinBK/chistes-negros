from flask import Flask,requests,jsonify
import json

app = Flask(__name__)
#Arreglo que contiene los chistes
chistes ={ [
    "mujeres": [
      {"id":1, "titulo":"el chiste","chiste":"un chiste"}
      {"id":1, "titulo":"el chiste","chiste":"un chiste"}]
    "gordos": [
        {"id":1, "titulo":"el chiste","chiste":"un chiste"}
        {"id":1, "titulo":"el chiste","chiste":"un chiste"}]
]
}
@app.route('/', methods =['GET'])
def get_books():
    #funcion para devolvder el contenido de "chistes" en formato json
    return jsonify (chistes)

#funcion dentro de flask para correr el API
if __name__ == '__main__':
    app.run(debug=True)