import json
import pygame

from utills.models import Settings


with open("settings.json", "r") as f:
    data = json.load(f)
    settings = Settings(**data)

pygame.init()
display = pygame.display.set_mode((settings.display.width, settings.display.height))
clock = pygame.time.Clock()
condition = True

while condition:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condition = False

        display.fill("white")
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
