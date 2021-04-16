import pygame
import math

# constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
GAME_FPS = 30
GAME_CLOCK = pygame.time.Clock()

GAME_CAPTION = "Double Pendulum Sim"
GAME_ICON = "media/game_icon.png"

WHITE_COLOR = (255, 255 , 255)
BLACK_COLOR = (0, 0, 0)

STARTING_PIVOT = (int(SCREEN_WIDTH / 2) , int(SCREEN_HEIGHT / 2))

Gravity = 8 # 9.8

MASS_1 = 40
MASS_2 = 80
ROD_LENGTH_1 = 150
ROD_LENGTH_2 = 150

angle1 = math.pi/2
angle2 = math.pi/2
angle_velocity1 = 0
angle_velocity2 = 0
angle_acceleration1 = 0
angle_acceleration2 = 0

# Drawing Constants
ROD_THICKNESS = 6
MASS_1_RADIUS = MASS_1 * 1.5
MASS_2_RADIUS = MASS_2 * 1.5
# LINE_THICKNESS
# LINE_1_COLOR
# LINE_2_COLOR

scatter1 = []
scatter2 = []

x_offset = STARTING_PIVOT[0]
y_offset = STARTING_PIVOT[1]

import formula
import point
import random
