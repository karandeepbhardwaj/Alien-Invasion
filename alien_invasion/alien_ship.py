import pygame


class AlienShip():

    def __init__(self, screen):
        """Initialize the alien Ship image and get its rect."""
        self.screen = screen

        # Load the alien Ship image and get its rect.
        self.image = pygame.image.load('images/space_Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new alien Ship at the bottom center of the screen.
        self.rect.center = self.screen_rect.center
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the alien Ship at tits current location."""
        self.screen.blit(self.image, self.rect)
