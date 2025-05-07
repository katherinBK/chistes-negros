from flask import Flask,jsonify
import requests
import json

app = Flask(__name__)
#Arreglo que contiene los chistes
chistes = {
    "mujeres": [
        {"id": 1, "capi machista": "capitan america luego de ser descongelado y ver como las mujeres hablan pedir permiso", "chiste": "un chiste"},
        {"id": 2, "NenaSaludando": "porque la niña se cayo de la hamaca? porque no tenia brazos xdddd", "abuelita": "persona1:tu abuela es abuelita?. persona2:no porque?.... persona1:porque la vi debajo de un camion"}
        {"id": 2, "Coches": "una mujer luego de tener un gran dia: Muy bien ire a chocar con el auto", "Ella e callaita": "mama en la escuela me dicen guitarra.. porque me toca el profe de musica"}
    ],
    "gordos": [
        {"id": 1, "titulo": "PROF FABIAN GORDASO SIMP", "chiste": "un chiste"},
        {"id": 2, "titulo": "ola soy una pelota.", "chiste": "otro chiste"}
    ],
    "negros": [
        {"id": 1, "titulo": "cuando un negro ve un latigo le da nostalgia o miedo", "africano": "usi un africano dice pan comido es facil o dificil?"},
        {"id": 2, "titulo": "TRAEME UN CAFE, NEGRO", "disney haz buenos live action": "que es mas negro que los chistes de humor negro??: los live action de disney"}
        {"id": 2, "titulo": "si pepito tiene 5 manzanas y juan le roba 2.. de que color es juan?", "disney haz buenos live action": "que es mas negro que los chistes de humor negro??: los live action de disney"}
    ],
    "judios": [
        {"id": 1, "judios vrgs": "¿En qué se diferencia un judío de una pizza? Que la pizza no grita cuando la meten al horno.", "chiste": "un chiste"},
        {"id": 2, "titulo": "TRAEME UN CAFE, NEGRO", "pistolAfricana": "cual es la pistola mas dificil de conseguir en africa? la pistola de agua"}
    ],
    "random": [
        {"id": 1, "vegetal": "¿Cuál es la parte más difícil de comer un vegetal? La silla de ruedas.", "CIEGOOOODEMRD": "porque el niño ciego se murio en la pelicula? porque no vio el trailer."},
        {"id": 2, "legoo": "tenia un amigo que le apodaron lego.. porque lo encontraron en pedazos en una bolsa", "": ""}   
        {"id": 2, "SYSTEMofADown": "cual es la banda favorita de unos niños con sindrome de down?????-......... es SystemOfA down", "huerfanos": "¿Por qué los huérfanos no juegan a las escondidas? Porque nadie va a buscarlos."}
    ]
 
 }
@app.route('/', methods =['GET'])
def get_books():
    #funcion para devolvder el contenido de "chistes" en formato json
    return jsonify (chistes)

#funcion dentro de flask para correr el API
if __name__ == '__main__':
    app.run(debug=True)