# 1-Import library
import pygame as py
from pygame.locals import *
import math
import random
import time

#2-Intialize the game
py.init()
py.mixer.init()
width,height = 400,600
screen = py.display.set_mode((width,height))
playerpos =[200-50,600-20]
botpos = [200-50,0]
ballpos = [200-15,300-15]
direcbot=[False,False]
direcplayer=[False,False]
ballspeedvec=[-0.3,1]
ballspeed = 0.3


#3 Load images
barimg = py.image.load("images/bar.png")
player = py.transform.scale(barimg,(100,20))
bot = py.transform.scale(barimg,(100,20))
ball = py.image.load("images/ball.png")
ball=py.transform.scale(ball,(30,30))
gameover=py.image.load("images/gameover.png")
youwin=py.image.load("images/youwin.png")
youwin = py.transform.scale(youwin, (width, height))
gameover = py.transform.scale(gameover, (width, height))



#4 loađ audio
hit = py.mixer.Sound("sounds/shoot.wav")
hit.set_volume(0.1)
py.mixer.music.load('sounds/moonlight.wav')
py.mixer.music.play(-1, 0.0)
py.mixer.music.set_volume(0.25)
#5 loop
running = 1
exitcode = 0
while running:
    screen.fill(0)

    screen.blit(player,playerpos)
    screen.blit(bot,botpos)
    screen.blit(ball,ballpos)
    for event in py.event.get():
        if event.type==py.QUIT:
            # if it is quit the game
            py.quit()
            exit(0)
        #5.1 move player bar catch key
        if event.type==py.KEYDOWN:
            if event.key==K_LEFT:
                direcplayer[0]=True
            elif event.key==K_RIGHT:
                direcplayer[1]=True
        if event.type==py.KEYUP:
            if event.key==K_LEFT:
                direcplayer[0]=False
            elif event.key==K_RIGHT:
                direcplayer[1]=False


    #5.2 ball move
    ballpos[0]+=ballspeedvec[0]*ballspeed
    ballpos[1]+=ballspeedvec[1]*ballspeed

    #5.3ball collison
    ballrect=py.Rect(ball.get_rect())
    playerrect=py.Rect(player.get_rect())
    botrect=py.Rect(bot.get_rect())
    #5.3.1 set rectangle
    ballrect.top=ballpos[1]
    ballrect.left=ballpos[0]
    ballrect.right=ballpos[0]+30
    ballrect.bottom=ballpos[1]+30

    playerrect.top=playerpos[1]
    playerrect.bottom=playerpos[1]+20
    playerrect.left=playerpos[0]
    playerrect.right=playerpos[0]+100

    botrect.bottom=botpos[1]+20
    botrect.top=botpos[1]+20
    botrect.left=botpos[0]
    botrect.right=botpos[0]+100
    #5.3.2 check collision
    if ballrect.colliderect(playerrect):
        ballspeedvec[1]*=-1
        ballspeed*=1.01
        hit.play()
    if ballrect.colliderect(botrect):
        ballspeedvec[1]*=-1
        ballspeed*=1.01
        hit.play()
    if ballrect.left < 10 or ballrect.right > 400:
        ballspeedvec[0]*=-1
        ballspeed*=1.01
        hit.play()



    #6 move player bar
    if direcplayer[0] and playerpos[0]>0:
        playerpos[0]-=0.3
    elif direcplayer[1] and playerpos[0]<400-100:
        playerpos[0]+=0.3


    #7 bot auto move
    if ballpos[0] - botpos[0] > 0 and ballpos[0] < 300 and abs(ballpos[0] - botpos[0]) > 0.3:
        botpos[0]+=0.1
    elif ballpos[0] - botpos[0] < 0 and ballpos[0] > 0 and abs(ballpos[0] - botpos[0]) > 0.3 :
        botpos[0]-=0.1


    #8 win-lose condition
    if ballpos[1] > 600:
        exitcode=0
        running=0
    if ballpos[1] < 0:
        exitcode=1
        running=0


    py.display.flip()

# 9. Win-lose display
if exitcode==0:
    screen.blit(gameover, (0,0))
else:
    screen.blit(youwin, (0,0))
while 1:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit(0)
    py.display.flip()

