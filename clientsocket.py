import socket
 # create a socket object

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#get local machine name

host=socket.gethostname()

port=9999

# connection to the hostname on the port

s.connect((host,port))

#recieve no more than 1024 byte

msg=s.recv(1024)
s.close()

print(msg.decode('ascii'))
