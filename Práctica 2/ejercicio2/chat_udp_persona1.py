#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 901

status = True    
# Se crea un objeto socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Se enlaza al socket especificado
s.bind(('localhost', 1201))
# Mientras el cliente no desee desconectarse:
while(status):
    print("Dices: ")
    mensaje_enviado = input()
    # Envío un mensaje codificado al servidor a través del socket
    s.sendto(mensaje_enviado.encode(), (HOST, 1200))
    # Si desea desconectarse, se sale del bucle y se cierra la conexión
    if(mensaje_enviado=="desconectado"):
        print("Te has desconectado")
        status=False
    # Si desea enviar un mensaje:
    else:
        # Espera a recibir un mensaje del servidor, que reenvía los mensajes del otro cliente
        print("Esperando mensaje de Persona 2...")
        mensaje_recibido = s.recvfrom(1024)
        # Si el otro cliente se ha desconectado, éste también
        if(str(mensaje_recibido[0])=="b'desconectado'"):
            print("Persona 2 se ha desconectado")
            status=False
        # Si no, muestra el mensaje que el cliente te ha enviado
        else:
            print("Persona 2 dice: "+ str(mensaje_recibido[0]))

else:
    # Cierra la conexión
    s.close()
