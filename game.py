# -*- coding: utf-8 -*-

import pygame

from plateau import jeu, pomme
from projet_class_serpent import Serpent
from time import sleep


pygame.init()

board = jeu()
ecran = pygame.display.set_mode((960,960))
red = (255,0,0)
grey = (215,215,215)
green = (30,150,60)

def mouv(board,set_tete):
    co_tete = Serpent.tete
    board[x][y] == co_tete #savoir ou est la tête de surpent sur le plateau

def game(board):
    ready  = False 
    while not ready: # tant que le jeu n'est pas prêt
        if board[5][5] == 2:
            board[5][5]
            board = pomme(board)
        else: 
            ready = True
    
    board[5][5] = Serpent()
    board[5][5].direction = "e"
    
    while ready:
        for event in pygame.event.get():
            for y in range(len(board)):
                co_y = 0
                for x in range(1, y+1):
                    co_x = 80*x
                    if board[y][x] == 3:
                        pygame.draw.rect(ecran, grey, pygame.Rect(co_y, co_y, co_x, co_x))
                    elif board[y][x] == 2:
                        pygame.draw.rect(ecran, red, pygame.Rect(co_y, co_y, co_x, co_x))
                    elif isinstance(board[y][x], Serpent):
                        pygame.draw.rect(ecran, green, pygame.Rect(co_y, co_y, co_x, co_x))
            
            pygame.display.update()
            if event.type == pygame.K_ESCAPE   :
                ready = False
    
    if event.type == pygame.KEYUP: # flèche du haut jouer
        #On récupere la potition de la tête
        board[y][x].direction = "up"
        
    if event.type == pygame.KEYLEFT: # flèche du gauche jouer
        #On récupere la potition de la tête
        board[y][x].direction = "left"
        
    if event.type == pygame.KEYRIGHT: # flèche du droit jouer
        #On récupere la potition de la tête
        board[y][x].direction = "right"
        
    if event.type == pygame.KEYDOWN: # flèche du bas jouer
        #On récupere la potition de la tête
        board[y][x].direction = "down"
        

        
        
    pygame.quit()
        