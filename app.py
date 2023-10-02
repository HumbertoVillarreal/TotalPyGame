import pygame as pg

def player():
    screen.blit(playerImg, (xProtag,yProtag))

pg.init

screen = pg.display.set_mode((800,600))

#Title and icon
pg.display.set_caption("My Game")
icon = pg.image.load("icon.ico")
pg.display.set_icon(icon)

#Protag
playerImg = pg.image.load("player.png")
xProtag = (screen.get_width()/2) - (playerImg.get_width()/2)
yProtag = screen.get_height() - 100


#Game loop
loop = True
while loop:
    
    screen.fill((255,0,0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            loop = False
    
    player()
    
    pg.display.update()