import pygame
import random
from imports import *
from helpers import *
from objects import *

# Valores para la pantalla

WIDTH = 1024 + 300
HIGH = 700

if __name__ == '__main__':
	pygame.init()
	reloj = pygame.time.Clock()
	fuente = pygame.font.SysFont("comicsansms", 30)
	# pantalla_s=load_sound('background.ogg',curdir)
	pos = pygame.mouse.get_pos()#recibe donde esta ubicado el mouse

	#----------------SCREEN--------------------------

	SCREEN = pygame.display.set_mode([WIDTH,HIGH])
	bg = pygame.image.load('Background.png')
	bg = pygame.transform.scale(bg, (WIDTH-300, HIGH))
	rect = bg.get_rect()
	pygame.display.set_caption("Parques Distribuido")
	SCREEN.fill((0,0,0))

	#--------------BOTONES---------------------------

	txt_btn_iniciar = fuente.render("INICIAR JUEGO",1, BLANCO)
	txt_btn_salir = fuente.render("SALIR",1, BLANCO)
	txt_btn_tirar = fuente.render("TIRAR",1, BLANCO) # tirar dados
	btn_x = WIDTH
	btn_y = 130
	btn_deltax = -250
	btn_deltay = 100

	btn_iniciar = Cuadro(SCREEN,100,100,VERDE)

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
		btn_iniciar.draw(bg,WIDTH+100,HIGH+100)
		SCREEN.blit(txt_btn_iniciar,(btn_x + btn_deltax, btn_y))
		SCREEN.blit(txt_btn_salir,(btn_x + btn_deltax, btn_y + btn_deltay))
		SCREEN.blit(txt_btn_tirar,(btn_x + btn_deltax, btn_y + 2*btn_deltay))
		pygame.display.flip()
		reloj.tick(60)
