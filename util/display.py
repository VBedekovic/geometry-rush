import pygame
from util.window import prozor_igre, display_width

black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
grey=(128,128,128)
crimson=(220,20,60)

#tekst      #in util
def text_objects(text, font, color):
    text_surf = font.render(text, True, color)
    return text_surf, text_surf.get_rect()

def title(text):
    naslov_font=pygame.font.SysFont('Bauhaus 93', 150)
    text_surf, text_rect = text_objects(text, naslov_font, grey)
    text_rect.center= ((display_width/2), 110)
    prozor_igre.blit(text_surf, text_rect)

def display_text(text, font_size, boja, na_visini):
    font=pygame.font.SysFont('Bauhaus 93', font_size)
    text_surf, text_rect = text_objects(text, font, boja)
    text_rect.center=((display_width/2), na_visini)
    prozor_igre.blit(text_surf, text_rect)

def multiline_text(text, x, y, font_size):
    font=pygame.font.SysFont('Bauhaus 93', font_size)
    redovi=[]
    for red in text:
        redovi.append(font.render(red, True, grey))
    for red in range(len(redovi)):
        prozor_igre.blit(redovi[red], (x, y+(red*font_size)+(5*red)))
        
    
#button     #in util
button_frame=pygame.image.load('sprites/menu/button_frame.png')
over_button_frame=pygame.image.load('sprites/menu/button_frame_selected.png')
over_button_frame_red=pygame.image.load('sprites/menu/button_frame_selected_red.png')
def button(text, font_size, boja, okvir, na_visini):
    button_rect=okvir.get_rect()
    button_rect.center=((display_width/2), na_visini)
    #print(button_rect) -->  # x=475 | y=250,450,650,850 | w=250 | h=100 
    prozor_igre.blit(okvir, button_rect)
    display_text(text, font_size, boja, na_visini)

