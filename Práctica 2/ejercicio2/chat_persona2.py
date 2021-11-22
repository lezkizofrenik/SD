#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 1202
# Variable que determina si el cliente estará activo
status = True    
# Creamos un objeto socket UTP y lo enlazamos al socket especificado
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Mientras el cliente esté activo:
while(status):
    # Espera a recibir un mensaje del servidor
    mensaje_recibido = s.recv(1024).decode()
    # Si el mensaje indica que la otra persona se ha desconectado,
    # éste también se desconecta.
    if(mensaje_recibido =="desconectado"):
        print("La Persona 1 se ha desconectado")
        status=False
    # Si la otra persona le ha enviado un mensaje:
    else:
        #Muestra el mensaje recibido
        print("Persona 1 dice: "+ mensaje_recibido)
        print("Dices: ")
        # Codifica la respuesta
        mensaje_enviado = str.encode(input(), 'utf-8')
        # Envía el mensaje de respuesta al servidor
        s.send(mensaje_enviado)
        # Si el mensaje era para desconectarse, te desconectas
        if(mensaje_enviado.decode()=="desconectado"):
            print("Te has desconectado")
            status=False

else:
    #Se cierra la conexión
    s.close()
