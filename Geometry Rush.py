import pygame, random, ctypes

ctypes.windll.user32.SetProcessDPIAware()


pygame.init()

display_width=1200          #in util
display_height=1000         #in util

#boje       #in util
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
grey=(128,128,128)
crimson=(220,20,60)


######prozor
from util.window import prozor_igre
#prozor_igre=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Geometry Rush')
game_icon=pygame.image.load('images/gameIcon.png')
pygame.display.set_icon(game_icon)

#in util  from here down,  above isn't
from util.loaded_files import pozadina, pozadina_igre_load_1, pozadina_igre_load_2, pozadina_igre, transparent
""" pozadina=pygame.image.load('images/pozadina.jpg')
pozadina_igre_load_1=pygame.image.load('images/pozadina granica 1.jpg')
pozadina_igre_load_2=pygame.image.load('images/pozadina granica 2.jpg')
pozadina_igre=pygame.image.load('images/pozadina granica final.jpg')
pozadina=pozadina.convert_alpha()
pozadina_igre_load_1=pozadina_igre_load_1.convert_alpha()
pozadina_igre_load_2=pozadina_igre_load_2.convert_alpha()
pozadina_igre=pozadina_igre.convert_alpha()
transparent=pygame.image.load('images/transparent.png')
transparent.set_alpha(100) """

#clock=pygame.time.Clock()   #moved to util.window
from util.window import clock

#izračuni   #in util
def vel_kut45(vel):
    br=(vel*(2**(1/2)))/2
    return br

def vel_kut_pol45(vel):
    a=vel*0.92388   #cos(45/2)
    b=vel*0.38627   #sin(45/2)   
    return a, b

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



#####main character
slika=pygame.image.load('sprites/mc/mc_slika.png')      #in util
mc_desno=pygame.image.load('sprites/mc/mc_right.png')
mc_lijevo=pygame.image.load('sprites/mc/mc_left.png')
mc_gore=pygame.image.load('sprites/mc/mc_up.png')
mc_dolje=pygame.image.load('sprites/mc/mc_down.png')
mc_erased=pygame.image.load('sprites/mc/mc_erased.png')
mc_died=pygame.image.load('sprites/mc/mc_died.png')
mc_happy=pygame.image.load('sprites/mc/mc_happy.png')
mc_ghost=pygame.image.load('sprites/mc/mc_ghost.png')
def mc(x, y, smjer_slike, ghost_mode=False):
    if not ghost_mode:
        if smjer_slike=='center':
            prozor_igre.blit(slika,(x,y))
        elif smjer_slike=='left':
            prozor_igre.blit(mc_lijevo,(x,y))
        elif smjer_slike=='right':
            prozor_igre.blit(mc_desno,(x,y))
        elif smjer_slike=='up':
            prozor_igre.blit(mc_gore,(x,y))
        elif smjer_slike=='down':
            prozor_igre.blit(mc_dolje,(x,y))
    else:
        prozor_igre.blit(mc_ghost,(x,y))
    

#####metak
from classes.Metak import Metak

#####enemy
from classes.Enemy import Enemy

#####powerups
coffee_sprite=pygame.image.load('sprites/powerup/coffee.png')
shotgun_sprite=pygame.image.load('sprites/powerup/shotgun.png')
machinegun_sprite=pygame.image.load('sprites/powerup/machine gun.png')
krug_sprite=pygame.image.load('sprites/powerup/krug.png')
ghost_plus_sprite=pygame.image.load('sprites/powerup/ghost plus.png')
nuke_gumica_sprite=pygame.image.load('sprites/powerup/nuke gumica.png')
star_sprite=pygame.image.load('sprites/powerup/super star.png')

from classes.Powerup import Powerup

from util.display import sat, ghost_vrijeme

from util.display import enemies_erased, scoreboard_dat, high_score_beaten
        


#####zvuk
pygame.mixer.music.load('music/Slip.wav')
pygame.mixer.music.set_volume(0.1)
marker_zvuk=pygame.mixer.Sound('sound/drawing_on_paper_with_marker.wav')
gumica_zvuk=pygame.mixer.Sound('sound/eraser.wav')
pokupljeno_zvuk=pygame.mixer.Sound('sound/pokupljeno.wav')  #in util
hit_zvuk=pygame.mixer.Sound('sound/pogodak.wav')
game_over_zvuk=pygame.mixer.Sound('sound/game over.wav')


#def main_menu_loop():
from game_states.main_menu import main_menu_loop

#def game_loop(play_game, exit_game):
from game_states.game import game_loop



#def play_again_loop(play_game, exit_game, score):
from game_states.play_again import play_again_loop

def scoreboard_loop(go_scoreboard, exit_game):
    with open('scoreboard.txt', 'r') as dat:
        scores=dat.readlines()

    ime=[]
    score=[]
    broj_ljudi=len(scores)
    for i in range(broj_ljudi):
        ime.append(scores[i][:17])
        score.append(scores[i][17:-1])
        
    granica_move=0
    granica_min, granica_max=0+granica_move, 9+granica_move
    
    go_back=False
    while not go_back:
        
        for event in pygame.event.get():
            #izlaz
            if event.type==pygame.QUIT:
                exit_game=True
                go_back=True
                go_scoreboard=False


        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click, _ , _ =pygame.mouse.get_pressed()

        
        #crtanje
        prozor_igre.fill(white)
        prozor_igre.blit(pozadina,(0,0))

        if broj_ljudi==0:
            display_text('empty', 40, grey, 300)

        else:
            if 475 < mouse_x < 475+250 and 600 < mouse_y < 600+100:
                button('up', 70, black, over_button_frame, 650)
                if mouse_click==1 and granica_move > 0:
                    granica_move-=1
            else:
                button('up', 70, grey, button_frame, 650)

            if 475 < mouse_x < 475+250 and 725 < mouse_y < 725+100:
                button('down', 70, black, over_button_frame, 775)
                if mouse_click==1 and granica_move+10 < broj_ljudi:
                    granica_move+=1
            else:
                button('down', 70, grey, button_frame, 775)
        

        if 475 < mouse_x < 475+250 and 850 < mouse_y < 850+100:
            button('back', 70, black, over_button_frame, 900)
            if mouse_click==1:
                go_back=True
                go_scoreboard=False
        else:
            button('back', 70, grey, button_frame, 900)

        
        multiline_text(ime[0+granica_move:10+granica_move], 400, 120, 40)
        multiline_text(score[0+granica_move:10+granica_move], 700, 120, 40)
        display_text('SCOREBOARD', 100, grey, 75)

        pygame.display.update()
        clock.tick(15)

    return go_scoreboard, exit_game


#def info_loop(go_info, exit_game):
from game_states.info import info_loop   

play_game=False
play_again=False
go_scoreboard=False
go_info=False
exit_game=False
while not exit_game:
    play_game, go_scoreboard, go_info, exit_game = main_menu_loop(play_game, go_scoreboard, go_info, exit_game)
    while play_game:
        play_game, play_again, exit_game, score = game_loop(play_game, exit_game)
        if play_again:
            play_game, exit_game=play_again_loop(play_game, exit_game, score)
    while go_scoreboard:
        go_scoreboard, exit_game=scoreboard_loop(go_scoreboard, exit_game)
    while go_info:
        go_info, exit_game=info_loop(go_info, exit_game)
        
pygame.quit()
quit()
