import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, walk_down, walk_up, walk_right, walk_left):
        super().__init__()
        self.sheet_walk_down = self.load_frames(walk_down, 8)  #  8 frames
        self.sheet_walk_up = self.load_frames(walk_up, 8)      # 8 frames
        self.sheet_walk_right = self.load_frames(walk_right, 8)
        self.sheet_walk_left = self.load_frames(walk_left, 8)
        self.current_sheet = self.sheet_walk_down
        self.index = 0
        self.image = self.current_sheet[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
        self.last_update = pygame.time.get_ticks()
        self.is_walking = False
        self.speed = 5

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
        if self.is_walking and now - self.last_update > 100:
            self.index = (self.index + 1) % len(self.current_sheet)
            self.image = self.current_sheet[self.index]
            self.last_update = now

    def walking_down(self):
        self.rect.y += self.speed
        if self.current_sheet != self.sheet_walk_down:
            self.current_sheet = self.sheet_walk_down

        self.is_walking = True
    def walking_up(self):

        self.rect.y -= self.speed
        if self.current_sheet != self.sheet_walk_up:
            self.current_sheet = self.sheet_walk_up
        self.is_walking = True
    def walking_right(self):
        self.rect.x += self.speed
        if self.current_sheet != self.sheet_walk_right:
            self.current_sheet = self.sheet_walk_right
        self.is_walking = True
    def walking_left(self):
        self.rect.x -= self.speed
        if self.current_sheet != self.sheet_walk_left:
            self.current_sheet = self.sheet_walk_left
        self.is_walking = True
    def stop_walking(self):
        self.is_walking = False
        self.index = 0
        self.image = self.current_sheet[self.index] # Update the image to the first frame