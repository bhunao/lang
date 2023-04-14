import random
import sys
import pygame

from string import ascii_letters


pygame.init()
height = 150
width = 150
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def w(pos):
    return width/8*pos

def h(pos):
    return height/8*pos


size = pygame.math.Vector2(width/2, height/2)
size2 = size / 2.5

center_p = pygame.Rect(0,0, *size)
center_p.center = w(4), h(4)
top_p = pygame.Rect(0,0, *size2)
top_p.center = w(4), h(2)
right_p = pygame.Rect(0, 0, *size2)
right_p.center = w(6), h(4)
down_p = pygame.Rect(0, 0, *size2)
down_p.center = w(4), h(6)
left_p = pygame.Rect(0, 0, *size2)
left_p.center = w(2), h(4)

topleft_p = pygame.Rect(0, 0, *size2)
topleft_p.center = w(2.5), h(2.5)
topright_p = pygame.Rect(0, 0, *size2)
topright_p.center = w(5.5), h(2.5)
bottomright_p = pygame.Rect(0, 0, *size2)
bottomright_p.center = w(5.5), h(5.5)
bottomleft_p = pygame.Rect(0, 0, *size2)
bottomleft_p.center = w(2.5), h(5.5)

color1 = "yellow"
color2 = "brown"

points = [
    top_p,
    right_p,
    down_p,
    left_p,
    topleft_p,
    topright_p,
    bottomright_p,
    bottomleft_p
]

nval = 0
rand_val = random.choice(ascii_letters)
chosen = ascii_letters[nval]
bin_val = format(ord(chosen), 'b')
print(chosen,bin_val)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

while 1:
    # background
    screen.fill("brown")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            chosen = ascii_letters[nval]
            bin_val = format(ord(chosen), 'b')
            nval += 1
            if nval >= len(ascii_letters):
                nval = 0

            print(chosen,bin_val)
    

    pygame.draw.rect(screen, color1, center_p, border_radius=1000)

    for i, (n, point) in enumerate(zip(reversed(bin_val), points)):
        if int(n):
            color = color1 if i<=3 else color2
            pygame.draw.rect(screen, color, point, border_radius=100)
    
    draw_text(chosen, pygame.font.SysFont('Arial', 70), "brown", screen, w(4), h(4))
    pygame.display.flip()
    clock.tick(60)
