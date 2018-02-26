import socket

if __name__ == '__main__':
    direccion = socket.gethostbyname('maps.google.com')
    mensaje = ' {} es {} '.format('maps.google.com', direccion)
    print(mensaje)


