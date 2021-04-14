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

def main(screen):
    running = True

    while running:
        GAME_CLOCK.tick(GAME_FPS)
        screen.fill(BACKGROUND_COLOR)

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
            pygame.display.update()
        else:
            pygame.quit()


if __name__ == "__main__":
    screen = initialize()
    main(screen)
