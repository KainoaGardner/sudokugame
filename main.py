import pygame
from settings import *
from display import *

pygame.init()

def main():
    run = True
    board.makeBoard()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                if MARGINGAP <= mousePos[0] <= WIDTH - MARGINGAP and MARGINGAP <= mousePos[1] <= HEIGHT - MARGINGAP:
                    tileR = (mousePos[1] - MARGINGAP) // TILESIZE
                    tileC = (mousePos[0] - MARGINGAP) // TILESIZE
                    clickedTile = (tileR,tileC)
                    if event.button == 1:
                        board.leftRight = "Left"
                    elif event.button == 3:
                        board.leftRight = "Right"
                    if clickedTile == board.highLight:
                        board.highLight = ()
                        board.leftRight = ""
                    else:
                        board.highLight = (tileR,tileC)


        display()
    pygame.quit()

main()