import sprite
import imagesheet
import pygame
import os

pygame.init()           #pylint: disable=E1101
w = pygame.display.set_mode([400, 400])
c = pygame.time.Clock()

xpos = 100
ypos = 100
sheet = imagesheet.ImageSheet(os.path.join(".", "spaceship_sprite.png"), 2, 2)
spaceship = sprite.Sprite(os.path.join(".", "spaceship_sprite.png"), xpos, ypos)
#spaceship = sprite.Sprite(sheet, xpos, ypos)
#spaceship.current_sprite = 3

drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #pylint: disable=E1101
            drawing = False

    w.fill((128, 128, 128))
    x,y = pygame.mouse.get_pos()
    spaceship.center = (x,y)
    spaceship.flip_y = False
    spaceship.draw()
    pygame.display.flip()
    c.tick(30)
