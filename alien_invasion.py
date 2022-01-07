import os
import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """manage game assets"""

    def __init__(self):
        """initialize game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            # watch for keyboard mouse movements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # refresh screen
            pygame.display.flip()

if __name__ == "__main__":
    # make a game instance
    ai = AlienInvasion()
    ai.run_game()