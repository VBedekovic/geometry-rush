import pygame
from util.window import prozor_igre, display_width

#color
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
grey=(128,128,128)
crimson=(220,20,60)

#text
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
        
    
#button
button_frame=pygame.image.load('sprites/menu/button_frame.png')
over_button_frame=pygame.image.load('sprites/menu/button_frame_selected.png')
over_button_frame_red=pygame.image.load('sprites/menu/button_frame_selected_red.png')
def button(text, font_size, boja, okvir, na_visini):
    button_rect=okvir.get_rect()
    button_rect.center=((display_width/2), na_visini)
    #print(button_rect) -->  # x=475 | y=250,450,650,850 | w=250 | h=100 
    prozor_igre.blit(okvir, button_rect)
    display_text(text, font_size, boja, na_visini)

#time
###timer
def sat(t):
    minute=t//60
    sekunde=t%60
    font = pygame.font.SysFont('Bauhaus 93',30)
    text = font.render('{:02d}:{:02d}'.format(minute, sekunde), True, black)
    prozor_igre.blit(text, (1120,0))

###ghost mode time
def ghost_vrijeme(t):
    sekunde=t//60
    font = pygame.font.SysFont('Bauhaus 93',35)
    if sekunde>3:
        text = font.render('ghost-time left: {:02d}s'.format(sekunde), True, black)
    elif t!=0:
        text = font.render('ghost-time left: {:02d}s'.format(sekunde), True, crimson)
    else:
        text = font.render('ghost-time left: none'.format(sekunde), True, crimson)
    text_rect=text.get_rect()
    text_rect.center=((display_width/2), 975)
    
    prozor_igre.blit(text, text_rect)


#score
def enemies_erased(count):
    font = pygame.font.SysFont('Bauhaus 93',30)
    text = font.render('Erased enemies: '+str(count), True, black)
    prozor_igre.blit(text, (0,0))

        
def scoreboard_dat(ime, score):
    with open('scoreboard.txt', 'r') as dat:
        redovi=dat.readlines()

    if len(redovi)!=0:
        for i in range(len(redovi)):
            redovi[i]=redovi[i][5:]

    redovi.append('{:12s}{}\n'.format(ime, score))

    redovi.sort(key=lambda x: int(x[12:-1]), reverse=True)

    for i in range(len(redovi)):
        redovi[i]='{:>4} '.format(str(i+1)+'.')+redovi[i]

    with open('scoreboard.txt', 'w') as dat:
        dat.writelines(redovi)

def high_score_beaten(score):
    with open('scoreboard.txt', 'r') as dat:
        broj=dat.readline()

    if broj!='':
        broj=int(broj[17:-1])

    if broj=='':
        return True
        
    if score > broj:
        return True
    
    return False
    
