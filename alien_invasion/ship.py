class Ship():

    def __init__(self, screen):
        """Initialize the ship image and get its rect."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom == self.screen_rect.bottom

    def blitme(self):
        """Drwa the ship at tits current location."""
        self.screen.blit(self.image, self.rect)