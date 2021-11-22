#!/usr/bin/env python3
#!/usr/bin/env python2
import socket

# Creamos un objeto socket TCP
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Asociamos el objeto al socket especificado
socketServidor.bind(('localhost', 1200))
# Se prepara para aceptar un cliente
socketServidor.listen(1)
print("Esperando")
# Se queda esperando a que un cliente se conecte y devuelve un objeto socket para comunicarse 
# con él y su socket (IP y puerto)
s_cliente, addr = socketServidor.accept()
# Recibe un mensaje de 1024 bytes como máximo
mensaje = s_cliente.recv(1024)
print("Recibo:["+ str(mensaje.decode()) +"] del cliente con la direccion "+str(addr))
# Envía un mensaje codificado al cliente
s_cliente.send(str.encode('Hola, cliente, soy el servidor','utf-8'))
# Cierra la conexión del cliente
s_cliente.close()
# Cierra la conexión del servidor
socketServidor.close()
