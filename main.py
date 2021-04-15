from constants import *

def initialize():
    # Initialize pygame
    pygame.init()
    # create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_CAPTION)
    icon = pygame.image.load(GAME_ICON)
    pygame.display.set_icon(icon)

    return screen


def logic(screen):
    global angle1, angle2, angle_velocity1, angle_velocity2
    # calculate the acceleration
    angle_acceleration1 = formula.FirstAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity,
                                                     angle_velocity1, angle_velocity2)
    angle_acceleration2 = formula.SecondAcceleration(angle1, angle2, mass1, mass2, length1, length2, Gravity,
                                                      angle_velocity1, angle_velocity2)

    x1 = float(length1 * math.sin(angle1) + x_offset)
    y1 = float(length1 * math.cos(angle1) + y_offset)

    x2 = float(x1 + length2 * math.sin(angle2))
    y2 = float(y1 + length2 * math.cos(angle2))

    # the angle varies with respect to the velocity and the velocity with respect to the acceleration
    angle_velocity1 += angle_acceleration1
    angle_velocity2 += angle_acceleration2
    angle1 += angle_velocity1
    angle2 += angle_velocity2

    scatter1.append((x1, y1))
    scatter2.append((x2, y2))

    for my_point in scatter2:
        # random_color = (random.randint(20, 255), random.randint(20, 255), random.randint(20, 255))
        plot = point.Point(my_point[0], my_point[1], screen, white, scatter2)
        plot.draw()

    pygame.draw.line(screen, white, starting_point, (x1, y1), 6)

    pygame.draw.line(screen, white, (x1, y1), (x2, y2), 6)
    pygame.draw.circle(screen, white, (int(x2), int(y2)), 10)
    pygame.draw.circle(screen, (20, 200, 30), (int(x1), int(y1)), 20)
    if len(scatter1) > 1:
        pygame.draw.lines(screen, (100, 50, 100), False, scatter1, 1)


def main(screen):
    running = True

    while running:
        GAME_CLOCK.tick(GAME_FPS)
        screen.fill(black)

        # Key Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Game in-progress
        if running:
            # Logic Loop Handler
            logic(screen)

            pygame.display.update()
        else:
            pygame.quit()


if __name__ == "__main__":
    screen = initialize()
    main(screen)
