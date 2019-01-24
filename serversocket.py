import socket
# create a socket object

serversocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# GET LOCAL MACHINE NAME

host=socket.gethostname()

port=9999

#bind to the port
serversocket.bind((host,port))

# queue upto 5 requests

serversocket.listen(5)

while True:
    #establish a connection
    clientsocket, addr=serversocket.accept()
    print("got a connection from %s" %str(addr))
    msg='Thank you for connecting...! '+"\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()



    
