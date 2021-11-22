#!/usr/bin/env python
from bottle import Bottle, run, template, route, get, request, post, response
import json
import os
from json import JSONEncoder

app = Bottle()

if os.stat("sample.json").st_size == 0:
    _rooms=[]
else:
    with open('sample.json', 'r') as openfile: 
        # Reading from json file 
        _rooms = json.load(openfile) 

class Room:

    def __init__(self, id, cap, equip, occ):
        self.id = id
        self.cap = cap
        self.equip = equip
        self.occ = occ

    def toJson(self):
        return json.loads(json.dumps(self.__dict__))



def write_file():
    json_object = json.dumps(_rooms, indent = len(_rooms)) 
    # Writing to sample.json 
    with open("sample.json", "w") as outfile: 
        outfile.write(json_object) 

# GET ITEM

@app.route('/room/<id>')
def get_room(id):
    for room in _rooms:
        if room['id'] == id:
            return room
        print(room)
    return template("<b> No se ha encontrado una habitación con id ={{id}}</b>", id = id)



# GET ALL
@app.route('/rooms') 
def getrooms():
    return dict(data=_rooms)

# GET ROOMS BY AVAILABILITY

@app.route('/rooms/available/<occu>')
def get_occupation(occu):
    print(occu)
    if occu == 'free' or occu=='occupied':
        _list =[]
        for room in _rooms:
            print(room)
            if room['occ'] ==occu:
                _list.append(room)
        if len(_list) == 0: 
            return "<b>No hay ninguna habitación con esas características</b>"
        else:
            return dict(data=_list)    
    else:
        return("<b>Introduzca free u occupied</b>")


# FORMULARIO DEL POST
@app.route('/new') # or @route('/login')
def new():
    return '''
    <div style="display: flex; height:100%; width: 100%; justify-content:center;">
                <div style="display:flex; flex-direction: column; justify-content:center; align-content:center; height:100%">
                <h2> Insertar habitación </h2>
                <form action="/new" method="post" style="display:flex; flex-direction:column; justify-content: space-around">                 
                    <div style="display:flex; justify-content: space-between"><p>id:</p><input name="id" type="text" style="margin: 20px;"/></div>
                    <div style="display:flex; justify-content: space-between"><p>cap:</p> <input name="cap" type="text" style="margin: 20px;"></div>
                    <div style="display:flex; justify-content: space-between"><p>equip:</p> <input name="equip" style="margin: 20px;" type="text" ></div>
                    <div style="display:flex; justify-content: space-between"><p>occ:</p> <input name="occ" type="text" style="margin: 20px;"/></div>
                    <input value="New" type="submit" style="margin: 20px; align-self:center"/><br>
                </form></div></div>
    '''

# POST
@app.route('/new', method='POST')
def post_room():
    try:
        room = Room(request.forms.get('id'), request.forms.get('cap'), request.forms.get('equip'),request.forms.get('occ'))
        _rooms.append(room.toJson())
        write_file()
        
    except:
        raise ValueError


    response.headers['content-type'] = 'application/json'
    return json.dumps({'id': room.id, 'cap': room.cap, 'equip': room.equip, 'occ': room.occ})



# MODIFY

# FORMULARIO DEL PUT
@app.route('/modify/<id>') # or @route('/login')
def new(id):
    for room in _rooms:
        if room['id'] == id:
            print(room)
            return template('''
            <div style="display: flex; height:100%; width: 100%; justify-content:center;">
                <div style="display:flex; flex-direction: column; justify-content:center; align-content:center; height:100%">
                    <h2> Modificar habitación con id={{id}} </h2>
                    <form action="/modify/{{id}}" method="POST" style="display:flex; flex-direction:column; justify-content: space-around">                    
                        <div style="display:flex; justify-content: space-between"><p>cap:</p> <input name="cap" type="text" value= {{cap}} style="margin: 20px;"/></div>
                        <div style="display:flex; justify-content: space-between"><p>equip:</p> <input name="equip" style="margin: 20px;" type="text" value={{equip}} ></div>
                        <div style="display:flex; justify-content: space-between"><p>occ:</p> <input name="occ" type="text" value={{occ}} style="margin: 20px;"/></div>
                        <input value="Modify" type="submit" style="margin: 20px; align-self:center"/><br>
                    </form>
                </div>
            </div>
            ''', id=id, cap= room['cap'], equip=room['equip'], occ=room['occ'])
    return template("<b> No se ha encontrado una habitación con id ={{id}}</b>", id = id)

  
# METODO PUT
@app.route('/modify/<id>', method=['POST'])
def mod_room(id):
    try:
        newroom = Room(id, request.forms.get('cap'), request.forms.get('equip'),request.forms.get('occ'))
        for room in _rooms:
            if room['id'] == id:
                print(room)
                room['cap'] = newroom.cap
                room['equip'] = newroom.equip
                room['occ'] = newroom.occ
                print(room)
                write_file()
                response.headers['Content-Type'] = 'application/json'
                return newroom.toJson()
    except:
        raise ValueError
  

# FORMULARIO DELETE
@app.route('/delete/<id>') # or @route('/login')
def new(id):
    for room in _rooms:
        if room['id'] == id:
            print(room)
            return template('''
             <div style="display: flex; height:100%; width: 100%; justify-content:center;">
                <div style="display:flex; flex-direction: column; justify-content:center; align-content:center; height:100%">
                    <h2> ¿Está seguro que desea eliminar la habitación {{id}}? </h2>
                    <form method="post" action="/delete/{{id}}" style="display:flex; flex-direction:column;">                    
                        <input value="Sí" type="submit" style="margin: 20px; align-self:center" /><br>
                    </form>
                </div></div>
            ''', id=id)
    return template("<b> No se ha encontrado una habitación con id ={{id}}</b>", id = id)

# METODO DELETE
@app.route('/delete/<id>', method='POST')
def delete_room(id):
    try:
        for room in _rooms:
            if room['id'] == id:
                _rooms.remove(room)
                write_file()

    except:
        raise ValueError


run(app, host='localhost', port=8080)