import os
import pygame

def run_game():
    # Inilialize game and create a scree object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    # Start the main loop for the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
    