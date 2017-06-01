import pygame
import sys
from pygame.locals import *

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1, imagen2,x,y):
        self.imagen_normal = imagen1
        self.imagen_seleccion = imagen2
        self.imagen_actual = self.imagen_normal
        self.rect = self.imagen_actual.get_rect()
        self.rect.left,self.rect.top = x,y

    def accion(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual = self.imagen_seleccion
        else:
            self.imagen_actual = self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)

def menu(cursor):
    ALTO = 600
    ANCHO = 600

    pygame.init()

    PANTALLA = pygame.display.set_mode([ANCHO,ALTO])
    pygame.key.set_repeat(100,10)

    fondo = pygame.image.load("game.png")
    jugar1 = pygame.image.load("botones/1.png")
    jugar2 = pygame.image.load("botones/1.1.png")
    salir1 = pygame.image.load("botones/2.png")
    salir2 = pygame.image.load("botones/2.2.png")
    boton1 = Boton(jugar1,jugar2,100,100)
    boton2 = Boton(salir1,salir2,100,200)
    pygame.mixer.music.load("musica/1.mp3")
    pygame.mixer.music.play(3)

    cerrar= False

    while not cerrar:
        tecla = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                cerrar = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(boton1.rect):
                    val = False
                    cerrar = True
                if cursor.colliderect(boton2.rect):
                    cerrar = True
                    val = True
                
        cursor.posicion()
        PANTALLA.blit(fondo,(0,0))
        boton1.accion(PANTALLA,cursor)
        boton2.accion(PANTALLA,cursor)
        pygame.display.flip()
    pygame.mixer.music.stop()
    #pygame.quit()
    return val
