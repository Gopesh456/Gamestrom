import pygame
import math

# Intilize the game
pygame.init()
# creats a screen(Width and Hight)
screen = pygame.display.set_mode((800, 600))
# Creating a title:
pygame.display.set_caption("Space Invader")
# Creating a Icon:
icon = pygame.image.load("maze icon.png")
pygame.display.set_icon(icon)
score = 0
# Background
Bg = pygame.image.load("maze.png")
BgX = 0
BgY = 0
Bg2 = pygame.image.load("Maze 2.jpg")
BgX2 = 0
BgY2 = 0
# Creating a Player:
player1 = pygame.image.load("car top view right.png")
player1X = 64
player1Y = 418
player_left = pygame.image.load("car top view left.png")
player_right = pygame.image.load("car top view right.png")
player_back = pygame.image.load("car top view back.png")
player_up = pygame.image.load("car top view.png")
enemy = pygame.image.load("ufo.png")
enemyx = 400
enemyY = 600


def isCollision(enemyx, enemyY, player1X, player1Y):
    distance = math.sqrt(math.pow(enemyx - player1X, 2) + (math.pow(enemyY - player1Y, 2)))
    print(distance)


# game loop:
running = True
while running:
    # Screen color (RGB) maxi=255.Two brackets
    #screen.fill((255, 255, 255))
   # screen.blit(Bg, (BgX, BgY))
    #screen.blit(player1, (player1X, player1Y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
       # isCollision(enemyx, enemyY, player1X, player1Y)
        # It checks weather a key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1X -= 9
                player1 = player_left
            if event.key == pygame.K_RIGHT:
                player1X += 9
            player1 = player_right
            if event.key == pygame.K_UP:
                player1Y -= 9
                player1 = player_up
            if event.key == pygame.K_DOWN:
                player1Y += 9
                player1 = player_back
            if event.key == pygame.K_LEFT:
                player1X -= 9
            if event.key == pygame.K_RIGHT:
                player1X += 9
            if event.key == pygame.K_UP:
                player1Y -= 9
            if event.key == pygame.K_DOWN:
                player1Y += 9
    screen.blit(player1, (player1X, player1Y))
if player1X == 694:
    Bg = Bg2
    player1X = 100
    player1Y = 76

pygame.display.update()
