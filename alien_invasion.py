import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        # Update the ship's position.
        ship.update()
        # Update position of bullets and get rid of old bullets.
        gf.update_bullets(bullets)

        # Redraw the screen during each pass through the loop.
        # Blit (overlap) the ship on the screen at the rect position.
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()