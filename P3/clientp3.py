import socket


# SERVER IP, PORT
IP = "212.128.253.105"
PORT = 9000

while True:
    msgs=[]
    while True:
        msg = input("> ") + '\n'
        msgs.append(msg)
        if msg== '' + '\n':
            break

    
    send=''.join(msgs)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server (IP, PORT)
    s.connect((IP, PORT))

    # Send the request message to the server
    s.send(str.encode(send))

    # Receive the servers respoinse
    response = s.recv(2048).decode('utf-8')

    # Print the server's response
    print("Response: {}".format(response))

    s.close()