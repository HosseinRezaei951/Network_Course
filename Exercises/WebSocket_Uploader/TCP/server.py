import socket
import sys

SERVER_HOST = 'localhost'
SERVER_PORT = 6000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))

serverSocket.listen(2)
print("Server is ready ... on port ", SERVER_PORT)
connectionSocket, addr = serverSocket.accept()
while True:
    data = connectionSocket.recv(1024)
    modifiedData = str(data.decode()).upper()
    print("Message: ", modifiedData)
    connectionSocket.send(modifiedData.encode())

connectionSocket.close()

