import pygame

class Treasure_chest(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.animation = False
        self.treasure_chest = []

    # Loading Treasure_chest images
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0000.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0001.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0002.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0003.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0004.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0005.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0006.png").convert_alpha())
        self.treasure_chest.append(pygame.image.load("Images/Treasure_chest/treasure chest0007.png").convert_alpha())

        self.current_image = 0
        self.image = self.treasure_chest[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        def update():
            if self.animation:
                self.animation += 1

                if self.current_image >= len(self.treasure_chest):
                    self.current_image = 0
                    self.animation = False
                self.image = self.treasure_chest[int(self.current_image)]

        def open_tresure_chest():
            self.animation = True
