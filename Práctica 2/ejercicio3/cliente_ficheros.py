#!/usr/bin/env python3
#!/usr/bin/env python2
import os
import socket

# Se crea un objeto socket tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Se enlaza el objeto al socket especificado
s.connect(('localhost', 1210))
print("Introduce el comando ls o el fichero que desee: ")
# El usuario debe introducir si desea listar el directorio 
# o el nombre del archivo que desea descargar
petic = None
petic = input()
# Se codifica y se envía al servidor
s.send(str.encode(petic, 'utf-8'))
# Si pide listar los archivos disponibles:
if petic == 'ls':
    # Espera a recibir la lista
    fichs = s.recv(1024)

    # Muestra lista de ficheros
    print("Ficheros disponibles: ")
    print(fichs.decode())
    # Introduce el nombre del archivo que desea descargar
    print("Indique qué fichero desea descargar: ")
    petic=None
    petic = input()
    #Pedimos dicho fichero

# Codifica y envía el nombre del fichero que desea descargar
s.send(str.encode(petic, 'utf-8'))
# Espera a recibir si el archivo existe o no
fichero_encontrado = s.recv(1024).decode()

# Si no existe, muestra un mensaje de error
if fichero_encontrado == 'False':
    print("No se encuentra el fichero que ha solicitado")

# Si existe:
else:
    # Recibe el contenido del fichero
    fichero_2 = s.recv(1024)
    # Crea un archivo con el mismo nombre y guarda el contenido dentro
    datos = open("../recibido/" + petic,'w')
    datos.write(fichero_2.decode())
    datos.close()
    print("Archivo recibido")
    fichero_2 = None

# Cierra la conexión
s.close()
