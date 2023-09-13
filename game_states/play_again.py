import pygame

from util.window import prozor_igre, clock
from util.display import white, grey, black, \
                            over_button_frame, button_frame, \
                            button, display_text, \
                            high_score_beaten, scoreboard_dat
from util.loaded_files import pozadina

from classes.MainCharacter import mc_happy, mc_died

def play_again_loop(play_game, exit_game, score):
    selected=False
    name=''
    while not selected:
        
        for event in pygame.event.get():
            #izlaz
            if event.type==pygame.QUIT:
                play_game=False
                exit_game=True
                selected=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    name=name[:-1]
                    
            if len(name)<10:   
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        name+='q'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_w:
                        name+='w'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_e:
                        name+='e'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        name+='r'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_t:
                        name+='t'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_z:
                        name+='y'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_u:
                        name+='u'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_i:
                        name+='i'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_o:
                        name+='o'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_p:
                        name+='p'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_a:
                        name+='a'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_s:
                        name+='s'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_d:
                        name+='d'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_f:
                        name+='f'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_g:
                        name+='g'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_h:
                        name+='h'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_j:
                        name+='j'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_k:
                        name+='k'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_l:
                        name+='l'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_y:
                        name+='z'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x:
                        name+='x'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_c:
                        name+='c'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_v:
                        name+='v'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_b:
                        name+='b'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_n:
                        name+='n'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_m:
                        name+='m'
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        name+=' '

            
                
        prozor_igre.fill(white)
        prozor_igre.blit(pozadina,(0,0))
        
        display_text('GAME OVER', 100, grey, 100)

        if high_score_beaten(score):
            display_text('new high score: '+str(score), 60, black, 350)
            prozor_igre.blit(mc_happy,(575,200))
        else:   
            display_text('score: '+str(score), 60, grey, 350)
            prozor_igre.blit(mc_died,(575,200))

        display_text('name: '+name, 60, grey, 450)


        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click, _ , _ =pygame.mouse.get_pressed()

        if 475 < mouse_x < 475+250 and 550 < mouse_y < 550+100:
            button('restart', 70, black, over_button_frame, 600)
            if mouse_click==1:
                play_game=True
                selected=True
        else:
            button('restart', 70, grey, button_frame, 600)

        if 475 < mouse_x < 475+250 and 750 < mouse_y < 750+100:
            button('main menu', 45, black, over_button_frame, 800)
            if mouse_click==1:
                play_game=False
                selected=True
        else:
            button('main menu', 45, grey, button_frame, 800)

        pygame.display.update()
        clock.tick(15)
    
    scoreboard_dat(name, score)

    return play_game, exit_game