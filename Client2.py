# Début de client

import socket
import select




def debut():
    Clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    actions = 1
    socketlist = []
    Clientsock.connect(("127.0.0.1" , 7777))

def suite():
    while actions:
        a2,b2,c2 = select.select(socketlist+[Clientsock],[],[])
        for i in a2:
            sc , ip = Clientsock.accept()
            if actions == False:
                break
            elif i == Clientsock:
                socketlist.append(sc)
            else:
                msgclient = sc.recv(1024)
                if msgclient == '':
                    socketlist.remove(sc)
                    sc.close()

