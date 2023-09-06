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

#initialize pygame
pygame.init()

#initialize game window
pygame.display.set_caption("Greatest Snake Game Ever")
game_window = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

#FPS controller
fps = pygame.time.Clock()

#snake default position
snake_position = [100, 50]

#define first 4 blocks of the snake body
snake_body = [[100,50],[90,50],[80,50],[70,50]]

#fruit position
fruit_position = [random.randrange(1, (WINDOW_X//10)) * 10,
                  random.randrange(1, (WINDOW_Y//10)) * 10]
fruit_spawn = True

#set the default snake direction towards right
direction = 'RIGHT'
change_to = direction

#initial score
score = 0

def show_score(choice, color, font, size):
    #This function creates a rectangle that displays the score for the player
    #   Create font, surface, and the rectangle from that surface and creates
    #it all with blit
    
    #create font
    score_font = pygame.font.SysFont(font, size)

    #create the display for the surface object
    score_surface = score_font.render("Score : " + str(score), True, color)

    #create a rectangular object for the text surface
    score_rect = score_surface.get_rect()

    #display text
    #blit - method that displays scores and where
    game_window.blit(score_surface, score_rect)

def game_over():
    #This function runs when either the player runs into a wall or itself
    #Displays scores then quits
    
    #create font
    my_font = pygame.font.SysFont("comic sans", 50)

    #create a text surface on which text will be drawn
    game_over_surface = my_font.render("Your score is: "
                                       + str(score), True, RED)

    #create a rectangular object for the text
    game_over_rect = game_over_surface.get_rect()

    #set the position of the text
    game_over_rect.midtop = (WINDOW_X / 2, WINDOW_Y / 4)

    #blit then draws the text onto the screen
    game_window.blit(game_over_surface, game_over_rect)
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
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    #If two keys pressed simultaneously, snake will not move
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    #moving the snake
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    #Snake body growth mechanism
    #if fruits and snake collide, increment score by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (WINDOW_X // 10)) * 10,
                          random.randrange(1, (WINDOW_Y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(game_window, GREEN, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, WHITE, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    #Game over conditions
    #running into walls
    if snake_position[0] < 0 or snake_position[0] > WINDOW_X - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > WINDOW_Y - 10:
        game_over()
    
    #touching snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    #display score continuously
    show_score(1, WHITE, "comic sans", 20)

    #refresh game screen
    pygame.display.update()

    #frames per second (fps) / refresh rate
    fps.tick(SNAKE_SPEED)
    
