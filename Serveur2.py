# Début de serveur

import socket
import select
import time

listeclient = []
Serveur = None
sc = None

def debut():
    global Serveur
    Serveur = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    Serveur.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    Serveur.bind (("127.0.0.1" , 7777 )) 
    Serveur.listen(5)
    print("En attente de client")
    global listeclient
    global sc

    while len(listeclient) < 1:
        a, b, c = select.select (listeclient + [Serveur], [], [])
        for i in a:
            actions = False
            sc, addr = Serveur.accept()
            print("New Client", addr)
            if i == Serveur:
                listeclient.append(sc)
            elif actions == False:
                break
            else:
                msg = sc.recv (1024)
                    
                if msg == b'':
                    listeclient.remove (sc)
                    sc.close ()



def choixmap():
    m=input("Quel map : map1 , map2 , map3 ?")
    return m



