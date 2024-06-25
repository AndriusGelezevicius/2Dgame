import pygame
from Player import Player


pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2Dgame")

# Load sprite Sheets //:TODO: add more images
player_walkind_down = pygame.image.load("Images/rpg_sprite_walk_down.png").convert_alpha()
player_walkind_up = pygame.image.load("Images/rpg_sprite_walk_up.png").convert_alpha()
player_walkind_right = pygame.image.load("Images/rpg_sprite_walk_right.png").convert_alpha()
player_walkind_left = pygame.image.load("Images/rpg_sprite_walk_left.png").convert_alpha()
player = Player(player_walkind_down, player_walkind_up, player_walkind_right, player_walkind_left)

sprites = pygame.sprite.Group()
sprites.add(player)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.walking_down()
            elif event.key == pygame.K_UP:
                player.walking_up()
            elif event.key == pygame.K_RIGHT:
                player.walking_right()
            elif event.key == pygame.K_LEFT:
                player.walking_left()

    sprites.update()
    screen.fill((0, 255, 0))
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
