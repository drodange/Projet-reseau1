#!/usr/bin/python3

import socket
import select
import sys
import time

socket_host = socket.socket(socket.AF_INET , socket.SOCK_STREAM , 0)

list_players_read = [] # liste des sockets joueurs connectés en lecture uniquement
list_players_write = [] # liste des sockets joueurs connectés en écriture uniquement
list_select = [] # la list_players ne doit contenir que les autres joueurs d'où une list_select
list_addr = [] # liste des paires (ip, port)
list_none2 = []

list_host = sys.argv[3:] # début list_host vide si 1er lancement
print(list_host)

def eden_host(): # fonction lancement socket
    """
    socket_host.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1) # éviter un problème de socket
    socket_host.bind((sys.argv[1], int(sys.argv[2]))) # sys.argv rustine pour test en ip local
    socket_host.bind(('',7777))
    socket_host.listen(5)"""

    if len(list_host) == 0: # SERVEUR : connexion après un connect() du client
        
        socket_host.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1) # éviter un problème de socket
        socket_host.bind((sys.argv[1], int(sys.argv[2])))
        socket_host.listen(5)
        eden_serv()
        #time.sleep(2)
        #eden_connect_serv()

    else: # CLIENT : connexion avec ip/port

        eden_connect_argv()
        #data = input()
        #eden_send(data=data)
        #eden_recv()
        #eden_serv()


def eden_serv(): # création serveur + écoute de connexion

    while len(list_players_read) < 1: # en attente de la connexion d'un ou plus de joueurs (pour l'instant 1 joueur à modifier par la suite)

        list_socket_read, list_socket_write, useless2 = select.select(list_players_read + [socket_host], list_players_write, list_none2)

        for sock_read in list_socket_read:
            
            if sock_read == socket_host:
                socket_client, addr = sock_read.accept()
                list_players_read.append(socket_client)
                #print(list_players_read)
                list_addr.append(addr)
                print("Connexion joueur ", addr)
                #return list_players, list_addr 
                
def eden_connect_argv(): # fonction de connexion du CLIENT

    socket_host.connect((list_host[0], int(list_host[1])))

def eden_connect_serv(): # test de connexion inter-serveur

    for ipport in list_addr:

        socket_host.connect(ipport)

def eden_send_recv(data): # gestion de l'envoi de données

    if data != "":

        if len(list_host) == 0: # le serveur envoi

            list_socket_read, list_socket_write, useless2 = select.select(list_players_read, list_players_write + [list_players_read[0]], list_none2)

            for sock_write in list_socket_write:

                data = str(data)
                data = data.encode("utf-8")
                sock_write.sendall(data)

        else: # le client envoi

            data = str(data)
            data = data.encode("utf-8")
            socket_host.sendall(data)

    else:

        if len(list_host) == 0: # le SERVEUR reçoit

            list_socket_read, list_socket_write, useless2 = select.select(list_players_read + [socket_host], list_players_write, list_none2)

            for sock_read in list_socket_read:

                data = sock_read.recv(4096)
                data = data.decode("utf-8")
                if data != "":
                    #print(data)
                    return data # ne fonctionne pas avec plus de 2 joueurs

        else: # le CIENT reçoit

            data = socket_host.recv(4096)
            data = data.decode("utf-8")
            if data != "":
                #print(data)
                return data
           
    
    
#class eden:

