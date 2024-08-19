import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 6000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



print("Connected ... ")

filename = input(str("Please enter the filename of the file: "))

# open file
with open(filename,'rb') as file :
       # send file
       file_data = file.read(4096)
       while(file_data):
              if(clientSocket.sendto(file_data,(SERVER_HOST,SERVER_PORT))):
                     file_data = file.read(4096) 
       
       # close connection
       clientSocket.close()
       print("Data has been transmitted successfully. ")
       