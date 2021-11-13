# Début de client

import socket
import select

Clientsock = None


def debut():
    global Clientsock
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

def envoi2(data):
    Clientsock.send(data.encode())

def choixperso():
    p = input("Quel personnage : Woman , Man , Snake ?")
    for i in persos:
        if p == persos[i]:
            persos.remove(p)
    return (p , persos)
