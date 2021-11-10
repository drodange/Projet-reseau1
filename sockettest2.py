import Client
import Serveur


def sendDebut():
    maps = ['map1' , 'map2' , 'map3']
    roles = ['Adam' , 'Eve' , 'Serpent']
    if actions == Client1:
        choix = input("Quel role : Adam , Eve , Serpent ?")
        for i in len(roles):
            if choix == maps[i]:
                sock.send (roles[i])
    if actions == Serv1:
        choix = input("Quel map : map1 , map2 , map3 ?")
        for i in len(maps):
            if choix == maps[i]:
                sock.send (maps[i])

    
