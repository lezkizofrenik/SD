#!/usr/bin/env python3
#!/usr/bin/env python2

import socket
import requests
import json

HOST = 'localhost'
PORTC = 1213

# Se crea un objeto socket para comunicarse con el cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se enlaza el objeto con el socket especificado
cliente.bind((HOST, PORTC))
# Se prepara para aceptar una conexión
cliente.listen(1)
# Aceptan la conexion y recibe el objeto para comunicarse con el cliente
# y el socket
s, addr1 = cliente.accept()
# Mientras el cliente siga conectado:
status = True

while(status):
    # Espera a recibir la opción que desea el cliente
    print("Esperando que el cliente elija una opción")
    opt = s.recv(1024).decode()
    # OPCION 1, ALTA
    if opt is "1":
        # Recibe un JSON con los datos de la habitación que desea hacer el alta
        roomJson = s.recv(1024).decode()
        print("recibido: " + roomJson)
        # Envía los datos a la dirección correspondiente
        resolucion = requests.post('http://localhost:8080/new', data=roomJson)
        # Si la operación de la api se ha realizado con éxito, devolverá
        # un código de éxito junto a la respuesta de la api
        if resolucion.ok == True:
            # Envía el mensaje devuelto por la api al cliente
            s.send(str.encode(resolucion.text, 'utf-8'))
  
    else:
        # OPCION 2, MODIFICAR
        if opt is "2":
            # Recibe un JSON en formato string con los datos de la habitación que desea hacer el alta
            roomJson = s.recv(1024).decode()   
            # Extrae el json del string para obtener el id y construir
            # la url a la que deberá acceder para modificar la habitación  
            jsonv=json.loads(roomJson)
            url = "http://localhost:8080/modify/" + str(jsonv['id'])
            # Envía a la url correspondiente los datos modificados
            resolucion = requests.post(url, data=roomJson)
            # Si la operación de la api se ha realizado con éxito, devolverá
            # un código de éxito junto a la respuesta de la api
            if resolucion.ok == True:
                s.send(str.encode(resolucion.text, 'utf-8'))
        else:
            # OPERACION 3, GET ALL
            if opt is "3":
                resolucion = requests.get('http://localhost:8080/rooms')
                s.send(str.encode(resolucion.text, 'utf-8'))

            else:
                # OPERACION 4: GET ONE ROOM
                if opt is "4":
                    # Recibe el id de la habitación que desea ver
                    id = s.recv(1024).decode()    
                    # construye la url correspondiente a la que debe solicitar el dato  
                    url = "http://localhost:8080/room/" + id
                    # Realiza la petición
                    resolucion = requests.get(url)
                    # Si la operación de la api se ha realizado con éxito, devolverá
                    # un código de éxito junto a la respuesta de la api
                    if resolucion.ok == True:
                         s.send(str.encode(resolucion.text, 'utf-8'))
                else:
                    # OPERACION 5: HABITACIONES LIBRES/OCUPADAS

                    if opt is "5":
                        # Obtiene 'free' u 'occupied' según haya solicitado
                        free = s.recv(1024).decode() 
                        # construye la url correspondiente a la que debe solicitar el dato  
                        url = "http://localhost:8080/rooms/available/" + free
                        # Realiza la petición
                        resolucion = requests.get(url)
                        # Si la operación de la api se ha realizado con éxito, devolverá
                        # un código de éxito junto a la respuesta de la api
                        if resolucion.ok == True:
                            s.send(str.encode(resolucion.text, 'utf-8'))
                    else:
                        # OPERACION 6: ELIMINAR HABITACION

                        if opt is "6":
                            # Obtiene el id de la habitación que desea eliminar
                            id = s.recv(1024).decode() 
                            # Construye la url correspondiente     
                            url = "http://localhost:8080/delete/" + id
                            # Realiza la petición
                            resolucion = requests.post(url)
                            # Si la operación de la api se ha realizado con éxito, devolverá
                            # un código de éxito junto a la respuesta de la api
                            if resolucion.ok == True:
                                s.send(str.encode(resolucion.text, 'utf-8'))

                        else:
                            # OPCION 7: SALIR
                            if opt is "7":
                                status = False
else:
    #Cierra la conexión
    s.close()   
