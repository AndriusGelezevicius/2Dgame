import pygame

class Treasure_chest(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.opened = False
        self.animation = False
        self.treasure_chest_images = []

    # Loading Treasure_chest images
        for i in range(8):
            self.treasure_chest_images.append(
                pygame.image.load(f"Images/Treasure_chest/treasure chest000{i}.png").convert_alpha())

        self.current_image = 0
        self.image = self.treasure_chest_images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def open_treasure_chest(self):
        if not self.opened:
            self.opened = True
            self.animation = True
    def update(self):
        if self.animation:
            self.current_image += 0.2

            if self.current_image >= len(self.treasure_chest_images):
                self.current_image = len(self.treasure_chest_images) - 1  # Stay on the last image
                self.animation = False
            self.image = self.treasure_chest_images[int(self.current_image)]



