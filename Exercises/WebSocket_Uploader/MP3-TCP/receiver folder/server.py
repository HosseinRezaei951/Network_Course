import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 6000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))
serverSocket.listen(1)

print(SERVER_HOST)
print("Waiting for any incoming connections ... ")
connectionSocket, addr = serverSocket.accept()
print(addr,"Has connected to the server")


filename = "received.mp3"
file = open(filename,'wb')
while True :
      # get file bytes
      file_data = connectionSocket.recv(4096)
      if not file_data :
            break
      # write bytes on file
      file.write(file_data)
file.close()

print("File has been received successfully. ")

