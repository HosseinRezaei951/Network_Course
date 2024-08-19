import socket, threading 

print_lock = threading.Lock() 

# thread fuction 
class threaded(threading.Thread): 
    def __init__(self,connection, address):
        threading.Thread.__init__(self)
        self.csocket = connection
        self.addr = address
        print ("New connection added: ", address)

    def run(self):
        while True:
            request = self.csocket.recv(1024).decode('utf-8')
            # GET / HTTP/1.0
            # data received from client 
            if not request:
                break
            
            print(request)
            string_list = request.split(' ')     # Split request from spaces
            if len(string_list) > 2 :
                method = string_list[0]
                requesting_file = string_list[1]

                print('Client ',self.addr,' request ',requesting_file)

                myfile = requesting_file.split('?')[0] # After the "?" symbol not relevent here
                myfile = myfile.lstrip('/')
                if(myfile == ''):
                    myfile = 'index.html'    # Load index file as default

                try:
                    file = open(myfile,'rb') # open file , r => read , b => byte format
                    response = file.read()
                    file.close()

                    header = 'HTTP/1.1 200 OK\n'

                    if(myfile.endswith(".jpg")):
                        mimetype = 'image/jpg'
                    elif(myfile.endswith(".css")):
                        mimetype = 'text/css'
                    else:
                        mimetype = 'text/html'

                    header += 'Content-Type: '+str(mimetype)+'\n\n'

                except Exception as e:
                    header = 'HTTP/1.1 404 Not Found\n\n'
                    response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')

                final_response = header.encode('utf-8')
                final_response += response
                self.csocket.send(final_response)
                print(requesting_file,'sent to clien',self.addr[1])
                break

        print ("Client at ", self.addr , " disconnected...")
        # connection closed 
        self.csocket.close()
        print('Bye\n')
    
        
 
def Main():
    HOST,PORT = '192.168.39.135',80
    
 
    my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    my_socket.bind((HOST,PORT))
   
    print("socket binded to post", PORT) 
  
    # put the socket into listening mode 
    print("socket is listening") 
  
    # a forever loop until client wants to exit 
    while True:
        my_socket.listen(5)
        # establish connection with client 
        connection,address = my_socket.accept()
        
        newthread = threaded(connection, address)
        newthread.start() 
  
if __name__ == '__main__':
    Main()