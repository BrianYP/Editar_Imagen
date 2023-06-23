import socket

host ="localhost"
port = 5656
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host,port))
servidor.listen(1)
print("Servidor en espera de conexiones")
conexionActiva, addr= servidor.accept()

while True:
    recibido = conexionActiva.recv(1024)
    print("Cliente escribio: ",recibido.decode(encoding="ascii", errors="ignore"))
    enviar = input("Servidor: ")
    conexionActiva.send(enviar.encode(encoding="ascii", errors="ignore"))
conexionActiva.close()