# client application
import socket
import sys

# server address and port 
serverAddrConst = 'localhost'
serverPort = 4000

# AF_INET: we are using IPv4
# Sock_DGRAM: UDP connection (Datagrams)
# making the socket with below configuration
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('input your sentence: ')

    # here the client port isn't important and OS handles Port itself
    clientSocket.sendto(msg.encode(), (serverAddrConst, serverPort))
    # server Address is just port address but in order to send a packet next time 
    # we have to use tuple of ip and port so ServerAddrConst and serverAddr are two
    # different objects 

    modifiedSentence, serverAddr = clientSocket.recvfrom(1024)
    print("Modified sentence received from server : ", modifiedSentence.decode())
