# -*- coding: utf-8 -*-

# Modulos 
import pygame
from pygame.locals import *
import sys
 
# Constantes


#----------------------------


# Clases


#----------------------------

def main():
    pygame.init()

    while True:
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			sys.exit()
    			


if __name__ == "__main__":
    main()