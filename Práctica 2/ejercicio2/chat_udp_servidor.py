#!/usr/bin/env python3
#!/usr/bin/env python2
import socket

# Se crea un objeto socket UDP  
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Se enlaza al socket especificado
s.bind(('localhost', 1200))


status = True

# Mientras ninguno de los clientes se desconecten:
while(status):
    # Espera a recibir un mensaje del cliente 1 y lo imprime
    print("Esperando el mensaje de la persona 1")
    mensaje1 = s.recvfrom(1024)
    print("Recibido de Persona 1:["+ str(mensaje1[0]) +"]")
    # Reenvía el mensaje del cliente 1 al cliente 2
    s.sendto(mensaje1[0], ('localhost', 1202))
    # Si el mensaje indicaba que el cliente 1 se ha desconectado,
    # el servidor también se desconecta
    if str(mensaje1[0])=="b'desconectado'":
        status=False
    # Si el cliente 1 no se ha desconectado:
    else:
        # El servidor espera a recibir la respuesta del cliente 2
        print("Esperando el mensaje de la persona 2")
        mensaje2 = s.recvfrom(1024)
        print("Recibo de Persona 2:["+ str(mensaje2[0]) +"]")
        # Reenvía la respuesta del cliente 2 al cliente 1
        s.sendto(mensaje2[0], ('localhost', 1201))

        # Si el cliente 2 se ha desconectado, el servidor también
        if str(mensaje2[0])=="b'desconectado'":
            status=False

# Cierra la conexión
s.close()
print("Desconectado")
