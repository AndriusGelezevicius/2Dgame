import pygame
from Player import Player


pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2Dgame")

# Load sprite Sheets //:TODO: add more images
player_sheet = pygame.image.load("Images/rpg_sprite_walk_down.png").convert_alpha()
player = Player(player_sheet)

# Extract a frame from the sheet
frame_width = 22
frame_height = 32
scale = 2 # scale factor
frame = 0
player.image = player.get_image(frame, frame_width,frame_height, scale, (255,255,255)) # black? idk

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 255, 0))
    screen.blit(player.image, (100,100))
    pygame.display.flip()
    clock.tick(60)
