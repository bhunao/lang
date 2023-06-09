import sys
import pygame

from string import ascii_letters,  digits


pygame.init()
height = 300
width = 150
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

def w(pos):
    return width/8*pos

def h(pos):
    return height/8*pos

def pos(x, y):
    return w(x), h(y)

size = pygame.math.Vector2(width/2, height/2)
size2 = size / 2.5

center_p = pygame.Rect(0,0, *size)
center_p.center = pos(4, 4)
top_p = pygame.Rect(0,0, *size2)
top_p.center = pos(4,2)
right_p = pygame.Rect(0, 0, *size2)
right_p.center = pos(6, 4)
down_p = pygame.Rect(0, 0, *size2)
down_p.center = pos(4, 6)
left_p = pygame.Rect(0, 0, *size2)
left_p.center = pos(2, 4)

topleft_p = pygame.Rect(0, 0, *size2)
topleft_p.center = pos(2.5, 2.5)
topright_p = pygame.Rect(0, 0, *size2)
topright_p.center = pos(5.5, 2.5)
bottomright_p = pygame.Rect(0, 0, *size2)
bottomright_p.center = pos(5.5, 5.5)
bottomleft_p = pygame.Rect(0, 0, *size2)
bottomleft_p.center = pos(2.5, 5.5)

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
letters = ascii_letters + digits
chosen = letters[nval]
bin_val = format(ord(chosen), 'b')
print(chosen,bin_val)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_letter():
    screen.fill("brown")
    pygame.draw.rect(screen, color1, center_p, border_radius=1000)
    for i, (n, point) in enumerate(zip(reversed(bin_val), points)):
        if int(n):
            color = color1 if i<=3 else color2
            pygame.draw.rect(screen, color, point, border_radius=100)
    draw_text(chosen, pygame.font.SysFont('Arial', 70), "brown", screen, w(4), h(4))

draw_letter()
while 1:
    # background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEWHEEL:
            nval += event.y

            if nval >= len(letters):
                nval = 0
            elif nval < 0:
                nval = len(letters) - 1

            chosen = letters[nval]
            bin_val = format(ord(chosen), 'b')
            print(chosen,bin_val)
            draw_letter()

    pygame.display.flip()
    clock.tick(60)
