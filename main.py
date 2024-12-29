import json
import pygame

from utills.models import Settings
from base.entities import Environment, Agent

with open("settings.json", "r") as f:
    data = json.load(f)
    settings = Settings(**data)

pygame.init()
display = pygame.display.set_mode((settings.display.width, settings.display.height))
clock = pygame.time.Clock()
condition = True


current_environment = Environment({"left": 0, "right": 512, "top": 0, "bottom": 512}, [], [])


while condition:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            condition = False

        display.fill("white")
        pygame.display.flip()
        clock.tick(60)

pygame.quit()
