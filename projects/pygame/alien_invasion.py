import sys
import pygame as pg
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pg.init()

        self.clock = pg.time.Clock()
        self.settings = Settings()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pg.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        if event.key == pg.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_q:
            sys.exit()

    def _check_keyup_event(self, event):
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Updates images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pg.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()