# Début de serveur

import socket
import select

l = []


class Serveursocket:

    def __init__(self, addr):
        self.Serveur = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.socket = []
        self.addr = addr
        self.actions = 1

    def debut(self):
        self.Serveur.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.Serveur.bind (self.addr) # Pourquoi pas un tuple ?
        self.Serveur.listen (20)
        self.socket.append (self.Serveur)

    def suite(self):
        while self.actions:
            a, b, c = select.select (l + [self.Serveur], [], [])
            for i in a:
                sc, addr = self.Serveur.accept ()
                if self.actions == False:
                    break
                elif sc == self.Serveur:
                    l.append (sc)
                    break
                else:
                    msg = sc.recv (1024)
                    if msg == '':
                        l.remove (sc)
                        sc.close ()
                    break