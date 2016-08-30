# coding=utf-8

from socket import *
import sys


HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
CODEC = 'utf-8'

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input(u'>>')
    # data = raw_input(u'>>')。decode(sys.stdin.encoding)
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()


