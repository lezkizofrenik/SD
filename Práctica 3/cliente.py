#!/usr/bin/env python3
#!/usr/bin/env python2

import os
import sys
import socket
import json
import ast

HOST = 'localhost'
PORT = 1213

status = True
sec = True

# Creamos un objeto socket UTP y lo enlazamos al socket especificado
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# Mientras que el cliente no desee desconectarse:
while(status):
    # Elige una opción
    print("Elija qué opción desea realizar:\n\t1. Dar de alta una nueva habitación\n\t2. Modificar los datos de una habitación existente\n\t3. Consultar la lista de habitaciones existentes\n\t4. Consultar los datos de una habitación específica\n\t5. Consultar la lista de habitaciones ocupadas o libres\n\t6. Eliminar una habitación existente \n\t7. Salir\n")
    opt = input()

    # OPCIÓN 1, ALTA
    if opt is "1":
        # Codifica la opción deseada para enviarla al servidor
        opcion = str.encode("1", 'utf-8')
        s.send(opcion)
        # Introduce el id de la habitación (atributo 1)
        print("Introduzca el identificador de la habitación:")
        userInput = input()
        # Comprueba si es un dígito, de lo contrario lanza un error
        try:
            roomId = int(userInput)
        except ValueError:
            print("ATENCION: El identificador debe ser un dígito.")
            sys.exit()
        # Introduce el nº de plazas de la habitación (atributo 2)
        print("Introduzca el número de plazas de la habitación:")
        # Vuelve a comprobar si son dígitos
        userInput = input()
        try:
            roomCap = int(userInput)
        except ValueError:
            print("ATENCION: La capacidad de la habitación debe ser un dígito.")
            sys.exit()

        # Introduce el equipamiento de la habitación (atributo 3)
        print("Introduzca la lista de equipamiento (escriba todo el equipamiento separado por comas y pulse 'Intro' cuando termine):")
        roomEqui = input()

        # Introduce si la habitación está ocupada o no
        print("¿Se encuentra la habitación ocupada? ([S]i/[N]o):")
        ocu = input()
        # Comprueba si la opción introducida cumple con el formato requerido
        while(ocu != 's' and ocu != 'n'):
            print("Opción no valida. Escriba 'S' si la habitación está ocupado o 'N' si la habitación esta libre.")
            ocu = input()

        # Si está ocupada, asigna 'ocuppied' al atributo, de lo contrario asigna 'free'
        if ocu is 's':
            roomOccu = 'occupied'
        else:
            if ocu is 'n':
                roomOccu = 'free'

        # Crea un diccionario con los atributos introducidos
        room = {'id': roomId,
                'cap': roomCap,
                'equip': roomEqui,
                'occ': roomOccu}

        # Lo convierte a JSON
        roomJson = json.dumps(room)
        # Envía el JSON al servidor, convirtiendolo a bytes
        s.sendall(bytes(roomJson, encoding= 'utf-8'))
        # Espera respuesta del servidor y lo muestra por terminal
        respuesta = s.recv(1024).decode()
        print(respuesta)
    else:
        # OPCION 2, MODIFICAR
        if opt is "2":
            # Codifica la opción deseada para enviarla al servidor

            opcion = str.encode("2", 'utf-8')
            s.send(opcion)
            # Introduce el id de la habitación que desea modificar
            print("Introduzca el identificador de la habitación que quiere modificar:")
            roomId = input()
            # Comprueba que se han introducido dígitos
            try:
                roomId = int(roomId)
            except ValueError:
                print("ATENCION: El identificador debe ser un dígito.")
                sys.exit()
            # Introduce los atributos correspondientes y comprueba  que su formato es correcto
            print("Introduzca el número de plazas de la habitación:")
            roomCap = input()
            try:
                roomCap = int(roomCap)
            except ValueError:
                print("ATENCION: La capacidad de la habitación debe ser un dígito.")
                sys.exit()

            print("Introduzca la lista de equipamiento (escriba todo el equipamiento separado por comas y pulse 'Intro' cuando termine):")
            roomEqui = input()

            print("¿Se encuentra la habitación ocupada? (s/n):")
            ocu = input()
            while(ocu != 's' and ocu != 'n'):
                print("Opción no valida. Escriba 'S' si la habitación está ocupado o 'N' si la habitación esta libre.")
                ocu = input()

            if ocu is 's':
                roomOcu = "occupied"
            else:
                if ocu is 'n':
                    roomOcu = "free"

            room = {'id': roomId,
                    'cap': roomCap,
                    'equip': roomEqui,
                    'occ': roomOcu}

            # Lo convierte a JSON
            roomJson = json.dumps(room)
            # Envía el JSON al servidor, convirtiendolo a bytes
            s.sendall(bytes(roomJson, encoding= 'utf-8'))
            # Espera respuesta del servidor y lo muestra por terminal
            respuesta = s.recv(1024).decode()
            print(respuesta)
        else:
            # OPERACION 3, GET ALL
            if opt is "3":
                # Codifica la opción deseada para enviarla al servidor
                opcion = str.encode("3", 'utf-8')
                s.send(opcion)
                # Espera la respuesta del servidor y la muestra
                respuesta = s.recv(1024).decode()
                print(respuesta)
            else:
                # OPERACION 4: GET ONE ROOM
                if opt is "4":
                    # Codifica la opción deseada para enviarla al servidor
                    opcion = str.encode("4", 'utf-8')
                    s.send(opcion)
                    # Introduce el nº de la habitación que desea y comprueba si son dígitos,
                    # de lo contrario, lanza una excepcion
                    print("Introduzca el identificador de la habitación:")
                    userInput = input()
                    try:
                        idNum = int(userInput)
                    except ValueError:
                        print("ATENCION: El identificador debe ser un dígito.")
                        sys.exit()
                    # Convierte el número a string para codificarlo y enviarlo al servidor
                    roomId = str(idNum)
                    s.send(bytes(roomId, encoding='utf-8'))
                    # Espera la respuesta del servidor y la muestra
                    respuesta = s.recv(1024).decode()
                    print(respuesta)
                else:
                    # OPERACION 5: HABITACIONES LIBRES/OCUPADAS
                    if opt is "5":
                        # Codifica la opción deseada para enviarla al servidor

                        opcion = str.encode("5", 'utf-8')
                        s.send(opcion)

                        # Introduce si desea ver habitaciones libres u ocupadas y comprueba si el formato es correcto
                        print("¿Qué lista desea ver?\n\t1. Habitaciones libres\n\t2. Habitaciones ocupadas")
                        op = input()

                        while(op != "1" and op != "2"):
                            print("ATENCIÓN: Opción no válida. Introduzca '1' si desea ver las habitaciones libres y '2' si desea ver las habitaciones ocupadas.")
                            op = input()

                        if op is "1":
                            opti = "free"
                        else:
                            if op is "2":
                                opti = "occupied"

                        # Codifica la opción que desea ver para enviarla al servidor
                        s.send(bytes(opti, encoding='utf-8'))
                        # Espera a la respuesta del servidor e imprime la respuesta
                        respuesta = s.recv(1024).decode()
                        print(respuesta)
                    else:
                        # OPERACION 6: ELIMINAR HABITACION
                        if opt is "6":
                            # Codifica la opción deseada para enviarla al servidor
                            opcion = str.encode("6", 'utf-8')
                            s.send(opcion)
                            # Introduce el id de la habitación deseada y comprueba que se han introducido dígitos
                            # de lo contrario, lanza un error
                            print("Introduzca el identificador de la habitación:")
                            userInput = input()
                            try:
                                idNum = int(userInput)
                            except ValueError:
                                print("ATENCION: El identificador debe ser un dígito.")
                                sys.exit()
                            # Convierte los dígitos del número de la habitación a string para codificarlo y enviarlo
                            # al servidor
                            roomId = str(idNum)
                            s.send(bytes(roomId, encoding='utf-8'))
                            # Espera la respuesta del servidor y muestra el resultado
                            respuesta = s.recv(1024).decode()
                            print(respuesta)

                        else:
                            # OPCION 7:SALIR
                            if opt is "7":
                                # Codifica la opción deseada para enviarla al servidor
                                opcion = str.encode("7", 'utf-8')
                                # Notifica al servidor y al flujo que desea acabar la comunicación
                                s.send(opcion)
                                status = False
                            else:
                                print("ATENCIÓN: Opción inválida")
else:
    # Cierrra la conexión con el servidor
    s.close()   