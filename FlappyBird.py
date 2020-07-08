### Flappy Bird Game ###
### Sahil Islam ###
### 31/05/2020 ###


import pygame
import numpy as np
import time

pygame.init()

display_width = 450
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
whiten = (230, 230, 250)
color1 = (78, 138, 211)
color2 = (154, 3, 33)
color3 = (242, 238, 29)

pygame.mixer.music.load('background.mp3')
# pygame.mixer.music.load('bell.mp3')
# pygame.mixer.music.load('gameOver.mp3')

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("FLAPPY BIRD")
clock = pygame.time.Clock()



def bird(x, y):
    w = 10
    h = 10
    pygame.draw.ellipse(screen, color3, [int(x), int(y), int(w), int(h)])


def block(x, y, h, w, blank):
    yd = y + h + blank
    hd = display_height - yd
    pygame.draw.rect(screen, color2, [int(x), int(y), int(w), int(h)])
    pygame.draw.rect(screen, color2, [int(x), int(yd), int(w), int(hd)])


def score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render(("Score: " + str(count)), True, whiten)
    screen.blit(text, (0, 0))


def textObjects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def messageDisplay(text, posX, posY, size):
    largeText = pygame.font.SysFont('monaco', size)
    text_surface, text_rectangle = textObjects(text, largeText)
    text_rectangle.center = (int(posX), int(posY))
    screen.blit(text_surface, text_rectangle)
    pygame.display.update()
    time.sleep(2)
    gameLoop()


def crash(count):
    messageDisplay("* You Crashed  * " + " Final Score: " + str(count), display_width/2., display_height/2., size=30)


def gameLoop():
    pygame.mixer.music.play(-1)
    fps = 70

    birdXpos = display_width / 8.0
    birdYpos = display_height / 2.
    birdYvel = 0

    blockXpos = display_width
    blockYpos = 0
    blockXvel = -5
    blockWidth = 50

    blockHeight = np.random.randint(0, display_height)
    blankSpace = np.random.randint(50, 100)
    count = 0

    gameExit = False
    while not gameExit:
        screen.fill(color1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    birdYvel = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    birdYvel = +5

        birdYpos += birdYvel

        blockXpos += blockXvel

        if blockXpos + blockWidth < 0:
            blockXpos = display_width + 10.
            fps += 2
            blockHeight = np.random.randint(0, display_height / 2.)
            blankSpace = np.random.randint(50, 200)

        if blockXpos < birdXpos < blockXpos + blockWidth:
            count += 0.1
            #pygame.mixer.music.play(0)


        score(round(count))

        if birdYpos < 0 or birdYpos + 10 > display_height or \
                blockXpos < birdXpos < blockXpos + blockWidth and birdYpos < blockYpos + blockHeight or \
                blockXpos < birdXpos < blockXpos + blockWidth and birdYpos > blockYpos + blockHeight + blankSpace:

            pygame.mixer.music.stop()
            # pygame.mixer.music.play(-1)
            crash(round(count))



        bird(birdXpos, birdYpos)

        block(blockXpos, blockYpos, blockHeight, blockWidth, blankSpace)
        pygame.display.update()
        clock.tick(fps)


gameLoop()
pygame.quit()
quit()
