import pygame

class Ship:
    """manage the ship"""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship and get it's rect
        self.image = pygame.image.load('images/113-0.bmp')
        self.rect = self.image.get_rect()