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

    def prep_instructions(self, instructions_str):
        """Generate message on how to start game"""
        self.insturctions_image = self.font_small.render(instructions_str, True,
                                self.text_color, self.ai_settings.bg_color)

        self.insturctions_rect = self.insturctions_image.get_rect()
        self.insturctions_rect.centerx = self.screen_rect.centerx
        self.insturctions_rect.bottom = self.screen_rect.bottom - 100

    def prep_open_screen(self):
        """Set the name of the game to display on opening screen"""
        open_screen_str = "SPACE FIGHTER!"
        instructions_str = "Press P to play, or Q to quit"
        self.set_headline(open_screen_str)
        self.prep_instructions(instructions_str)

    def prep_game_over(self):
        """Set the game over message"""
        game_over_str = "GAME OVER!"
        instructions_str = "Press P to play, or Q to quit"
        self.set_headline(game_over_str)
        self.prep_instructions(instructions_str)

    def prep_pause_screen(self):
        """Set the paused message"""
        pause_screen_str = "GAME PAUSED"
        instructions_str = "Press ESC key to resume play"
        self.set_headline(pause_screen_str)
        self.prep_instructions(instructions_str)

    def set_headline(self, input_str):
        """Set the contents and position of headline text"""
        self.headline_image = self.font_big.render(input_str, True,
                                                   self.text_color)

        self.headline_rect = self.headline_image.get_rect()
        self.headline_rect.centerx = self.screen_rect.centerx
        self.headline_rect.centery = self.screen_rect.centery - 100

    def draw_splash_screen(self):
        """Draw all splash screen contents"""
        self.screen.blit(self.headline_image, self.headline_rect)
        self.screen.blit(self.insturctions_image, self.insturctions_rect)
