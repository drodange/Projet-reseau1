#!/usr/bin/python3

# Copyright (c) 2017-2019 Samuel Thibault <samuel.thibault@ens-lyon.org>
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY Samuel Thibault ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.

import sys
import pygame
import time
import Client2
import Serveur2

map = None
t = None

map1 = [ [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', ' ', ' ', 'S', ' ', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'M' ],
        [ 'W', 'X', ' ', 'X', 'A', 'X', 'X', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ] ]

map2 = [ [ 'W', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', ' ', ' ', 'S', ' ', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', 'A', 'X', 'X', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', ' ', ' ', ' ', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'M' ] ]

map3 = [ [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ],
        [ ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', ' ', 'S', ' ', ' ', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', ' ', 'X', 'X', ' ', 'X', 'M' ],
        [ 'W', ' ', ' ', 'X', ' ', 'X', 'X', ' ', ' ', ' ' ],
        [ ' ', 'X', ' ', 'X', ' ', 'A', ' ', ' ', 'X', ' ' ],
        [ ' ', 'X', ' ', 'X', 'X', 'X', 'X', 'X', 'X', ' ' ],
        [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ] ]

def main():
    global map
    global t
    while True:
        #Choix du mode de jeu, le premier joueur doit forcément être serveur.
        mode = input ("Quel mode : Serveur, Client\n")
        #Si on choisit Serveur ou Client, le while se break et on passe à la suite.
        if mode == 'Serveur' or 'Client':
            break
        #Si on ne choisit ni Serveur ni Client , le jeu ne se lance pas et le programme s'arrête.
        else:
            print("Mode invalide")
            sys.exit()

    #Coté serveur
    if mode == 'Serveur':
        Serveur2.debut() #On lance la socket serveur avec le programme contenu dans Serveur2.
        y = str(Serveur2.choixmap()) #Le serveur choisit la map.
        if y == "map1" : 
            map = map1
        if y == "map2" :
            map = map2
        if y == "map3" :
            map = map3
        Serveur2.envoi(y) #Le serveur envoie la map au client.
        time.sleep(10) #Le serveur se met en "attente" de recevoir la liste des personnages restants.
        msg = Serveur2.sc.recv(1024)
        x = msg.decode()
        t = input("Quel personnage : %s" %x ) #On stocke le résultat de l'input dans une variable utilisée après.
    
    #Coté Client
    if mode == 'Client':
        Client2.debut() #On connecte une socket cliente au serveur précédemment 
        time.sleep(10) #On met le client en attente du choix de la map
        msg = Client2.Clientsock.recv(1024) #On reçoit la map sous forme encodée
        #Ici on analyse le message décodé et on le compare pour pouvoir affecter la bonne map.
        if msg.decode() == "map1" : 
            map = map1
        if msg.decode() == "map2" :
            map = map2
        if msg.decode() == "map3" :
            map = map3
        x = Client2.choixperso()  #On lance le choix du personnage en premier chez le client avec la fonction choixperso de Client2.
        t = x[0] # On récupère le personnage que le client à choisit ( la valeur de p dans le return )
        x2 = x[1] # On affecte à x2 la deuxième partie de x ( les personnages restants )
        Client2.envoi2(str(x2)) # On envoie la liste des personnages restants 
main()


width = len(map[0])
height = len(map)

# This is the sprites size
unit = 64
grass = (0x00, 0x90, 0x00)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode( (unit * width, unit * height) )

# Load resources
woman = pygame.image.load("image/woman.png")
woman_ghost = woman.copy()
woman_ghost.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
woman_coords = [ 0, 0 ]
man = pygame.image.load("image/man.png")
man_ghost = man.copy()
man_ghost.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
man_coords = [ 0, 0 ]

snake = pygame.image.load("image/snake.png")
snake_ghost = snake.copy()
snake_ghost.fill((255, 255, 255, 128), None, pygame.BLEND_RGBA_MULT)
snake_coords = [ 0, 0 ]

stone = pygame.image.load("image/stone.png")
stone_coords = [ 0, 0 ]

apple = pygame.image.load("image/apple.png")
apple_coords = [ 0, 0 ]

woman_move = [ 0, 0 ]
man_move = [ 0, 0 ]
snake_move = [ 0, 0 ]

# Initialize positions
def init():
    def find(coords, c):
        for y in range(len(map)):
            for x in range(len(map[y])):
                if map[y][x] == c:
                    coords[0] = x
                    coords[1] = y
                    return
        raise Exception('oops')

    find(woman_coords, 'W')
    find(man_coords, 'M')
    find(snake_coords, 'S')
    find(apple_coords, 'A')

init()

while True:
    e = pygame.event.wait()

    # Check for exit
    if e.type == pygame.QUIT:
        sys.exit()

    elif e.type == pygame.KEYDOWN:
    #Ici le t correspond au t défini dans la fonction main() , et on assigne chaque joueur à son personnage.
        if t == 'Woman': 
    # Check for wowoman movements
            if e.key == pygame.K_z:
                woman_move = [ 0, -1 ]
                pass
            elif e.key == pygame.K_s:
                woman_move = [ 0, 1 ]
                pass
            elif e.key == pygame.K_q:
                woman_move = [ -1, 0 ]
                pass
            elif e.key == pygame.K_d:
                woman_move = [ 1, 0 ]
                pass

        if t == 'Man':
            # Check for man movements    
            if e.key == pygame.K_UP:
                man_move = [ 0, -1 ]
                pass
            elif e.key == pygame.K_DOWN:
                man_move = [ 0, 1 ]
                pass
            elif e.key == pygame.K_LEFT:
                man_move = [ -1, 0 ]
                pass
            elif e.key == pygame.K_RIGHT:
                man_move = [ 1, 0 ]
                pass
        if t == 'Snake':
            #Snake move
            if e.key == pygame.K_o:
                snake_move = [ 0, -1 ]
                pass
            elif e.key == pygame.K_l:
                snake_move = [ 0, 1 ]
                pass
            elif e.key == pygame.K_k:
                snake_move = [ -1, 0 ]
                pass
            elif e.key == pygame.K_m:
                snake_move = [ 1, 0 ]
                pass

        #else:
        #    print(e)

    def move(coords, move):
        return [ coords[0] + move[0], coords[1] + move[1] ]

        # Compute moves
    woman_newcoords = move(woman_coords, woman_move)
    man_newcoords = move(man_coords, man_move)
    snake_newcoords = move(snake_coords, snake_move)

        # But bound to window
    def bound(newcoords, coords, move):
        if newcoords[0] < 0 or newcoords[0] >= width or newcoords[1] < 0 or newcoords[1] >= height:
            # out of bounds
            newcoords[0] = coords[0]
            newcoords[1] = coords[1]
            move[0] = 0
            move[1] = 0

    bound(woman_newcoords, woman_coords, woman_move)
    bound(man_newcoords, man_coords, man_move)
    bound(snake_newcoords, snake_coords, snake_move)

    def collide(newcoords, coords, move):
        if map[newcoords[1]][newcoords[0]] == 'X':
                # Stone
            newcoords[0] = coords[0]
            newcoords[1] = coords[1]
            move[0] = 0
            move[1] = 0

        # Prevent collisions with stones
    collide(woman_newcoords, woman_coords, woman_move)
    collide(man_newcoords, man_coords, man_move)
    collide(snake_newcoords, snake_coords, snake_move)

        # Prevent collisions between players
    if woman_newcoords == man_newcoords:
        woman_newcoords = woman_coords
        woman_move = [ 0, 0 ]
        man_newcoords = man_coords
        man_move = [ 0, 0 ]

        # Make everybody move when everybody chose her/his direction
    if woman_move != [ 0, 0 ] and man_move != [ 0, 0 ] and snake_move != [ 0, 0 ]:
        woman_coords = woman_newcoords
        man_coords = man_newcoords
        snake_coords = snake_newcoords
        woman_move = [ 0, 0 ]
        man_move = [ 0, 0 ]
        snake_move = [ 0, 0 ]

        #print("woman at %u,%u to %u,%u" % (woman_coords[0], woman_coords[1], woman_newcoords[0], woman_newcoords[1]))
        #print("man at %u,%u to %u,%u" % (man_coords[0], man_coords[1], man_newcoords[0], man_newcoords[1]))
        #print("snake at %u,%u to %u,%u" % (snake_coords[0], snake_coords[1], snake_newcoords[0], snake_newcoords[1]))

        # Display everything
    screen.fill(grass)

    def blit(item, coords):
        screen.blit(item, (unit * coords[0], unit * coords[1]))

    # Display stones
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'X':
                blit(stone, (x, y))

        # Display moving items
    blit(apple, apple_coords)

    blit(woman_ghost, woman_newcoords)
    blit(woman, woman_coords)
    blit(man_ghost, man_newcoords)
    blit(man, man_coords)

#    blit(snake_ghost, snake_newcoords)
#    blit(snake, snake_coords)

        # Show new state
    pygame.display.flip()

    if woman_coords == apple_coords:
        print("woman won!\n")
        sys.exit()
    
    elif man_coords == apple_coords:
        print("man won!\n")
        sys.exit()

    if woman_coords == snake_coords:
        print("woman lost!\n")
        print("snake won!\n")
        sys.exit()
    
    elif man_coords == snake_coords:
        print("man lost!\n")
        print("snake won! \n")
        sys.exit()


