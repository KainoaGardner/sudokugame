import pygame
from settings import *

class Board():
    def __init__(self,board):
        self.board = board

    def drawBoard(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                pygame.draw.rect(screen,"#ecf0f1",pygame.Rect(MARGINGAP + TILESIZE * c,MARGINGAP + TILESIZE * r,TILESIZE,TILESIZE))

    def drawLines(self):
        for c in range(len(self.board) + 1):
            if c % 3 == 0:
                pygame.draw.line(screen, "#2d3436", (MARGINGAP + TILESIZE * c, MARGINGAP),(MARGINGAP + TILESIZE * c, HEIGHT - MARGINGAP), 5)
            else:
                pygame.draw.line(screen,"#2d3436",(MARGINGAP + TILESIZE * c,MARGINGAP),(MARGINGAP + TILESIZE * c,HEIGHT - MARGINGAP),2)
        for r in range(len(self.board) + 1):
            if r % 3 == 0:
                pygame.draw.line(screen,"#2d3436",(MARGINGAP,MARGINGAP + TILESIZE * r),(WIDTH - MARGINGAP,MARGINGAP + TILESIZE * r),8)
            else:
                pygame.draw.line(screen, "#2d3436", (MARGINGAP, MARGINGAP + TILESIZE * r),(WIDTH - MARGINGAP, MARGINGAP + TILESIZE * r), 2)

    def drawNumbers(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] != 0:
                    numberText = font.render(f"{self.board[r][c]}",True,"#2d3436")
                    numberTextRect = numberText.get_rect()
                    numberTextRect.center = (MARGINGAP + TILESIZE * c + TILESIZE // 2,MARGINGAP + TILESIZE * r + TILESIZE // 2)
                    screen.blit(numberText,numberTextRect)


    def update(self):
        self.drawBoard()
        self.drawNumbers()
        self.drawLines()
