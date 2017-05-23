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
	cursor = Cursor()

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

		
		margen_x_dados = WIDTH - 220
		margen_y_dados = 300
		margen_x_salir = WIDTH - 220
		margen_y_salir = HIGH - 100
		btn_dados1 = pygame.image.load("objetos/dados.png")
		btn_dados2 = pygame.image.load("objetos/dados2.png")
		btn_salir1= pygame.image.load("objetos/botones/2.png")
		btn_salir2= pygame.image.load("objetos/botones/2.2.png")
		btn_dados1 = pygame.transform.scale(btn_dados1, (100, 100))
		btn_dados2 = pygame.transform.scale(btn_dados2, (100, 100))
		boton_salir = Boton(btn_salir1,btn_salir2,margen_x_salir,margen_y_salir)
		boton_dados = Boton(btn_dados1, btn_dados2, margen_x_dados, margen_y_dados)

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
			cursor.posicion()
			SCREEN.fill((0,0,0))
			boton_salir.accion(SCREEN, cursor)
			boton_dados.accion(SCREEN, cursor)
			SCREEN.blit(pygame.transform.scale(bg, (WIDTH-300, HIGH)), (0, 0))
			pygame.display.flip()
			reloj.tick(60)
		else:
			pass
			#Pantalla fin
