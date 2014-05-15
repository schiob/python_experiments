# -*- coding: utf-8 -*-

#importamos modulos
import pygame
import random

class Player(pygame.sprite.Sprite):
	def __init__(self,imagen):
		self.imagen = imagen
		self.rect = self.imagen.get_rect()
		self.rect.top, self.rect.left = 280, 400
	def mover(self, vx, vy):
		self.rect.move_ip(vx, vy)
		if self.rect.left < 0 or self.rect.right >= 600:
			vx = -vx
		if self.rect.top < 0 or self.rect.bottom >= 500:
			vy = -vy
		self.rect.move_ip(vx, vy)

	def update(self, superficie):
		superficie.blit(self.imagen,self.rect)

	def inicial(self):
		self.rect.top, self.rect.left = 280, 400

class Recs(object):
	def __init__(self, numeroinicial): 
		self.lista = []
		for x in range(numeroinicial):
			left = random.randint(1, 580)
			top = random.randint(-500, -10)
			wigth = random.randint(10, 30)
			hight = random.randint(10, 30)
			self.lista.append(pygame.Rect(left, top, wigth, hight))

	def mover(self):
		for rectangulo in self.lista:
			rectangulo.move_ip(0, 5)

	def poner(self, superficie):
		for rectangulo in self.lista:
			pygame.draw.rect(superficie, [200, 0, 100], rectangulo)

	def regresar(self):
		for x in range(len(self.lista)):
			if self.lista[x].top > 520:
				left = random.randint(1, 580)
				top = random.randint(-500, -10)
				wigth = random.randint(10, 30)
				hight = random.randint(10, 30)
				self.lista[x] = pygame.Rect(left, top, wigth, hight)

	def regresar_todos(self):
		for x in range(len(self.lista)):
			self.lista[x].top = random.randint(-500, -10)
			self.lista[x].left = random.randint(1, 500)

def colision(player, recs):
	for rec in recs.lista:
		if player.rect.colliderect(rec):
			return True
	return False


#funcion principal
def main():
	pygame.init()
	pantalla = pygame.display.set_mode([600, 500])
	pygame.display.set_caption('Proyecto esquiva')
	reloj1 = pygame.time.Clock()
	imagen1 = pygame.image.load('nave.jpg')
	imagenexp = pygame.image.load('explocion.png').convert_alpha()
	player = Player(imagen1)
	recs = Recs(30)
	r2 = pygame.Rect(random.randint(0, 550), random.randint(0, 450), 20, 20)
	fuente1 = pygame.font.SysFont('Arial', 30, True, False)
	fuente2 = pygame.font.SysFont('Arial', 40, True, False)
	
	#variables auxiliares
	velocidad = 10
	vx, vy = 0, 0
	leftsigue, rightsigue, upsigue, downsigue = False, False, False, False
	salir = False
	pega = False
	marcador = 0
	mas_alto = False
	
	while salir != True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				salir = True

			if event.type == pygame.KEYDOWN:
				if pega == True:
					if event.key == pygame.K_RETURN:
						marcador = 0
						recs.regresar_todos()
						player.inicial()
						recs.poner(pantalla)
						player.update(pantalla)
						r2 = pygame.Rect(random.randint(0, 550), random.randint(0, 450), 20, 20)
						pega = False
						mas_alto = False

				if pega == False:
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
		reloj1.tick(15)

		marc = str(marcador)
		mostrar = fuente1.render(marc, 0, (0, 200, 0))
		alfinal = fuente2.render('Jugar de nuevo: enter', 0, [255,255,255])
		nueva_marca = fuente2.render('!Nueva high score! ' + marc , 0, [255,255,255])

		pantalla.fill([0, 0, 0])

		if pega == False:
			recs.mover()
			player.mover(vx, vy)
			player.update(pantalla)
		

		if player.rect.colliderect(r2):
			r2.height = 0
			r2.width = 0
			marcador += 1

		if r2.width == 0:
			r2 = pygame.Rect(random.randint(0, 550), random.randint(0, 450), 20, 20)
		
		
		if colision(player, recs):
			pega = True
			pantalla.blit(imagenexp, (player.rect.left, player.rect.top))
		recs.poner(pantalla)
		pygame.draw.rect(pantalla, (0, 0, 250), r2)
		if pega == True:
			pantalla.blit(alfinal, (100, 450))
			high_score_doc = open('high_score.txt', 'r+')
			high_score_str = high_score_doc.read()
			high_score = int(high_score_str)
			high_score_mostrar = fuente2.render('High Score: ' + high_score_str, 0, [155,155,155])
			if marcador > high_score:
				high_score_doc.seek(0)
				high_score_doc.write(marc)
				mas_alto = True
			if not mas_alto:
				pantalla.blit(high_score_mostrar, [100, 350])
			high_score_doc.close()
			if mas_alto:
				pantalla.blit(nueva_marca, [100, 350])

		recs.regresar()
		pantalla.blit(mostrar, (5, 5))
		pygame.display.update()

	pygame.quit()

main()
