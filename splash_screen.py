import pygame.font


class SplashScreen:
    """A class which generates text for screen before
    gameplay begins"""

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # Font settings
        self.text_color = (30, 30, 30)
        self.font_big = pygame.font.SysFont(None, 88)
        self.font_small = pygame.font.SysFont(None, 28)

        # Prep messages
        self.prep_open_screen()
        self.prep_instructions()

    def prep_open_screen(self):
        # Generate 'Space Fighter!' message
        open_screen_str = "SPACE FIGHTER!"
        self.set_headline(open_screen_str)

    def prep_game_over(self):
        # Generate 'Game Over' message
        game_over_str = "GAME OVER!"
        self.set_headline(game_over_str)

    def set_headline(self, input_str):
        self.headline_image = self.font_big.render(input_str, True,
                                                   self.text_color)

        self.headline_rect = self.headline_image.get_rect()
        self.headline_rect.centerx = self.screen_rect.centerx
        self.headline_rect.centery = self.screen_rect.centery - 100

    def prep_instructions(self):
        """Generate message on how to start game"""
        instructions_str = "Press P to play, or Q to quit"
        self.insturctions_image = self.font_small.render(instructions_str, True,
                                self.text_color, self.ai_settings.bg_color)

        self.insturctions_rect = self.insturctions_image.get_rect()
        self.insturctions_rect.centerx = self.screen_rect.centerx
        self.insturctions_rect.bottom = self.screen_rect.bottom - 100

    def draw_splash_screen(self):
        # Draw the screen
        self.screen.blit(self.headline_image, self.headline_rect)
        self.screen.blit(self.insturctions_image, self.insturctions_rect)
