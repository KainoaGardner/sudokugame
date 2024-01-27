from settings import *
import pygame
from board import Board
board = Board()
def display():
    screen.fill("#d2b48c")
    board.update()
    pygame.display.update()
    clock.tick(FPS)

