import socket
from Seqp3 import Seq


PORT = 8001
IP = '212.128.253.105'
MAX_OPEN_REQUEST = 5


# Processing the message from the client: the entire message, the sequence and the operations
def process_client(cs):
    msg = cs.recv(2048).decode('utf-8')
    msg = msg.strip(' \n')
    asdf = msg.partition('\n')
    seq = asdf[0].upper()

    try:
        data= msg.split('\n')
        operations = data[1:]
    except:
        operations= None

    print('Message from the client: {}'.format(msg))

    return msg, seq, operations

# Function that checks if the user wants to see if the server is alive or
# if the data introduced is correct.
def check(msg, seq, operations):
    checkvar= ['complement', 'len', 'reverse', 'countA','countC','countG','countT', 'percA','percC','percG','percT',]

    for operation in operations:
        if not operation in checkvar:
            checkvar= 'ERROR'

    if msg == '':
        return 'ALIVE'
    elif (seq.upper().strip('ACTG ')!= '') or checkvar== 'ERROR':
        return 'ERROR'
    else:
        return 'OK'

# Creating a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((IP, PORT))
serversocket.listen(MAX_OPEN_REQUEST)

print('Socket ready: {}'.format(serversocket))

while True:
    print('Waiting for connections at: {}, {}'.format(IP, PORT))
    # process the client request
    (clientsocket, addres) = serversocket.accept()
    print('Atetending client: {}'.format(addres))

    # Calling the functions
    msg, seq, operations=process_client(clientsocket)
    resp=check(msg, seq, operations)


    if resp=='ERROR' or resp=='ALIVE':
        clientsocket.send(str.encode(resp))

    # Main program to generate the information requested by the user
    else:
        response= '\nOK'
        i = Seq(seq)
        ops = {'len': i.len(),
                      'complement': i.complement(),
                      'reverse': i.reverse(),
                      'countA': i.count('a'),
                      'countT': i.count('t'),
                      'countG': i.count('g'),
                      'countC': i.count('c'),
                      'percA': i.perc('a'),
                      'percC': i.perc('c'),
                      'percT': i.perc('t'),
                      'percG': i.perc('g')}

        for operation in operations:
            data= ops[operation]
            data=str(data)
            response+='\n'+ data

        # Sending the information requested
        clientsocket.send(str.encode(response))

    # close the socket
    clientsocket.close()
