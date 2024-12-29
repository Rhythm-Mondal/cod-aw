import json
import pygame


with open("settings.json", "w+") as f:
    settings = json.load(f)

pygame.init()
display = pygame.display.set_mode(
    (
        settings.get("display", {}).get("width", 720),
        settings.get("display", {}).get("height", 1280),
    )
)
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
