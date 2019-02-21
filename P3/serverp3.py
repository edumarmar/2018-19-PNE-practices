import socket
from Seqp3 import Seq


PORT = 9001
IP = '212.128.253.108'
MAX_OPEN_REQUEST = 5


def process_client(cs):
    # Reading the message from the client
    msg = cs.recv(2048).decode('utf-8')
    resp=msg
    print('Message from the client: {}'.format(msg))


    if msg == '' + '\n':
        resp= 'ALIVE'

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
                  'percG': i.perc('g'),}

    return operations[operation]

def seq_check(seq):
    for i in seq:
        if i not in check:
            return 'ERROR'




print('Socket ready: {}'.format(serversocket))

while True:
    print('Waiting for connections at: {}, {}'.format(IP, PORT))

    # process the client request
    (clientsocket, addres) = serversocket.accept()
    print('Atetending client: {}'.format(addres))

    resp=process_client(clientsocket)
    print(resp)
    if resp!= 'ALIVE':
        data= resp.split('\n')
        print(data)
        seq=data[0]
        resp= seq_check(seq)
        print(resp)
        operation= data[1]
        try:
            resp=operations(seq, operation)
            resp=str(resp)
        except:
            pass

    clientsocket.send(str.encode(resp))
    # close the socket
    clientsocket.close()
