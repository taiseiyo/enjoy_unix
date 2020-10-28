#!/usr/bin/env python3
import sys
import pygame
from pygame.locals import QUIT, K_SPACE, KEYDOWN, K_ESCAPE

pygame.init()
surface = pygame.display.set_mode((400, 300))


def main():

    while True:
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                if(event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()

        surface.fill((0, 0, 0))
        pygame.display.update()


main()
