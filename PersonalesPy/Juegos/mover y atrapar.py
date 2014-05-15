# -*- coding: utf-8 -*-
import pygame
import random
def mine():
	pygame.init()
	pantalla = pygame.display.set_mode([500, 500])
	pygame.display.set_caption('Mover')
	reloj1 = pygame.time.Clock()
	#colores
	blanco = (250, 250, 250)
	azul = (0, 0, 200)
	rojo = (200, 0, 0)
	verde = (0, 250, 50)
	#rectangulos
	r1 = pygame.Rect(100, 100, 20, 20)
	r2 = pygame.Rect(random.randint(0, 450), random.randint(0, 450), 20, 20)
	rect_list = []
	for rect in range(20):
		w = random.randint(10, 30)
		h = random.randint(10, 30)
		x = random.randint(1, 30)
		y = random.randint(1, 450)
		rect_list.append(pygame.Rect(x, y, w, h))

	salir = False
	while salir != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir = True

			
		if r2.height == 0:
			r2 = pygame.Rect(random.randint(0, 450), random.randint(0, 450), 20, 20)
		(r1.left, r1.top) = pygame.mouse.get_pos()
		r1.left -= r1.width/2
		r1.top -= r1.height/2
		for rec in rect_list:
			pygame.draw.rect(pantalla, verde, rec)
		rec.move_ip(10, 0)
		reloj1.tick(60)
		pantalla.fill(blanco)
		if r1.colliderect(r2):
			r2.height = 0
			r2.width = 0
		pygame.draw.rect(pantalla, azul, r1)
		pygame.draw.rect(pantalla, rojo, r2)
		pygame.display.update()

	pygame.quit()

mine()