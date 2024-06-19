import pygame

pygame.init()
clock = pygame.time.Clock()

screen_width = 1000
screen_hight = 600
screen = pygame.display.set_mode((screen_width, screen_hight))
pygame.display.set_caption("2Dgame")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


screen.fill((0, 255, 0))
pygame.display.flip()
clock.tick(60)
