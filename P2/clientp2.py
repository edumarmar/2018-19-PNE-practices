# Programming our fist client

import socket

# create a socket for communicating with the server)


print('socket created')

PORT= 8080
IP= '212.128.253.103'

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(input(' Type your message: ')))
    s.close()

msg= s.recv(2048).decode('utf-8')
print('message from the server: ')
print(msg)

print('the end')