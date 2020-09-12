#!/usr/bin/python3

import pygame
from time import sleep
from random import randint

# initialize packages from pygame
pygame.init()

# used var
screen_width = 600
screen_height = 600

dark = (13, 15, 20)
red = (255, 0, 0)
blue = (100,149,237)
yellow = (255, 255, 84)
green = (81, 255, 61)

fps = 30

# creating game window
canvas = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shad0w-Snake")
pygame.display.update()


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)


#fuctions
def text_screen(text, color, position_x, position_y):
    screen_text = font.render(text, True, color)
    canvas.blit(screen_text, [position_x, position_y])

def plot_snake(window, color, snake_list, snake_len, snake_width):
    for x,y in snake_list:
        pygame.draw.rect(window, color, [x, y, snake_width, snake_len])


def gameloop():
    # essential variables
    exit_game = False
    game_over = False

    # object data
    snake_len = 10
    snake_width = 10

    position_x = 300
    position_y = 300
    velocity_x = 0
    velocity_y = 0

    food_size = 8

    food_x = randint(60, screen_width)
    food_y = randint(60, screen_height)

    score = 0

    snake_list = []
    snake_block = 1

    # creating game loop
    while not exit_game:
        if game_over:
            canvas.fill(dark)

            text_screen('GAME OVER', red, 200, 260)
            text_screen('YOUR SCORE IS : ' + str(score), yellow, 180, 280)
            text_screen('Press Enter to Restart', green, 160, 320)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        canvas.fill(dark)
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        velocity_x += 8
                        velocity_y = 0

                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        velocity_x -= 8
                        velocity_y = 0

                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        velocity_y -= 8
                        velocity_x = 0

                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        velocity_y += 8
                        velocity_x = 0

            position_x += velocity_x
            position_y += velocity_y

            if abs(position_x - food_x) < 11 and abs(position_y - food_y) < 14:
                score += 8
                snake_block += 5

                food_x = randint(40, screen_width/1.5)
                food_y = randint(40, screen_height/1.5)

            canvas.fill(dark)
            text_screen("Score : " + str(score), green, 0, 0)

            head = []
            head.append(position_x)
            head.append(position_y)
            snake_list.append(head)

            if len(snake_list) > snake_block:
                del snake_list[0]

            if position_x > screen_width-20 or position_x <= 0 or position_y >= screen_height-10 or position_y <= 0:
                game_over = True

            if head in snake_list[:-1]:
                game_over = True

            plot_snake(canvas, blue, snake_list, snake_len, snake_width)
            pygame.draw.circle(canvas, yellow, [food_x, food_y], food_size)


        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()


gameloop()