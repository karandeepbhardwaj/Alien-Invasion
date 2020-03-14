import sys
import pygame

from ship import Ship
from alien_ship import AlienShip
from settings import Settings
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)
    alien_ship = AlienShip(screen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ship)
        ship.update()
        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, screen, ship, alien_ship)


run_game()
