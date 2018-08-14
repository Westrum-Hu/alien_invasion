import sys

import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_function as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets, and a group of alien
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Creating a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            # Update the ship's position.
            ship.update()
            # Update position of bullets and get rid of old bullets.
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        
        # Update position of aliens
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        # Redraw the screen during each pass through the loop.
        # Blit (overlap) the ship on the screen at the rect position.
        # Make the most recently drawn screen visible.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()