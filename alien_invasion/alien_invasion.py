import pygame
from pygame.sprite import Group

from ship import Ship
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the score board
    sb = Scoreboard(ai_settings, screen, stats)
    # Make the Play button
    play_button = Button(ai_settings, screen, "Play")

    # Make a ship, a group of bullets and a group or aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    background_image = pygame.image.load('images/sky.bmp').convert()

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, background_image, ship, aliens, bullets, play_button)
        # Redraw the screen during each pass through the loop.
        # gf.update_screen(ai_settings, screen, ship, alien_ship)


run_game()
