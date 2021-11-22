#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 1201
# Variable que determina si el cliente estará activo
status = True  

# Creamos un objeto socket UTP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Lo enlazamos al socket especificado
s.connect((HOST, PORT))
# Mientras el cliente esté activo:
while(status):
    print("Dices: ")
    # Codifico el mensaje que deseo enviar
    mensaje_enviado = str.encode(input(), 'utf-8')
    # Envío el mensaje al socket
    s.send(mensaje_enviado)
    # Si el cliente ha enviado un mensaje:
    if(mensaje_enviado.decode() != "desconectado"):
        # Espera a recibir un mensaje 
        mensaje_recibido = s.recv(1024).decode()
        # Si el mensaje recibido indica que la otra persona
        # se ha desconectado, éste también se desconecta
        if(mensaje_recibido=="desconectado"):
            print("La Persona 2 se ha desconectado")
            status=False
        # Si la otra persona ha escrito un mensaje, lo muestra
        else:
            print("Persona 2 dice: "+ mensaje_recibido)
    # Si el cliente deseaba desconectarse, se desconecta
    else:
        print("Te has desconectado")
        status=False

else:
    # Cierra la conexión
    s.close()
