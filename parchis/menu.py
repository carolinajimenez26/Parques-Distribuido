import pygame
import sys
from pygame.locals import *
from objects import *


ALTO= 600
ANCHO= 700

pygame.init()

PANTALLA= pygame.display.set_mode([ANCHO,ALTO])
pygame.key.set_repeat(100,10)

def menu(cursor):
    fondo=pygame.image.load("objetos/game.png")
    jugar1= pygame.image.load("objetos/botones/1.png")
    jugar2= pygame.image.load("objetos/botones/1.1.png")
    salir1= pygame.image.load("objetos/botones/2.png")
    salir2= pygame.image.load("objetos/botones/2.2.png")
    boton1= Boton(jugar1,jugar2,100,100)
    boton2= Boton(salir1,salir2,100,200)
    pygame.mixer.music.load("musica/1.mp3")
    pygame.mixer.music.play(3)

    cerrar= False

    while not cerrar:
        tecla= pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==QUIT:
                cerrar=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):
                    val = True
                    cerrar = True
                if cursor.colliderect(boton2.rect):
                    cerrar=True
                    val = False
                
        cursor.posicion()
        PANTALLA.blit(fondo,(0,0))
        boton1.accion(PANTALLA,cursor)
        boton2.accion(PANTALLA,cursor)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.quit()
    return val
