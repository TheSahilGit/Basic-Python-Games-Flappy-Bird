### Basic game to learn the syntax and usage of Pygame in Python.###
### Sahil Islam ###
### Date: 05/04/2020 ###

import pygame
import time
import random

pygame.init()

display_width = 860
display_height = 540

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
ball_color = (255, 255, 51)
red_var1 = (72, 0, 10)
whiten = (230, 230, 250)

display_surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BALL BOUNCING 2D")
clock = pygame.time.Clock()


def draw_ball(ball_color, ballx, bally, ballr):
    pygame.draw.ellipse(display_surface, red, [int(ballx), int(bally), int(2 * ballr), int(2 * ballr)])


def bouncer(bouncer_specs):
    pygame.draw.rect(display_surface, red_var1, bouncer_specs)


def text_objects(text, font):
    text_surface = font.render(text, True, red)
    return text_surface, text_surface.get_rect()


def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(("Score: " + str(count)), True, black)
    display_surface.blit(text, (0, 0))


def message(text):
    text_specs = pygame.font.Font("freesansbold.ttf", 100)
    text_surface, text_rectangle = text_objects(text, text_specs)
    text_rectangle.center = (int(display_width / 2), int(display_height / 2))
    display_surface.blit(text_surface, text_rectangle)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message("Game Over")


def game_loop():
    # Ball Details:
    ball_radius = 7
    ball_x_vel = 3
    ball_y_vel = 3
    ball_x_position = random.randrange(0, display_width - 2 * ball_radius)
    ball_y_position = random.randrange(0, (display_height - 2 * ball_radius) / 2.)

    # Bouncer Details:
    bouncer_length = 80
    bouncer_breadth = 7
    bouncer_y1 = display_height - (bouncer_breadth * 1.5)
    bouncer_x1 = display_width / 2
    bouncer_x_position_change = 0
    bouncer_x_position_change = 0

    scored = 0

    display_exit = False
    while not display_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    bouncer_x_position_change = +7
                if event.key == pygame.K_LEFT:
                    bouncer_x_position_change = -7
            if event.type == pygame.KEYUP:
                bouncer_x_position_change = 0

        display_surface.fill(whiten)
        score(scored)

        if ball_x_position > display_width - 2 * ball_radius or ball_x_position < 0:
            ball_x_vel *= -1

        if ball_y_position < 0:
            ball_y_vel *= -1

        # Collision condition

        if ball_y_position + 2 * ball_radius >= bouncer_y1 and \
                ball_x_position >= bouncer_x1 and \
                ball_x_position + 2 * ball_radius <= bouncer_x1 + bouncer_length :
            ball_y_vel *= -1.1

            scored += 1

        if ball_y_position + 2 * ball_radius > display_height:
            crash()

        if bouncer_x1 > display_width:
            bouncer_x1 = 0
        if bouncer_x1 < 0:
            bouncer_x1 = display_width - bouncer_length

        ball_x_position += ball_x_vel
        ball_y_position += ball_y_vel

        bouncer_x1 += bouncer_x_position_change

        bouncer_specs = [int(bouncer_x1), int(bouncer_y1), int(bouncer_length), int(bouncer_breadth)]
        bouncer(bouncer_specs)
        draw_ball(ball_color, ball_x_position, ball_y_position, ball_radius)
        pygame.display.update()
        clock.tick(100)


game_loop()
pygame.quit()
quit()
