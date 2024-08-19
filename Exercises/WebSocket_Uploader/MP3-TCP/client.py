import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 6000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((SERVER_HOST,SERVER_PORT))


print("Connected ... ")

filename = input(str("Please enter the filename of the file: "))

# open file
with open(filename,'rb') as file :
       # send file
       file_data = file.read()
       clientSocket.sendall(file_data)

       # close connection
       clientSocket.close()
       print("Data has been transmitted successfully. ")
       