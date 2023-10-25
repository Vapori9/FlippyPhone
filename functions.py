import pygame
import math

from settings import *
def rectCollision(rect1, rect2):
    return \
        (rect1[0] + rect1[2] >= rect2[0] and
        rect1[0] <= rect2[0] + rect2[2] and
        rect1[1] + rect1[3] >= rect2[1] and
        rect1[1] <= rect2[1] + rect2[3])


def flippy_screen_draw_rect(x, y, width, height, thickness, color, display):
    mapped_x = x*RS + 14*RS
    mapped_y = y*RS + 10*RS
    mapped_width = width*RS
    mapped_height = height*RS
    mapped_thickness = math.floor(thickness*RS)
    pygame.draw.rect(display, color, (mapped_x, mapped_y, mapped_width, mapped_height), mapped_thickness)

def flippy_screen_draw_circle(x, y, radius, color, display, width=0):
    mapped_x = x*RS + 14*RS
    mapped_y = y*RS + 10*RS
    mapped_radius = radius*RS
    mapped_width = int(math.ceil(width*RS))
    pygame.draw.circle(display, color, (mapped_x, mapped_y), mapped_radius, mapped_width)

def flippy_screen_draw_image(x, y, surface, display):
    mapped_x = x * RS + 14 * RS
    mapped_y = y * RS + 10 * RS
    scaled_surface = pygame.transform.scale(surface, (surface.get_size()[0] *RS, surface.get_size()[1] *RS))
    display.blit(scaled_surface, (mapped_x, mapped_y))

def flippy_screen_draw_text(x, y, size, text, display, color=(0,0,0)):
    mapped_x = x * RS + 14 * RS
    mapped_y = y * RS + 10 * RS
    mapped_size = int(math.ceil(size * RS))
    font = pygame.font.SysFont(None, mapped_size)
    renderText = font.render(text, True, color)
    display.blit(renderText, (mapped_x, mapped_y))




