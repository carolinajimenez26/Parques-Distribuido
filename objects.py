import pygame

class Cuadro(pygame.sprite.Sprite):

    def __init__(self, pantalla, ancho, alto, color):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.pantalla = pantalla

    def draw(self, fondo, posx, posy):

        self.pantalla.blit(fondo, (posx,posy))


class Jugador(pygame.sprite.Sprite):

    pass

class Ficha(pygame.sprite.Sprite):

    pass
