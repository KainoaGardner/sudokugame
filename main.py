import pygame
from settings import *
from display import display
pygame.init()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                tileR = (mousePos[1] - MARGINGAP) // TILESIZE
                tileC = (mousePos[0] - MARGINGAP) // TILESIZE


        display()
    pygame.quit()

main()