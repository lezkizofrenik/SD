#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 902

status = True  
# Se crea un objeto socket UDP  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Se enlaza al socket especificado
s.bind(('localhost', 1202))

# Mientras el cliente no desee desconectarse:
while(status):
    # Espera a recibir un mensaje del servidor, intermediario de la conversación 
    # con el otro cliente
    print("Esperando mensaje de Persona 1...")
    mensaje_recibido = s.recvfrom(1024)
    # Si el otro cliente se ha desconectado, tú también
    if(str(mensaje_recibido[0])=="b'desconectado'"):
        print("Persona 1 se ha desconectado")
        status=False
    # Si te ha enviado un mensaje:
    else:
        # Muestra el mensaje que te ha enviado el cliente
        print("Persona 1 dice: "+ str(mensaje_recibido[0]))
        print("Dices: ")
        mensaje_enviado = input()
        # Escribes un mensaje y lo envía, codificado, al servidor para que lo 
        # reenvíe al cliente
        s.sendto(mensaje_enviado.encode(), (HOST, 1200))
        # Si el mensaje contenía el comando de desconexión, te desconectas.
        if(mensaje_enviado=="desconectado"):
            print("Te has desconectado")
            status=False

else:
    # Cierra la conexión con el servidor
    s.close()
