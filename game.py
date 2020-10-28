#!/usr/bin/env python3
import sys
import random
import pygame
from pygame.locals import QUIT, K_SPACE, KEYDOWN, K_ESCAPE, K_UP

pygame.init()
surface = pygame.display.set_mode((400, 300))


def main():

    flag = True
    images = ["./image/choki_new.png",
              "./image/gu_new.png", "./image/pa_new.png"]
    while True:
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

                elif(event.key == K_SPACE):
                    if(flag == True):
                        flag = False
                    elif(flag == False):
                        flag = True

                    target_index = random.randint(0, 2)

        surface.fill((0, 0, 0))

        if(flag == True):
            target = pygame.image.load(images[random.randint(0, 2)])
        else:
            target = pygame.image.load(images[target_index])

        surface.blit(target, (100, 100))
        pygame.display.update()


main()
