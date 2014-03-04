#!/usr/bin/env python
import SocketServer
import time

HOST = '127.0.0.1'
PORT = 9999

class ReusableTCPServer(SocketServer.TCPServer):
    allow_reuse_address = True

class ServeAndCloseHandler(SocketServer.BaseRequestHandler):
    """
    Sends some data and then closes, to test epoll behavior against.
    """

    def handle(self):
        for i in range(3):
            self.request.sendall('data %d\n' % i)
            time.sleep(.5)

if __name__ == '__main__':
    server = ReusableTCPServer((HOST, PORT), ServeAndCloseHandler)
    server.serve_forever()
