"""Use of recursive function to draw beautiful fractal patterns."""

### Sahil Islam ###
### 09/06/2020 ###

import pygame

pygame.init()

width = 800
height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))


def circle(x, y, r):
    pygame.draw.circle(screen, red, (int(x), int(y)), int(r), 1)
    if r > 2:
        circle(x + 0.5 * r, y, r * 0.5)
        circle(x - 0.5 * r, y, r * 0.5)
        circle(x, y + 0.5 * r, r * 0.5)


while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    circle(width / 2., height / 2., 300)

    pygame.display.update()
    clock.tick(100)
