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

        # Collision detection
    if player.rect.colliderect(house.rect):
        print("Collision")
        player.stop_walking()  # Stop animation
        # Adjust player position to avoid overlap
        if keys[pygame.K_DOWN]:
            player.rect.y -= player.speed
        elif keys[pygame.K_UP]:
            player.rect.y += player.speed
        elif keys[pygame.K_RIGHT]:
            player.rect.x -= player.speed
        elif keys[pygame.K_LEFT]:
            player.rect.x += player.speed

    # Boundaries of the game window
    if player.rect.x >= 610:
        player.rect.x = 610
    elif player.rect.x <= 0:
        player.rect.x = 0
    if player.rect.y >= 590:
        player.rect.y = 590
    elif player.rect.y <= 0:
        player.rect.y = 0




    screen.blit(background, (0, 0))
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
