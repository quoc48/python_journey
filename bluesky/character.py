import pygame

class Character:
    """A class to manage the character."""

    def __init__(self, ai_game):
        """Initialize the ship and set it's staring position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        # Load the character image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert_alpha()
        self.rect = self.image.get_rect()

        # Start each new character at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Convert the image to support transparency
        self.image = self.image.convert_alpha()

        # Set the color key for transparency
        self.image.set_colorkey((255, 255, 255))


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
