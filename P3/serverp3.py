import socket
from Seqp3 import Seq


PORT = 9000
IP = '212.128.253.105'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode('utf-8')
    resp=msg
    print('Message from the client: {}'.format(msg))
    return msg


def ping(msg):
    resp=''
    if msg == '' + '\n':
        resp= 'ALIVE'
    return resp


def seqcheck(seq):
    check = 'ACGT'
    for i in seq:
        if i not in check:
            resp = 'ERROR'
        else:
            resp = 'OK'
    return resp

def operationcheck(data):
    check= ['complement', 'len', 'reverse', 'countA','countC','countG','countT', 'percA','percC','percG','percT',]
    resp=None
    try:
        operations=data[1:]
        for i in operations:
            if i not in check:
                resp='ERROR'
    except:
        resp='ERROR'
    return resp


def operations(seq, operation):
    i = Seq(seq)
    operations = {'len': i.len(),
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

    return operations[operation]


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

    msg=process_client(clientsocket)
    response= []

    # checking if the user is just checking if the server is alive
    if ping(msg)=='ALIVE':
        clientsocket.send(str.encode(ping(msg)))

    # process the message of the client
    else:
        msg=msg.rstrip(' \n')
        data= msg.split('\n')
        seq=data[0]
        seq=seq.upper()

        # Checking if the request is alright

        if seqcheck(seq)== 'ERROR':
            print('errooooooooooooooor')
            clientsocket.send(str.encode('ERROR'))
        elif operationcheck(data)=='ERROR':
            print('errprrapesrjp 2222222')
            clientsocket.send(str.encode('ERROR'))
        else:
            response.append('OK')
            operations=data[1:]
            print(operations[0])
            print(seq)
            i=(operations(seq, operations[0]))


            for i, elem in enumerate(response):
                response[i]=str(elem)

            response='\n'.join(response)
            response=str(response)
            clientsocket.send(str.encode(response))


    # close the socket
    clientsocket.close()
