# by Timothy Downs, inputbox written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from objects import Boton


rojo1 = pygame.image.load("rojo.png")
rojo1= pygame.transform.scale(rojo1, (50,50))
rojo2 = pygame.image.load("ficha_roja_2.png")
rojo2= pygame.transform.scale(rojo2, (50,50))
verde1 = pygame.image.load("verde.png")
verde1= pygame.transform.scale(verde1, (50,50))
verde2 = pygame.image.load("ficha_verde_2.png")
verde2= pygame.transform.scale(verde2, (50,50))
azul1 = pygame.image.load("azul.png")
azul1= pygame.transform.scale(azul1, (50,50))
azul2 = pygame.image.load("ficha_azul_2.png")
azul2= pygame.transform.scale(azul2, (50,50))
amarillo1 = pygame.image.load("amarilla.png") 
amarillo1= pygame.transform.scale(amarillo1, (50,50))
amarillo2 = pygame.image.load("ficha_amarillo_2.png")
amarillo2= pygame.transform.scale(amarillo2, (50,50))

boton_rojo = Boton(rojo1,rojo2,100,100)
boton_verde = Boton(verde1,verde2,160,100)
boton_azul = Boton(azul1,azul2,220,100)
boton_amarillo = Boton(amarillo1,amarillo2,280,100)

color = "" 
current_color = None

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def posicion(self):
        self.left,self.top=pygame.mouse.get_pos()

cursor = Cursor()

def get_key(cursor, screen, current_color):
  color=current_color
  while 1:
    event = pygame.event.poll()
    if event.type == QUIT:
        break
    if event.type == pygame.MOUSEBUTTONDOWN:
      if cursor.colliderect(boton_rojo.rect):
        color = "rojo"
      if cursor.colliderect(boton_verde.rect):
        color = "verde"
      if cursor.colliderect(boton_azul.rect):
        color = "azul"
      if cursor.colliderect(boton_amarillo.rect):
        color = "amarillo"
    if event.type == KEYDOWN:
      return event.key, color

    cursor.posicion()
    boton_rojo.accion(screen,cursor)
    boton_verde.accion(screen,cursor)
    boton_azul.accion(screen,cursor)
    boton_amarillo.accion(screen,cursor)
    pygame.display.flip()

def display_box(screen, message, cursor):
  "Print a message in a box in the middle of the screen"
  x = 100 #(screen.get_width() / 2) - 102
  y = 20 #(screen.get_height() / 2) - 12
  fontobject = pygame.font.Font(None,25)
  pygame.draw.rect(screen, (0,0,0),(x,y,500,240), 0)
  #pygame.draw.rect(screen, (255,255,255),(x-5,y-5,204,24), 1)
  if len(message) != 0:
    screen.blit(fontobject.render(message, 1, (255,255,255)),
                (x, y))

  pygame.display.flip()


def ask(screen, question, cursor):
  "ask(screen, question) -> answer"
  current_color = None
  pygame.font.init()
  current_string = []
  display_box(screen, question + ": " + string.join(current_string,""), cursor)
  while 1:
    inkey, current_color = get_key(cursor, screen, current_color)
    if inkey == K_BACKSPACE:
      current_string = current_string[0:-1]
      #print ("curr : ", current_string)
    elif inkey == K_RETURN:
      break
    elif inkey == K_MINUS:
      current_string.append("-")
    elif inkey <= 127:
      if (len(current_string) <= 10):
        current_string.append(chr(inkey))
    print "Color seleccionado: %s" %current_color

    display_box(screen, question + ": " + string.join(current_string,""), cursor)
    
  return string.join(current_string,"")

def main():
  screen = pygame.display.set_mode((500,240))
  return ask(screen, "Nombre de usuario", cursor)

if __name__ == '__main__': main()
