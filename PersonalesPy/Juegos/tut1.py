# -*- coding: utf-8 -*-
import pygame

def main():
	pygame.init() # con esto se inicializan todas las funciones
	pantalla = pygame.display.set_mode([300,300]) # Hacer la pantalla, (tamaño)
	pygame.display.set_caption('tutorial numero 1') # Ponerle nombre en la barra de menu
	reloj1 = pygame.time.Clock() # hacer un reloj
	blanco = (255, 255, 255)
	azul = (20, 20, 255)
	rojo = (255, 20, 20)
	s1 = pygame.Surface([150, 150]) #creamos una superficie
	s1.fill(azul) #pintamos la superficie
	s2 = pygame.Surface([75, 75])
	s2.fill(rojo)


	salir = False	#todo este bucle es para que no se cierre
	while salir != True: #loop Principal
		for event in pygame.event.get():
			if event.type == pygame.QUIT: # si el evento es picarle a la tachita
				salir = True
		reloj1.tick(20)
		pantalla.fill(blanco)
		pantalla.blit(s1, [75, 75]) #ponemos la superficie sobre la pantalla, (superficie, coordenadas)
		s1.blit(s2, [37, 37])
		pygame.display.update()

	pygame.quit()

main()