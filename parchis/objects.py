import pygame
import random

class Jugador(pygame.sprite.Sprite):

    pass

class Ficha(pygame.sprite.Sprite):

    pass

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    
    def posicion(self):
        self.left,self.top = pygame.mouse.get_pos()


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

class Dado(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.img1 = pygame.image.load("objetos/dados/1.JPG")
        self.img1 = pygame.transform.scale(self.img1, (50, 50))
        self.img2 = pygame.image.load("objetos/dados/2.JPG")
        self.img2 = pygame.transform.scale(self.img2, (50, 50))
        self.img3 = pygame.image.load("objetos/dados/3.JPG")
        self.img3 = pygame.transform.scale(self.img3, (50, 50))
        self.img4 = pygame.image.load("objetos/dados/4.JPG")
        self.img4 = pygame.transform.scale(self.img4, (50, 50))
        self.img5 = pygame.image.load("objetos/dados/5.JPG")
        self.img5 = pygame.transform.scale(self.img5, (50, 50))
        self.img6 = pygame.image.load("objetos/dados/6.JPG")
        self.img6 = pygame.transform.scale(self.img6, (50, 50))
        self.imagen_actual = self.img1
        self.rect = self.imagen_actual.get_rect()
        self.rect.left = x
        self.rect.top = y

    def generate(self, pantalla): # genera numero aleatorio para el dado

        val = random.randint(1,6)
        self.accion(val, pantalla)

    def accion(self,val,pantalla):

        if (val == 1):
            self.imagen_actual = self.img1
        if (val == 2):
            self.imagen_actual = self.img2
        if (val == 3):
            self.imagen_actual = self.img3
        if (val == 4):
            self.imagen_actual = self.img4
        if (val == 5):
            self.imagen_actual = self.img5
        if (val == 6):
            self.imagen_actual = self.img6

        pantalla.blit(self.imagen_actual,self.rect)

    def draw(self, pantalla):
        
        pantalla.blit(self.imagen_actual,self.rect)

