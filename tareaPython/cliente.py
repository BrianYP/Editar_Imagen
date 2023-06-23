import socket

host ="localhost"
port = 5656

mi_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#version de IPV4
mi_socket.connect((host, port))
print("Iniciamos cliente")
while True:
    enviar = input("cliente: ")#ENVIAMOS INFORMACIÓN
    mi_socket.send(enviar.encode(encoding="ascii", errors="ignore"))#CODIFICADO
    recibir = mi_socket.recv(1024)
    print("Servidor", recibir.decode(encoding="ascii", errors="ignore"))
mi_socket.close()

