# server application

import socket
import sys

# AF_INET: we are using IPv4
# Sock_DGRAM: UDP connection (Datagrams)
# making the socket with below configuration
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


HOST = 'localhost'
PORT = 4000
# Bind the address and port to socket
serverSocket.bind((HOST, PORT))


while True:
    # data will be filled by msg and addrs is client address
    # 1024 is chunck size(?)
    data, addr = serverSocket.recvfrom(1024)

    # received massage is in bytes so first we decode it and make it string
    # after these steps we make all characters to uppercase ones
    modifiedData = str(data.decode()).upper()
    print("Message: ", data.decode())
    print(modifiedData)
    # modifeid data is string so we encoding it to bytes and sending it to 
    # client address
    serverSocket.sendto(modifiedData.encode(), addr)
