import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 6000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((SERVER_HOST, SERVER_PORT))


print(SERVER_HOST)
print("Waiting for any incoming connections ... ")


filename = "received.mp3"
file = open(filename,'wb')
while True :
      # get file bytes
      file_data, addr = serverSocket.recvfrom(4096)
      if not file_data :
            break
      # write bytes on file
      file.write(file_data)
file.close()

print("File has been received successfully. ")

