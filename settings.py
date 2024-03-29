import pygame
pygame.init()

TILESIZE = 100
MARGINGAP = TILESIZE // 2

WIDTH = MARGINGAP * 2 + TILESIZE * 9
HEIGHT = MARGINGAP * 2 + TILESIZE * 9
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE,False)

startBoard =[[0,0,0,2,6,0,7,0,1],
             [6,8,0,0,7,0,0,9,0],
             [1,9,0,0,0,4,5,0,0],
             [8,2,0,1,0,0,0,4,0],
             [0,0,4,6,0,2,9,0,0],
             [0,5,0,0,0,3,0,2,8],
             [0,0,9,3,0,0,0,7,4],
             [0,4,0,0,5,0,0,3,6],
             [7,0,3,0,1,8,0,0,0]]


board = startBoard.copy()

highLightLeft = pygame.surface.Surface((TILESIZE,TILESIZE))
highLightLeft.fill("#2d3436")
highLightLeft.set_alpha(100)

highLightRight = pygame.surface.Surface((TILESIZE,TILESIZE))
highLightRight.fill("#d63031")
highLightRight.set_alpha(100)

winFont = pygame.font.SysFont("BIZ UDPゴシック",TILESIZE//2,False)
winText = winFont.render(f"Solved",True,"#2d3436")
winTextRect = winText.get_rect()
winTextRect.center = (WIDTH // 2, MARGINGAP // 2)
