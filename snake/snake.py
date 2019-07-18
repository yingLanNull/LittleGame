#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsclock = pygame.time.Clock()
simulator = pygame.display

screenWidth = 640
screenHeight = 480

backgroundColor = pygame.Color(255, 255, 255)
darkSlateGrayColor = Color(47, 79, 79)
whiteColor = Color(255, 255, 255)

screen = simulator.set_mode((screenWidth, screenHeight))
simulator.set_caption("snake")

RIGHT = 'right'
UP = 'up'
LEFT = 'left'
DOWN = 'down'



snakeposition = [100, screenWidth/8]
snakesegments = [[100, screenWidth/8], [80, screenWidth/8], [60, screenWidth/8]]
raspberryposition = [300, 200]
raspberryspawned = 1
direction = [RIGHT, UP]
changedirection = direction[random.randint(0, 1)]


def gameover():
    gameoverfont = pygame.font.Font('freesansbold.ttf', 60)
    gameoversurf = gameoverfont.render("Game Over", True, backgroundColor)
    gameoverrect = gameoversurf.get_rect()
    gameoverrect.midtop = (320, 180)
    screen.blit(gameoversurf, gameoverrect)
    simulator.flip()
    time.sleep(2)
    exit()


def exit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
                if event.key == K_RIGHT or event.key == K_d:
                    changedirection = RIGHT
                if event.key == K_LEFT or event.key == K_a:
                    changedirection = LEFT
                if event.key == K_UP or event.key == K_w:
                    changedirection = DOWN
                if event.key == K_DOWN or event.key == K_s:
                    changedirection = UP

        if changedirection == RIGHT and not direction == LEFT:
            direction = changedirection
        if changedirection == LEFT and not direction == RIGHT:
            direction = changedirection
        if changedirection == UP and not direction == DOWN:
            direction = changedirection
        if changedirection == DOWN and not direction == UP:
            direction = changedirection

        if direction == RIGHT:
            snakeposition[0] += 20
        if direction == LEFT:
            snakeposition[0] -= 20
        if direction == UP:
            snakeposition[1] += 20
        if direction == DOWN:
            snakeposition[1] -= 20
        snakesegments.insert(0, list(snakeposition))
        if snakeposition[0] == raspberryposition[0] and snakeposition[1] == raspberryposition[1]:
            raspberryspawned = 0
        else:
            snakesegments.pop()
        if raspberryspawned == 0:
            x = random.randrange(1, screenWidth / 2 / 10)
            y = random.randrange(1, screenHeight / 2 / 10)
            raspberryposition = [int(x * 20), int(y * 20)]
        raspberryspawned = 1
        screen.fill(darkSlateGrayColor)
        for position in snakesegments:
            pygame.draw.rect(screen, whiteColor, Rect(position[0], position[1], 20, 20))
        pygame.draw.rect(screen, backgroundColor, Rect(raspberryposition[0], raspberryposition[1], 20, 20))
        simulator.flip()
        if snakeposition[0] > (screenWidth - 20) or snakeposition[0] < 0:
            gameover()
        if snakeposition[1] > (screenHeight - 20) or snakeposition[1] < 0:
            gameover()
        for snakebody in snakesegments[1:]:
            if snakeposition[0] == snakebody[0] and snakeposition[1] == snakebody[1]:
                gameover()
        fpsclock.tick(6)
