import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from splash_screen import SplashScreen
from ship import Ship
from background import Background
import game_functions as gf
import check_event_functions as ce


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Space Fighter')

    # Set the background
    background = Background(screen, ai_settings)

    # Make the buttons and splash screen
    play_button = Button(screen, "Play", "g")
    quit_button = Button(screen, "Quit", "r")
    splash_screen = SplashScreen(screen, ai_settings)

    # Create an instance to store game stats & create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets & aliens in
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        ce.check_events(ai_settings, screen, stats, sb, play_button, quit_button, ship,
                        aliens, bullets, splash_screen)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets, splash_screen)

        gf.update_screen(screen, stats, sb, ship, aliens,
                         bullets, play_button, quit_button, splash_screen, background)

        # Make the most recently drawn screen visible
        pygame.display.flip()


run_game()
