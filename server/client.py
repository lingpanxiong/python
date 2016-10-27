# tcp client
from socket import *

host = 'localhost'
port = 21567
bufsiz = 1024
addr = (host,port)

#tcpclisock = socket(AF_INET,SOCK_STREAM)
#tcpclisock.connect(addr)

while True:
    while True:
        tcpclisock = socket(AF_INET,SOCK_STREAM)
        tcpclisock.connect(addr)
        data = raw_input('me: ')
        if not data:
            break
        tcpclisock.send(data)
        data = tcpclisock.recv(bufsiz)
        if '886' in data:
            break	
        print data
    break

tcpclisock.close()
