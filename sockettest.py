import Client
import Serveur

Serv1 = 0
Client1 = 1


class Edensocket:
    def __init__(self, actions, addr):

        self.actions = actions
        self.addr = addr

        if self.actions == Serv1:
            self.sock = Serveur.Serveursocket(self.addr)
        elif self.actions == Client1:
            self.sock = Client.Clientsocket(self.addr)

        self.sock.debut()
        self.sock.suite()

   # def send(self, socket, datas):
   #      if self.actions == Client1:
   #          self.sock.send (maps)
   #      else:
   #          self.sock.sendall(maps)
