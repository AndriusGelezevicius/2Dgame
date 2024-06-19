import pygame
from Player import Player


pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2Dgame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


screen.fill((0, 255, 0))
pygame.display.flip()
clock.tick(60)
