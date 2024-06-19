import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.sheet = image
        self.image = self.sheet # initial image
        self.rect = self.image.get_rect()
    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width), 0, width, height)
        image = pygame.transform.scale(image, (image * scale, height * scale))
        image.set_colorkey(colour)
        return image