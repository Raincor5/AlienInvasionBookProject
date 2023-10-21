import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialising the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and set its starting position.
        self.image = pg.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)