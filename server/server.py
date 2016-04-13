#TCP server

from socket import *
from time import ctime

host = ''
port=21567
bufsize=1024
addr=(host,port)

tcpsersock = socket(AF_INET,SOCK_STREAM)
tcpsersock.bind(addr)
tcpsersock.listen(5)

#while True:
  
while True:
    print 'waiting from connection...'
    while True:
        tcpclisock, addr =tcpsersock.accept()
        print '...conneted from:',addr
        while True:
            data = tcpclisock.recv(bufsize)
            if not data:
                break
            print 'rec:',data
            data1=raw_input('me:')
            if not data1:
               break
            tcpclisock.send('[%s]%s%s'%(ctime(),'I have rec:',data1))
            if '886' in data:
                break
        if  '886' in data:
            break
tcpsersock.close()
