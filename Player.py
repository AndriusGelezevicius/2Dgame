import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, walk_down, walk_up):
        super().__init__()
        self.sheet_walk_down = self.load_frames(walk_down, 8)  #  8 frames
        self.sheet_walk_up = self.load_frames(walk_up, 8)      # 8 frames
        self.current_sheet = self.sheet_walk_down
        self.index = 0
        self.image = self.current_sheet[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.animation_speed = 1
        self.last_update = pygame.time.get_ticks()
        self.is_walking = False

    def load_frames(self, sheet, num_frames):
        frames = []
        sheet_width, sheet_height = sheet.get_size()
        frame_width = sheet_width / num_frames
        for i in range(num_frames):
            frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, sheet_height))
            frame.set_colorkey((255,255,255))
            frames.append(frame)
        return frames

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:
            self.index = (self.index + 1) % len(self.current_sheet)
            self.image = self.current_sheet[self.index]
            self.last_update = now

    def walking_down(self):
        self.current_sheet = self.sheet_walk_down
        self.index = 0
        self.is_walking = True

    def walking_up(self):
        self.current_sheet = self.sheet_walk_up
        self.index = 0
        self.is_walking = False
