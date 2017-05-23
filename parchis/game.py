import pygame
import random
from imports import *
from helpers import *
from objects import *
from menu import *

# Valores para la pantalla

WIDTH = 1024 + 300
HIGH = 700


if __name__ == '__main__':
	pygame.init()
	reloj = pygame.time.Clock()
	fuente = pygame.font.SysFont("comicsansms", 30)
	# pantalla_s=load_sound('background.ogg',curdir)
	pos = pygame.mouse.get_pos()#recibe donde esta ubicado el mouse
	cursor= Cursor()

	##############################################
	# muestra el menu
	jugar = menu(cursor)
	##############################################
	if jugar:
	#----------------SCREEN--------------------------

		SCREEN = pygame.display.set_mode([WIDTH,HIGH])
		bg = pygame.image.load('objetos/Background.png')
		bg = pygame.transform.scale(bg, (WIDTH-300, HIGH))
		rect = bg.get_rect()
		pygame.display.set_caption("Parques Distribuido")
		SCREEN.fill((0,0,0))

		#--------------BOTONES---------------------------

		
		btn_x = WIDTH
		btn_y = 130
		btn_deltax = -250
		btn_deltay = 100

		#---------------Sprites--------------------------

		ls_all = pygame.sprite.Group()
		ls_impactos = pygame.sprite.Group()

		#----------------JUGADOR-------------------------


	    #------------------------------------------------

		end = False

		while not end:

			pos = pygame.mouse.get_pos()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					end = True



	        #------------IMPRIME EN PANTALLA--------------
			#ls_all.update()
			#ls_all.draw(SCREEN)
			SCREEN.blit(pygame.transform.scale(bg, (WIDTH-300, HIGH)), (0, 0))

			pygame.display.flip()
			reloj.tick(60)
		else:
			pass
			#Pantalla fin
