import pygame, sys,time,copy,random
import numpy as np


pygame.init()
tiempo=time.time()
size=[960,600]
screen= pygame.display.set_mode(size)
clock=pygame.time.Clock()
#colores 

NEGRO=[0,0,0]
BLANCO=[250,250,250]
#casillas
nx=96
ny=60
ancho_casillas=size[0]//nx
alto_casillas=size[1]//ny
juego=np.zeros((ny,nx),dtype=int)
#juego=[]
#constructor de casillas
#for i in range(ny):
#	o=[]
#	for k in range(nx):
#		o.append(0)
#	juego.append(o)

evolucion=False
while True:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT :
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			xp=int(pos[0])//ancho_casillas
			yp=int(pos[1])//alto_casillas
			if juego[yp][xp]==1:
				juego[yp][xp]=0
			else:
				juego[yp][xp]=1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_SPACE:
				evolucion=not(evolucion)
			if event.key == pygame.K_r:
				for i in range(len(juego)):
					for k in range(len(juego[i])):
						juego[i][k]=random.randint(0,1)
			if event.key == pygame.K_c:
				for i in range(len(juego)):
					for k in range(len(juego[i])):
						juego[i][k]=0
		if event.type == pygame.KEYDOWN:
			if event.type == pygame.MOUSEBUTTONUP:
				pass
			if event.key == pygame.K_SPACE:
				pass
			if event.key == pygame.K_r:
				pass

	#dibujo
	#copia = copy.deepcopy(juego)
	copia = np.copy(juego)
	screen.fill(NEGRO)
	for i in range(ny):
		for k in range(nx):
			if juego[i][k]==1:
				pygame.draw.rect(screen,BLANCO,((k*ancho_casillas),(i*alto_casillas),ancho_casillas,alto_casillas))
			#pygame.draw.rect(screen,BLANCO,((k*ancho_casillas),(i*alto_casillas),ancho_casillas,alto_casillas),1)
			
			if evolucion:
				contador= copia[i-1][k-1] +copia[i-1][k] + copia[i-1][(k+1)%nx] + copia[i][k-1]+ copia[i][(k+1)%nx]+ copia[(i+1)%ny][k-1] + copia[(i+1)%ny][k] + copia[(i+1)%ny][(k+1)%nx]
				if juego[i][k]==1:
					if contador < 2 or contador >3:
						juego[i][k]=0
				if juego[i][k]==0:
					if contador == 3:
						juego[i][k]=1



	pygame.display.flip()
	clock.tick(10)