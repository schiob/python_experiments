import pygame
import sys
import math
from pygame.locals import *

windowSize = (1000, 1000)
NO_INTER = 250

pygame.init()
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode(windowSize)
pygame.display.set_caption('Mandelbrot')

backColor = pygame.Color(0, 0, 0)
blueColor = pygame.Color(0, 0, 255)


def evaluar(z):
    return math.sqrt((z[0]**2) + (z[1]**2))


def calcVal(coord, inter):
	z = [0, 0]
	cont = 0
	for x in xrange(1,inter):
		z = [(z[0]**2)-(z[1]**2), (z[0]*z[1])+(z[1]*z[0])]
		z = [(z[0] + coord[0]), (z[1] + coord[1])]
		cont+=1
		if(evaluar(z) >= 2):
			return cont
			#return False
	return cont
	#return True

#while True:
window.fill(backColor)

for x in range(0, windowSize[0]):
	for y in range(0, windowSize[1]):
		#solo dibujar el conjunto
		"""
		if(calcVal( ( (-2 + x*(4.0/ windowSize[0])) , (2 - y*(4.0/ windowSize[1]))), NO_INTER)):
			window.set_at((x, y), blueColor)
			#EFECTO COOL pero lento
			#pygame.display.update()
		"""
		#"""
		col = calcVal( ( (-2 + x*(4.0/ windowSize[0])) , (2 - y*(4.0/ windowSize[1]))), NO_INTER)
		if(col < 2):
			window.set_at((x, y), (0, 0, 0))
		
		elif(col > 1 and col < 11):
			window.set_at((x, y), (50, 0, 0))
		
		elif(col > 10 and col < 12):
			window.set_at((x, y), (100, 0, 0))
		
		elif(col > 11 and col < 15):
			window.set_at((x, y), (200, 10, 10))
		
		elif(col > 14 and col < 21):
			window.set_at((x, y), (220, 200, 200))
		
		elif(col > 20 and col < 50):
			window.set_at((x, y), (0, 255, 255))

		else:
			window.set_at((x, y), (0, 0, 0))
		#"""
		print(((x + y*windowSize[1])%windowSize[1])/10) #contador

while(True):
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(30)
