# Début de client

import socket
import select
l = []

class Clientsocket:

    def __init__(self, addr):
        self.Clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.actions = 1
        self.addr = addr

    def debut(self):
        self.Clientsock.connect(self.addr)

    def suite(self):
        while self.actions:
            a2,b2,c2 = select.select(l+[self.Clientsock],[],[])
            for i in a2:
                sc , addr = self.Clientsock.accept()
                if self.actions == False:
                    break
                elif sc == self.Clientsock:
                    l.append(sc)
                else:
                    msg = sc.recv(1024)
                    if msg == '':
                        l.remove(sc)
                        sc.close()

