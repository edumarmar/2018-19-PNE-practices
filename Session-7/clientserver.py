# Programming our fist client

import socket

# create a socket for communicating with the server)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('socket created')

PORT= 8080
IP= '212.128.253.81'
s.connect((IP, PORT))


while True:

    message= input(' Type your message: ')
    s.send(str.encode(message))

msg= s.recv(2048).decode('utf-8')
print('message from the server: ')
print(msg)

s.close()

print('the end')