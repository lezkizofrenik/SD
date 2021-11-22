#!/usr/bin/env python
from bottle import Bottle, run, template, route, get, request, post, response
import json
import os
from json import JSONEncoder

app = Bottle()

# Si sample.json no contiene nada, _rooms se inicializa a vacío
# Si contiene algo, vuelca los datos
if os.stat("sample.json").st_size == 0:
    _rooms=[]
else:
    with open('sample.json', 'r') as openfile: 
        # Reading from json file 
        _rooms = json.load(openfile) 

# Clase Room
class Room:

    def __init__(self, id, cap, equip, occ):
        self.id = id
        self.cap = cap
        self.equip = equip
        self.occ = occ
    # Convierte la clase a json
    def toJson(self):
        return json.loads(json.dumps(self.__dict__))


# Función que vuelca los datos de sample.json a la variable _rooms
def write_file():
    json_object = json.dumps(_rooms, indent = len(_rooms)) 
    with open("sample.json", "w") as outfile: 
        outfile.write(json_object) 

# GET ITEM

@app.route('/room/<id>')
def get_room(id):
# Recorre _rooms en busca de una habitación con el id especificado en el parámetro del path
# Si lo encuentra, devuelve sus datos, de lo contrario devuelve un mensaje de error
    for room in _rooms:
        if str(room['id']) == id:
            return room
        print(room)
    return template("No se ha encontrado una habitación con id ={{id}}", id = id)



# GET ALL
# Convierte _rooms en un diccionario(JSON) y lo devuelve
@app.route('/rooms') 
def getrooms():
    return dict(data=_rooms)

# GET ROOMS BY AVAILABILITY
# Recibe 'free' u 'occupied' a través del parámetro que recibe del path
# de lo contrario, envía un mensaje de error

@app.route('/rooms/available/<occu>')
def get_occupation(occu):
    print(occu)
    if occu == 'free' or occu=='occupied':
        _list =[]
        for room in _rooms:
            print(room)
            # Recorre _rooms en busca de todas las habitaciones libres u ocupadas
            # y lo añade a una lista auxiliar
            if room['occ'] ==occu:
                _list.append(room)
        # Si no ha encontrado ninguna, envía un mensaje de error. De lo contrario,
        # convierte la lista en un diccionario (JSON) y lo envía al servidor
        if len(_list) == 0: 
            return "No hay ninguna habitación con esas características"
        else:
            return dict(data=_list)    
    else:
        return("Introduzca free u occupied")



# POST
@app.route('/new', method='POST')
def post_room():
    try:
        # Recoge los datos que le envían
        data=json.load(request.body)
        # Lo añaden a la lista _rooms
        _rooms.append(data)
        # Actualiza el fichero JSON local
        write_file()
        
    except:
        raise ValueError


    return "true"



# MODIFY



  
# METODO PUT
@app.route('/modify/<id>', method=['POST'])
def mod_room(id):
    try:
        # Recoge los datos modificados que le envían
        data=json.load(request.body)
        # Busca la habitación que desea modificar
        for room in _rooms:
            # Si la encuentra, modifica sus datos y envía un mensaje de éxito
            if str(room['id']) == id:
              
                room['cap'] = data['cap']
                room['equip'] = data['equip']
                room['occ'] = data['occ']
                write_file()
                return "Modificado con éxito"
        # Si no la encuentra, devuelve un mensaje de error
        return "No existe el id proporcionado"

    except:
        raise ValueError
  



# METODO DELETE
@app.route('/delete/<id>', method='POST')
def delete_room(id):
    try:
        # Recorre la lista _rooms en busca de la habitación con el id proporcionado
        for room in _rooms:
            if str(room['id']) == id:
                # Si la encuentra, la elimina de la lista
                _rooms.remove(room)
                # Actualiza el fichero JSON local y envía un mensaje de éxito al servidor
                write_file()
                return "Eliminado con éxito"
        # Si la habitación no existe, devuelve un mensaje de error
        return "No existe el id proporcionado"

    except:
        raise ValueError

# Lanza la API en el socket especificado
run(app, host='localhost', port=8080)