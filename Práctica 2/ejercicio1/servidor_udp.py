#!/usr/bin/env python3
#!/usr/bin/env python2

import os
import socket

HOST= 'localhost'
PORT = 1200

# Creamos un objeto socket UDP
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Asociamos el objeto al socket especificado
s_udp.bind((HOST, PORT))

print("Esperando")
# Esperamos a recibir un mensaje de 1024 bytes como máximo
mensaje = s_udp.recvfrom(1024)

print("Recibido: " + str(mensaje))
#Se cierra la conexión
s_udp.close()
