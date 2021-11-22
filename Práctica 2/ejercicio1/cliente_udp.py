#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 1200

# Creamos un objeto socket UDP
s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Envía un mensaje codificado al socket especificado
s_udp.sendto(b"soy el cliente", (HOST, PORT))
# Cierra la conexión
s_udp.close()
