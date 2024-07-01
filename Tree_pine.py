import pygame

class Tree_pine(pygame.sprite.Sprite):
    def __init__(self, image, pos, scale=1.0):
        super().__init__()
        self.tree_pine_image = pygame.image.load("Images/tree_pine.png").convert_alpha()
        self.image = pygame.transform.scale(self.tree_pine_image,(int((self.tree_pine_image.get_width() * scale)), int((self.tree_pine_image.get_height() * scale))))
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
