import pygame


class Background:
    """A class to handle the display of the background image of the game"""

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Load the background image
        self.image = pygame.image.load('images/background.jpg').convert_alpha()

    def draw_background(self):
        """Draw the background"""
        self.screen.blit(self.image, (0, 0))
