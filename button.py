import pygame.font


class Button:

    def __init__(self, screen, msg, col):
        """Initialize the buttons attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48) # Default font at size 48

        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        if col == 'g': # Play Button
            self.button_color = (80, 220, 80)
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery + 100
        elif col == 'r': # Quit Button
            self.button_color = (220, 80, 80)
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery + 160

        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message on the screen"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
