#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

HOST= 'localhost'
PORT = 1300
# Variable que determina si el cliente estará activo
status = True    
# Creamos un objeto socket UTP y lo enlazamos al socket especificado
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while(status):
    opt = s.recv(1024).decode()

    if