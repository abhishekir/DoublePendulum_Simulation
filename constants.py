import pygame
import math

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_FPS = 30
GAME_CLOCK = pygame.time.Clock()

GAME_CAPTION = "Double Pendulum Sim"
GAME_ICON = "media/game_icon.png"
# BACKGROUND_COLOR = (0, 0, 50)

white = (255, 255 , 255)
black = (0, 0, 0)

mass1 = 80
mass2 = 40
length1 = 150
length2 = 150

angle1 = math.pi/2
angle2 = math.pi/2
angle_velocity1 = 0
angle_velocity2 = 0
angle_acceleration1 = 0
angle_acceleration2 = 0

Gravity = 9.8
scatter1 = []
scatter2 = []

starting_point = (int(SCREEN_WIDTH/2) , int(SCREEN_HEIGHT/4))

x_offset = starting_point[0]
y_offset = starting_point[1]

import formula
import point
import random
