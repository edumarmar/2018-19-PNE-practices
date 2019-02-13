# Programming our fist client

import socket
from seqp2 import Seq


# create a socket for communicating with the server)


print('socket created')

PORT= 8081
IP= '212.128.253.102'



while True:
    sequence= input('Enter the sequence that you want to analyze: ')
    s1 = Seq(sequence)
    compl=(s1.complement())
    rev=(s1.reverse())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))
    s.send(str.encode(compl))
    s.send(str.encode(rev))
    s.close()

msg= s.recv(2048).decode('utf-8')
print('message from the server: ')
print(msg)

print('the end')