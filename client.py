#!/usr/bin/env python
import select
import socket

HOST = '127.0.0.1'
PORT = 9999

def main():
    s = socket.socket()
    s.connect((HOST, PORT))
    epoll = select.epoll()
    epoll.register(s, select.POLLIN)
    while True:
        epoll.poll()
        data = s.recv(256)

if __name__ == '__main__':
    exit(main())
