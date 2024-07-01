import pygame
from pygame import mixer, FULLSCREEN, RESIZABLE, NOFRAME

from Player import Player
from House import House
from Treasure_chest import Treasure_chest
from Tree_pine import Tree_pine

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("2Dgame")

background = pygame.image.load("Images/background_grass.png").convert()
walking_sound = pygame.mixer.Sound("Sounds/walking_grass.mp3")
open_chest_sound = pygame.mixer.Sound("Sounds/open_chest.wav")

house_image = pygame.image.load("Images/house.png").convert_alpha()
house = House(house_image, (550,50))

tree_pine_image_path = "Image/tree_pine.png"
tree_pine1 = Tree_pine(tree_pine_image_path, (350,500), 3)
tree_pine2 = Tree_pine(tree_pine_image_path, (400,550), 3)
tree_pine3 = Tree_pine(tree_pine_image_path, (580,350), 3)
tree_pine4 = Tree_pine(tree_pine_image_path, (550,450), 3)



player_walkind_down = pygame.image.load("Images/rpg_sprite_walk_down.png").convert_alpha()
player_walkind_up = pygame.image.load("Images/rpg_sprite_walk_up.png").convert_alpha()
player_walkind_right = pygame.image.load("Images/rpg_sprite_walk_right.png").convert_alpha()
player_walkind_left = pygame.image.load("Images/rpg_sprite_walk_left.png").convert_alpha()
player = Player(player_walkind_down, player_walkind_up, player_walkind_right, player_walkind_left)

sprites = pygame.sprite.Group()
sprites.add(player, house, tree_pine1, tree_pine2, tree_pine3, tree_pine4)

treasure_chest1 = Treasure_chest(100,100)
treasure_chest2 = Treasure_chest(300,350)
treasure_chest3 = Treasure_chest(100,450)
sprites.add(treasure_chest1, treasure_chest2, treasure_chest3)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys = pygame.key.get_pressed()
    is_walking = False
    if keys[pygame.K_DOWN]:
        player.walking_down()
        is_walking = True
    elif keys[pygame.K_UP]:
        player.walking_up()
        is_walking = True
    elif keys[pygame.K_RIGHT]:
        player.walking_right()
        is_walking = True
    elif keys[pygame.K_LEFT]:
        player.walking_left()
        is_walking = True
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


    # Character's walking sound
    if is_walking:
        if not pygame.mixer.get_busy():
            walking_sound.play()
    else:
        walking_sound.stop()

    # Collision with treasure chest
    for chest in [treasure_chest1, treasure_chest2, treasure_chest3]:
        if player.rect.colliderect(chest.rect):
            if not chest.opened:
                print(f"Collider with treasure chest")
                chest.open_treasure_chest()
                open_chest_sound.play()
                player.stop_walking()

    # character's movement boundaries
    if player.rect.x >= SCREEN_WIDTH - player.rect.width:
        player.rect.x = SCREEN_WIDTH - player.rect.width
    elif player.rect.x <= 0:
        player.rect.x = 0
    if player.rect.y >= SCREEN_HEIGHT - player.rect.height:
        player.rect.y = SCREEN_HEIGHT - player.rect.height
    elif player.rect.y <= 0:
        player.rect.y = 0

    screen.blit(background, (0, 0))
    sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
