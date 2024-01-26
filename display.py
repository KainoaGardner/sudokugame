from settings import *
import pygame
from board import Board
board = Board()
def display():
    screen.fill("#7f8c8d")
    board.update()
    pygame.display.update()
    clock.tick(FPS)

