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

"""This specific method draws the Sierpinski triangle. (Both circle and square) """


#
def circle(x, y, r):
    pygame.draw.circle(screen, red, (int(x), int(y)), int(r), 1)
    if r > 2:
        circle(x + 0.5 * r, y, r * 0.5)
        circle(x - 0.5 * r, y, r * 0.5)
        circle(x, y + 0.5 * r, r * 0.5)


def square(x, y, w):
    pygame.draw.rect(screen, red, [int(x - w / 2.), int(y - w / 2.), int(w), int(w)], 1)
    if w > 2:
        square(x + 0.5 * w, y, w * 0.5)
        square(x - 0.5 * w, y, w * 0.5)
        square(x, y - 0.5 * w, w * 0.5)


#

while True:
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    square(width / 2., height / 2., 300)

    pygame.display.update()
    clock.tick(100)
