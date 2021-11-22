#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 1200

# Creamos un objeto socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Enlazamos el objeto al socket especificado
s.connect((HOST, PORT))
# Enviamos el mensaje codificado
s.send(str.encode('Hola servidor','utf-8'))
# Espera a recibir un mensaje
mensaje = s.recv(1024)
print("RECIBIDO: ["+ str(mensaje.decode())+"] del servidor")
# Cierra la conexión
s.close()
