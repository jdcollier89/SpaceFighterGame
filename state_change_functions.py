import pygame
import sys
import game_functions as gf


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Start a new game"""
    if not stats.game_active and not stats.level_begun:
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)

        # Reset the games stats
        stats.reset_stats()
        stats.game_active = True
        stats.level_begun = True

        # Reset the scoreboard images
        sb.prep_images()

        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship
        gf.create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def pause_game(stats, splash_screen):
    if stats.level_begun:
        if not stats.game_active:
            # Set game to inactive & update splash screen message
            stats.game_active = True
            pygame.mouse.set_visible(False)
        else:
            # Set game to active, and begin play again
            stats.game_active = False
            pygame.mouse.set_visible(True)
            splash_screen.prep_pause_screen()


def quit_game(stats):
    stats.save_highscore()
    sys.exit()
