import pygame 
import random
import time
pygame.init()

width = 1920
height = 1080

gameDisplay = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
clock = pygame.time.Clock()
values= []

white = (255,255,255)
flag = True
black = (0,0,0)

def draw():
	gameDisplay.fill(black)
	for i in range(width):
		pygame.draw.line(gameDisplay,white,(i,height),(i,height - values[i]))
	pygame.display.update()
		
def start():
	for i in range(width):
		r = random.randrange(height)
		values.append(r)
	sort()

def sort():
	for i in range(width):
		draw()

		for j in range(width - i - 1):
			a = values[j]
			b = values[j+1]
			if a>b:
				swap(values,j,j+1)
	flag = False


def swap(l,a,b):
	temp = l[a]
	l[a] = l[b]
	l[b] = temp


while True:
	start()
	if flag:
		pygame.quit()
		exit()
	pygame.display.update()
	clock.tick(1)


