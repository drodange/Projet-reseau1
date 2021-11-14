# Début de client

import socket
import select

Clientsock = None

persos = ['Woman','Man','Snake']

def debut():
    global Clientsock
    Clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    actions = 1
    socketlist = []
    Clientsock.connect(("127.0.0.1" , 7777))
    
#Envoi de données simple pour le client.
def envoi2(data):
    Clientsock.send(data.encode())

#Fonction pour le choix des personnages.
def choixperso():
    p = input("Quel personnage : Woman , Man , Snake ?\n")
    for i in persos:
        if p == i:
            persos.remove(p) #On enlève le personnage choisi par le client.
    return (p , persos) #On retourne le personnage choisi par le client et la liste des personnages restants.
