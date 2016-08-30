# coding=utf-8

from socket import *
from time import ctime


HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
CODEC = 'utf-8'

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print u'wating for connected'
    (tcpCliSock, addr) = tcpSerSock.accept()
    print u'...connected from: ', tcpCliSock
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            tcpCliSock.close()
            break
        tcpCliSock.send('[%s] %s' % (ctime(),data))
tcpSerSock.close()
