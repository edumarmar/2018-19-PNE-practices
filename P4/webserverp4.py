import socket
import termcolor

IP = "212.128.253.110"
PORT = 8080
MAX_OPEN_REQUESTS = 5


def process_client(cs, response_msg=None):
    """Process the client request.
    Parameters:  cs: socket for communicating with the client"""

    msg = cs.recv(2048).decode("utf-8")

    print()
    print("Request message: ")
    termcolor.cprint(msg, 'green')

    #reading the first line of the received msg (the request)

    request = msg.split('\n', 1)[0]
    i_final = (request.find(' ', 4))
    req = request[4:i_final]
    print(req)
    if req== '/':
        file= 'index.html'
    elif req== '/blue':
        file= 'blue.html'
    elif req== '/pink':
        file= 'pink.html'
    else:
        file='error.html'

    with open(file, 'r') as f:
        content = f.read()

    status_line = 'HTTP/1.1 200 OK\r\n'
    header = 'Content-Type: text/html\r\n'
    header += 'Content-Length: {}\r\n'.format(len(str.encode(content)))


    response_msg = status_line + header + '\r\n' + content

    cs.send(str.encode(response_msg))

    # Close the socket
    cs.close()


# MAIN PROGRAM

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUESTS)

print("Socket ready: {}".format(serversocket))

while True:

    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    print("Attending connections from client: {}".format(address))

    process_client(clientsocket)