import socket
import termcolor

PORT = 8080
IP = '212.128.253.112'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode('utf-8')
    if msg== 'EXIT':
        cs.send(str.encode('You exited the server, bye!!'))
        print('The client exited the server')
        exit(0)

    print('Message from the client: {}'.format(termcolor.cprint(msg, 'green')))

    cs.send(str.encode(msg))


# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print('Socket ready: {}'.format(serversocket))

while True:
    print('Waiting for connections at: {}, {}'.format(IP, PORT))

    # process the client request
    (clientsocket, addres) = serversocket.accept()
    print('Atetending client: {}'.format(addres))

    process_client(clientsocket)
    # close the socket
    clientsocket.close()
