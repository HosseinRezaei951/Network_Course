import socket
import sys

SERVER_HOST = 'localhost'
SERVER_PORT = 6000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((SERVER_HOST,SERVER_PORT))
 

while True:
    data = input("Enter your message: ")
    clientSocket.send(data.encode())
    modifiedData = clientSocket.recv(1024)
    print("Modified data : " , modifiedData.decode())


clientSocket.close()