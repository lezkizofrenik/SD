#!/usr/bin/env python3
#!/usr/bin/env python2

import os
import socket

#Guarda la lista de ficheros en el directorio del servidor
list_ficheros = os.listdir('.')
# Crea un objeto socket con el socket especificado
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.bind(('localhost', 1210))
# Se prepara para aceptar una conexión
cliente.listen(1)
# Recibe un objeto socket que le permite comunicarse con el cliente
# y el socket (IP y puerto)
s, addr = cliente.accept() 

# Espera a recibir si quiere una lista del directorio o un archivo
msg = s.recv(1024)
print(msg.decode())
# Si quiere el directorio
if msg.decode() == 'ls':
    # Convierte la lista en un string, lo codifica y lo envia
    s.send(str.encode('\n'.join(list_ficheros), 'utf-8'))
    #Limpia el buffer  
msg=None  
# Espera a recibir el nombre del archivo que quiere
msg=s.recvfrom(1024)
# Recorre la lista de ficheros para ver si el solicitado está
encontrado = False
for i in list_ficheros:
    if msg[0].decode() == i:
        # Si está, envía una notificación confirmandolo
        s.send(str.encode('True', 'utf-8'))
        # Abre el fichero y envía su contenido
        fichero = open(i,'r')
        datos = fichero.read()
        s.send(str.encode(datos, 'utf-8'))
        print("Enviado")
        fichero.close()
        encontrado = True
        datos = None
    
if encontrado == False:
    # Si no está, lo notifica
    s.send(str.encode('False', 'utf-8'))

# Fin del programa y cierra la conexión
cliente.close()
