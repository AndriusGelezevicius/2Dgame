import pygame
from Player import Player
from House import House

pygame.init()
clock = pygame.time.Clock()

screen_width = 640
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2Dgame")

background = pygame.image.load("Images/background_grass.png").convert()
house_image = pygame.image.load("Images/house.png").convert_alpha()
house = House(house_image, (550,50))

player_walkind_down = pygame.image.load("Images/rpg_sprite_walk_down.png").convert_alpha()
player_walkind_up = pygame.image.load("Images/rpg_sprite_walk_up.png").convert_alpha()
player_walkind_right = pygame.image.load("Images/rpg_sprite_walk_right.png").convert_alpha()
player_walkind_left = pygame.image.load("Images/rpg_sprite_walk_left.png").convert_alpha()
player = Player(player_walkind_down, player_walkind_up, player_walkind_right, player_walkind_left)

sprites = pygame.sprite.Group()
sprites.add(player, house)

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player.walking_down()
    elif keys[pygame.K_UP]:
        player.walking_up()
    elif keys[pygame.K_RIGHT]:
        player.walking_right()
    elif keys[pygame.K_LEFT]:
        player.walking_left()
    else:
        player.stop_walking()

    if player.rect.colliderect(house.rect):
        print("Collision")
        player.stop_walking()

    screen.blit(background, (0, 0))
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
