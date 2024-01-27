import pygame
from settings import *

class Board():
    def __init__(self):
        self.board = []
        self.highLight = ()
        self.leftRight = ""
        self.rightBoard=[[0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],]
        self.lastTurn = ""
        self.pressed = False

        self.correctRows = 0
        self.correctCol = 0
        self.solved = False

    def makeBoard(self):
        for r in range(len(startBoard)):
            row = []
            for c in range(len(startBoard[r])):
                row.append(startBoard[r][c])
            self.board.append(row)

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
                    if startBoard[r][c] == 0:
                        numberText = font.render(f"{self.board[r][c]}",True,"#636e72")
                        numberTextRect = numberText.get_rect()
                        numberTextRect.center = (MARGINGAP + TILESIZE * c + TILESIZE // 2, MARGINGAP + TILESIZE * r + TILESIZE // 2)
                        screen.blit(numberText, numberTextRect)
                    elif startBoard[r][c] != 0:
                        numberText = font.render(f"{self.board[r][c]}", True, "#2d3436")
                        numberTextRect = numberText.get_rect()
                        numberTextRect.center = (MARGINGAP + TILESIZE * c + TILESIZE // 2,MARGINGAP + TILESIZE * r + TILESIZE // 2)
                        screen.blit(numberText,numberTextRect)

                if self.rightBoard[r][c] != 0:
                    numberText = font.render(f"{self.rightBoard[r][c]}", True, "#ff7675")
                    numberTextRect = numberText.get_rect()
                    numberTextRect.center = (
                    MARGINGAP + TILESIZE * c + TILESIZE // 2, MARGINGAP + TILESIZE * r + TILESIZE // 2)
                    screen.blit(numberText, numberTextRect)


    def highlightTile(self):
        if self.highLight != ():
            if self.leftRight == "Left":
                screen.blit(highLightLeft, (MARGINGAP + TILESIZE * self.highLight[1], MARGINGAP + TILESIZE * self.highLight[0]))
            elif self.leftRight == "Right":
                screen.blit(highLightRight,(MARGINGAP + TILESIZE * self.highLight[1], MARGINGAP + TILESIZE * self.highLight[0]))
    def typeNumber(self):
        key = pygame.key.get_pressed()
        if self.highLight != () and startBoard[self.highLight[0]][self.highLight[1]] == 0:
            if key[pygame.K_SPACE]:
                if self.leftRight == "Right":
                    self.rightBoard[self.highLight[0]][self.highLight[1]] = 0
                else:
                    self.board[self.highLight[0]][self.highLight[1]] = 0
                    self.rightBoard[self.highLight[0]][self.highLight[1]] = 0
                self.highLight = ()
            if key[pygame.K_1]:
                self.changeNumber(1)
            elif key[pygame.K_2]:
                self.changeNumber(2)
            elif key[pygame.K_3]:
                self.changeNumber(3)
            elif key[pygame.K_4]:
                self.changeNumber(4)
            elif key[pygame.K_5]:
                self.changeNumber(5)
            elif key[pygame.K_6]:
                self.changeNumber(6)
            elif key[pygame.K_7]:
                self.changeNumber(7)
            elif key[pygame.K_8]:
                self.changeNumber(8)
            elif key[pygame.K_9]:
                self.changeNumber(9)
        elif key[pygame.K_p] and self.pressed == False:
            self.win()
            self.pressed = True
        elif key[pygame.K_o] and self.pressed == False:
            self.board = solvedBoard
            self.pressed = True

        if key[pygame.K_p] == False and key[pygame.K_o] == False:
            self.pressed = False


    def changeNumber(self,number):
        if self.leftRight == "Right":
            self.rightBoard[self.highLight[0]][self.highLight[1]] = number
            self.board[self.highLight[0]][self.highLight[1]] = 0
        else:
            self.board[self.highLight[0]][self.highLight[1]] = number
            self.rightBoard[self.highLight[0]][self.highLight[1]] = 0
        self.highLight = ()

    def win(self):
        for r in range(len(self.board)):
            correctNumbers = 0
            if self.board[r].count(0) == 0:
                for c in range(len(self.board[r])):
                    if self.board[r].count(self.board[r][c]) == 1:
                        correctNumbers += 1
            if correctNumbers == 9:
                self.correctRows += 1

        for c in range(9):
            tempList = []
            correctNumber = 0
            for r in range(9):
                tempList.append(self.board[r][c])
            for n in range(1,10):
                if tempList[n - 1] != 0:
                    if tempList.count(n) == 1:
                        correctNumber += 1
            if correctNumber == 9:
                self.correctCol += 1

        if self.correctCol == 9 and self.correctRows == 9:
            self.solved = True
        else:
            self.correctCol = 0
            self.correctRows = 0

    def displayWin(self):
        if self.solved:
            screen.blit(winText, winTextRect)

    def update(self):
        self.typeNumber()
        self.drawBoard()
        self.highlightTile()
        self.drawNumbers()
        self.displayWin()
        self.drawLines()



