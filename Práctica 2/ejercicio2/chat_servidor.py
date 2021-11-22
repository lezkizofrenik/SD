#!/usr/bin/env python3
#!/usr/bin/env python2
import socket

#Se crean un objeto socket por cada cliente con el que desea comunicarse
persona1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
persona2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se enlazan los objetos con los sockets especificados
persona1.bind(('localhost', 1201))
persona2.bind(('localhost', 1202))
# Se prepara para aceptar una conexión
persona1.listen(1)
persona2.listen(1)
# Aceptan las conexiones y reciben los objetos para comunicarse con los clientes
# y los sockets (IP y puerto)
s_cliente1, addr1 = persona1.accept()  
s_cliente2, addr2 = persona2.accept()

status = True
# Mientras los clientes sigan conectados:
while(status):
    # Espera a recibir un mensaje de 1024 bytes del primer cliente
    print("Esperando el mensaje de la persona 1")
    mensaje1 = s_cliente1.recv(1024)

    print("Recibo:["+ str(mensaje1) +"] del cliente con la direccion "+str(addr1))
    # Reenvia el mensaje del cliente 1 al cliente 2
    s_cliente2.send(mensaje1)

    #Si el cliente 1 se ha desconectado, sale del bucle y se cierran las conexiones
    if mensaje1.decode() == "desconectado":
        status=False
    #Si no:
    else:
        # Espera a que el cliente 2 responda
        print("Esperando el mensaje de la persona 2")
        mensaje2 = s_cliente2.recv(1024)
        print("Recibo:["+ str(mensaje2) +"] del cliente con la direccion "+str(addr2))

        # Reenvía el mensaje del cliente 2 al cliente 1
        s_cliente1.send(mensaje2)

        # Si en el mensaje dice que se ha desconectado, sale del bucle y se cierran las conexiones
        if mensaje2.decode() == "desconectado":
            status=False

# Cierre de conexiones
s_cliente1.close()
s_cliente2.close()
