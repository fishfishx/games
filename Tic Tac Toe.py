import pygame,sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((700,600))
board = [[0,0,0],[0,0,0],[0,0,0]]
turn =  1
inboard = True

def drawboard(screen):
    pygame.draw.line(screen,(0,0,0),(200,300),(500,300),8)
    pygame.draw.line(screen,(0,0,0),(200,400),(500,400),8)
    pygame.draw.line(screen,(0,0,0),(300,200),(300,500),8)
    pygame.draw.line(screen,(0,0,0),(400,200),(400,500),8)

def drawcircle(screen,x,y,r):
    pygame.draw.circle(screen,(0,0,0),(x,y),r,8)
def drawx(x,y,txt):
    screen.blit(txt,(x-25,y-35))

x = y = 0
r = 30
font1 = pygame.font.Font(None,120)
txt1 = font1.render('X',True,(0,0,0))
screen.fill((255,255,255))
drawboard(screen)
while True:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            x,y = event.pos
            inboard = True
            if x > 200 and x < 300 and y > 200 and y < 300 and board[0][0] == 0 and turn == 1:
                x,y = 250,250
                board[0][0] = 1
            elif x > 300 and x < 400 and y > 200 and y < 300 and board[0][1]:
                x,y = 350,250
                board[0][1] = 1
            elif x > 400 and x < 500 and y > 200 and y < 300:
                x,y = 450,250
            elif x > 200 and x < 300 and y > 300 and y < 400:
                x,y = 250,350
            elif x > 300 and x < 400 and y > 300 and y < 400:
                x,y = 350,350
            elif x > 400 and x < 500 and y > 300 and y < 400:
                x,y = 450,350
            elif x > 200 and x < 300 and y > 400 and y < 500:
                x,y = 250,450
            elif x > 300 and x < 400 and y > 400 and y < 500:
                x,y = 350,450
            elif x > 400 and x < 500 and y > 400 and y < 500:
                x,y = 450,450
            else:
                inboard = False
            if turn == 1 and inboard == True:
                drawcircle(screen,x,y,r)
                turn = 2
            elif turn == 2 and inboard == True:
                drawx(x,y,txt1)
                turn = 1
        elif event.type in (QUIT,None):
            sys.exit()


    pygame.display.update()
