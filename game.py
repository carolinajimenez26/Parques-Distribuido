import pygame
import random

WIDTH = 1024
HIGH = 700

if __name__ == '__main__':
	pygame.init()
	SCREEN = pygame.display.set_mode([WIDTH,HIGH])
	picture = pygame.image.load('Background.png')
	picture = pygame.transform.scale(picture, (WIDTH, HIGH))
	rect = picture.get_rect()
	SCREEN.blit(pygame.transform.scale(picture, (WIDTH, HIGH)), (0, 0))
	pygame.display.flip()

	reloj = pygame.time.Clock()
	pygame.display.set_caption("Parques Distribuido")
	background = pygame.image.load('Background.png').convert()

	pos = pygame.mouse.get_pos()#recibe donde esta ubicado el mouse
	ls_all = pygame.sprite.Group()
	ls_impactos = pygame.sprite.Group()
	#----------------JUGADOR-------------------------


    #------------------------------------------------
	pygame.display.flip()
	end = False

	while not end:

		pos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True



        #------------IMPRIME EN PANTALLA--------------
		#ls_all.update()
		#ls_all.draw(SCREEN)
		SCREEN.blit(pygame.transform.scale(picture, (WIDTH, HIGH)), (0, 0))
		pygame.display.flip()
		reloj.tick(60)
