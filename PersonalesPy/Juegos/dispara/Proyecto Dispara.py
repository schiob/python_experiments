
# -*- coding: utf-8 -*-

# Modulos 
import pygame
from pygame.locals import *
import sys
import random 
 
# Constantes

screen_widht = 600
screen_height = 500
velocidad = 10

#----------------------------


# Clases

class Player(pygame.sprite.Sprite):
	def __init__(self, imagen):
		self.imagen = imagen
		self.rec = self.imagen.get_rect()
		self.rec.top = 400
		self.rec.left = 300

	def mover(self, vx, vy):
		self.rec.move_ip(vx, vy)
		if self.rec.top < 0 or self.rec.bottom > screen_height:
			vy = -vy
		if self.rec.left < 0 or self.rec.right > screen_widht:
			vx = -vx
		self.rec.move_ip(vx, vy)


	def update(self, superficie):
		superficie.blit(self.imagen, self.rec)

class Bala(pygame.sprite.Sprite):
	def __init__(self, imagen, topp, midleft):
		self.imagen = imagen
		self.rect = self.imagen.get_rect()
		self.rect.top = topp
		self.rect.left = midleft + 9
		
	def mover(self):
		self.rect.move_ip(0, -15)

	def poner(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def regresar(self):
		self.rect.top = -5

class Malo(pygame.sprite.Sprite):
	def __init__(self, imagen):
		self.imagen = imagen
		self.rect = self.imagen.get_rect()
		self.rect.top = random.randint(-500, -10) 
		self.rect.left = random.randint(0, 590)

	def mover(self):
		self.rect.move_ip(0, 5)

	def update(self, superficie):
		superficie.blit(self.imagen, self.rect)

	def regresar(self):
		self.rect.top = random.randint(-500, -10) 
		self.rect.left = random.randint(0, 590)

#----------------------------

# Funciones
def load_image(nombre, alpha = False):
	imagen = pygame.image.load(nombre)
	if alpha == True:
		imagen = imagen.convert_alpha()
	else:
		imagen = imagen.convert()
	return imagen

def colision(balas, malo):
	for bala in balas:
		if malo.rect.colliderect(bala):
			bala.regresar()
			return True
	return False

def colision2(player, malos):
	for malo in malos:
		if malo.rect.colliderect(player.rec): #AQUI ESTA LA FALLA
			return True
	return False

#----------------------------

def main():
	pygame.init()
	screen = pygame.display.set_mode([screen_widht, screen_height])
	pygame.display.set_caption('Disparar')
	reloj = pygame.time.Clock()
	imagen_nave = load_image('nave.png', alpha = True)
	imagen_fondo = load_image('space.jpg', alpha = False)
	imagen_disparo = load_image('bala.png', alpha = True)
	imagen_malo = load_image('malo.png', alpha = True)
	imagen_explo = load_image('explocion.png', alpha = True)
	player1 = Player(imagen_nave)
	balas = []
	num_malos = 10
	fuente1 = pygame.font.SysFont('Arial', 30, True, False)
	malos = []
	marcador = 0
	sigue = True
	for x in range(num_malos):
		malos.append(Malo(imagen_malo))

	# Variables
	vx = 0
	vy = 0
	leftsigue, rightsigue, upsigue, downsigue = False, False, False, False

#----------------------------	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if sigue:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						balas.append(Bala(imagen_disparo, player1.rec.top, player1.rec.left))


					if event.key == pygame.K_LEFT:
						leftsigue = True
						vx = -velocidad
						
					if event.key == pygame.K_RIGHT:
						rightsigue = True
						vx = velocidad
					
					if event.key == pygame.K_UP:
						upsigue = True
						vy = -velocidad
					
					if event.key == pygame.K_DOWN:
						downsigue = True
						vy = velocidad

				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT:
						leftsigue = False
						if rightsigue == True:
							vx = velocidad
						else:
							vx = 0
					if event.key == pygame.K_RIGHT:
						rightsigue = False
						if leftsigue == True:
							vx = -velocidad
						else:
							vx = 0
					if event.key == pygame.K_UP:
						upsigue = False
						if downsigue == True:
							vy = velocidad
						else:
							vy = 0
					if event.key == pygame.K_DOWN:
						downsigue = False
						if upsigue == True:
							vy = -velocidad
						else:
							vy = 0


		reloj.tick(15)
		screen.blit(imagen_fondo, [0,0])
		player1.update(screen)
		player1.mover(vx, vy)
		if sigue == True:
			for malo in malos:
				malo.mover()
		for malo in malos:
			malo.update(screen)
		if sigue == True:
			for disparo in balas:
				disparo.poner(screen)
		for disparo in balas:
			disparo.mover()
		
		for malo in malos:
			if colision(balas, malo):
				malo.regresar()
				marcador += 1

		for malo in malos:
			if malo.rect.bottom > 500:
				malo.regresar()
				marcador -= 1

		for bala in balas:
			if bala.rect.top <= 0:
				balas.remove(bala)

		if colision2(player1, malos):
			sigue = False
			vx, vy = 0, 0
			screen.blit(imagen_explo, (player1.rec.left, player1.rec.top))


		marc = str(marcador)
		mostrar = fuente1.render(marc, 0, (200, 0, 0))
		screen.blit(mostrar, (5, 5))

		pygame.display.update()

	pygame.quit()


if __name__ == "__main__":
    main()
