from constants import *   
from main import * 

def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, (255, 255, 255)))
    screen.blit(img, (x,y))