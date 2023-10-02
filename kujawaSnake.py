#Daniel Kujawa
#9/4/2023
#drkujawa21 @github
import pygame
import time
import random

SNAKE_SPEED = 15

#Window Size
WINDOW_X = 720
WINDOW_Y = 480

#define colors
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)
PURPLE = pygame.Color(128, 0, 128)

#initialize pygame
pygame.init()

#initialize game window
pygame.display.set_caption("Greatest Snake Game Ever")
gameWindow = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

#FPS controller
fps = pygame.time.Clock()

#snake default position
snakePosition = [100, 50]

#define first 4 blocks of the snake body
snakeBody = [[100,50],[90,50],[80,50],[70,50]]

#fruit position
fruitPosition = [random.randrange(1, (WINDOW_X//10)) * 10,
                  random.randrange(1, (WINDOW_Y//10)) * 10]
fruitSpawn = True

#set the default snake direction towards right
direction = 'RIGHT'
changeTo = direction

#initial score
score = 0

def showScore(choice, color, font, size):
    #This function creates a rectangle that displays the score for the player
    #   Create font, surface, and the rectangle from that surface and creates
    #it all with blit
    
    #create font
    scoreFont = pygame.font.SysFont(font, size)

    #create the display for the surface object
    scoreSurface = scoreFont.render("Score : " + str(score), True, color)

    #create a rectangular object for the text surface
    scoreRect = scoreSurface.get_rect()

    #display text
    #blit - method that displays scores and where
    gameWindow.blit(scoreSurface, scoreRect)

def gameOver():
    #This function runs when either the player runs into a wall or itself
    #Displays scores then quits
    
    #create font
    myFont = pygame.font.SysFont("times new roman", 50)

    #create a text surface on which text will be drawn
    gameOverSurface = myFont.render("DEAD!!! Your score is: "
                                       + str(score), True, RED)

    #create a rectangular object for the text
    gameOverRect = gameOverSurface.get_rect()

    #set the position of the text
    gameOverRect.midtop = (WINDOW_X / 2, WINDOW_Y / 4)

    #blit then draws the text onto the screen
    gameWindow.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    #not sure what flip does

    #after 5 seconds, quit the program
    time.sleep(5)

    #deactivate the pygame library
    pygame.quit()

    quit()

#Main function
#Handles key input from user, prevents user from moving into snake,
#   increments player score whenever fruit is consumed, checks if player
#   hit a wall or the snake body.
#not sure why there is no main function definition
while True:

    #handling key presses on keyboard
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                changeTo = "UP"
            if event.key == pygame.K_DOWN:
                changeTo = "DOWN"
            if event.key == pygame.K_LEFT:
                changeTo = "LEFT"
            if event.key == pygame.K_RIGHT:
                changeTo = "RIGHT"

    #If two keys pressed simultaneously, snake will not move
    if changeTo == "UP" and direction != "DOWN":
        direction = "UP"
    if changeTo == "DOWN" and direction != "UP":
        direction = "DOWN"
    if changeTo == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if changeTo == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    #moving the snake
    if direction == "UP":
        snakePosition[1] -= 10
    if direction == "DOWN":
        snakePosition[1] += 10
    if direction == "LEFT":
        snakePosition[0] -= 10
    if direction == "RIGHT":
        snakePosition[0] += 10

    #Snake body growth mechanism
    #if fruits and snake collide, increment score by 10
    snakeBody.insert(0, list(snakePosition))
    if snakePosition[0] == fruitPosition[0] and snakePosition[1] == fruitPosition[1]:
        score += 10
        fruitSpawn = False
    else:
        snakeBody.pop()

    if not fruitSpawn:
        fruitPosition = [random.randrange(1, (WINDOW_X // 10)) * 10,
                          random.randrange(1, (WINDOW_Y // 10)) * 10]

    fruitSpawn = True
    gameWindow.fill(BLACK)

    body = 0
    for pos in snakeBody:
        if body == 0:
            pygame.draw.rect(gameWindow, RED, pygame.Rect(pos[0], pos[1], 10, 10))
            body += 1
        elif body % 2 == 0:
            pygame.draw.rect(gameWindow, PURPLE, pygame.Rect(pos[0], pos[1], 10, 10))
            body += 1
        else:
            pygame.draw.rect(gameWindow, GREEN, pygame.Rect(
                             pos[0], pos[1], 10, 10))
            body += 1

    pygame.draw.rect(gameWindow, WHITE, pygame.Rect(
        fruitPosition[0], fruitPosition[1], 10, 10))

    #Game over conditions
    #running into walls
    if snakePosition[0] < 0 or snakePosition[0] > WINDOW_X - 10:
        gameOver()
    if snakePosition[1] < 0 or snakePosition[1] > WINDOW_Y - 10:
        gameOver()
    
    #touching snake body
    for block in snakeBody[1:]:
        if snakePosition[0] == block[0] and snakePosition[1] == block[1]:
            gameOver()

    #display score continuously
    showScore(1, WHITE, "times new roman", 20)

    #refresh game screen
    pygame.display.update()

    #frames per second (fps) / refresh rate
    fps.tick(SNAKE_SPEED)
    
