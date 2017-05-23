import pygame
import sys
from pygame.locals import *
#from juego import *

ALTO= 600
ANCHO= 700

pygame.init()

PANTALLA= pygame.display.set_mode([ANCHO,ALTO])
pygame.key.set_repeat(100,10)

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def posicion(self):
        self.left,self.top=pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1, imagen2,x,y):
        self.imagen_normal= imagen1
        self.imagen_seleccion= imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=x,y

    def accion(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual= self.imagen_seleccion
        else:
            self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)


pygame.mixer.music.load("musica/1.mp3")
pygame.mixer.music.play(3)

def inicio():
    fondo=pygame.image.load("objetos/game.png")
    jugar1= pygame.image.load("objetos/botones/1.png")
    jugar2= pygame.image.load("objetos/botones/1.1.png")
    salir1= pygame.image.load("objetos/botones/2.png")
    salir2= pygame.image.load("objetos/botones/2.2.png")
    cursor= Cursor()
    boton1= Boton(jugar1,jugar2,100,100)
    boton2= Boton(salir1,salir2,100,200)

    cerrar= False

    while not cerrar:
        tecla= pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==QUIT:
                cerrar=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):
                    pass
                if cursor.colliderect(boton2.rect):
                    cerrar=True
                
        cursor.posicion()
        PANTALLA.blit(fondo,(0,0))
        boton1.accion(PANTALLA,cursor)
        boton2.accion(PANTALLA,cursor)
        pygame.display.flip()
    pygame.quit()
    

inicio()
