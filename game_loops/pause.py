import pygame

from util.window import prozor_igre, clock
from util.display import white, grey, black, \
                            button_frame, over_button_frame,\
                            display_text, button

def pause_game_loop(play_game, exit_game, score):
    selected=False
    while not selected:
                  
        for event in pygame.event.get():
            #izlaz
            if event.type==pygame.QUIT:
                play_game=False
                exit_game=True
                selected=True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    selected=True

        prozor_igre.fill(white)
        prozor_igre.blit(pygame.image.load('pause background.jpg'),(0,0))

        display_text('PAUSED', 100, black, 300)

        trenutni_score='current score: '+str(score)
        display_text(trenutni_score, 60, black, 400)
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click, _ , _ =pygame.mouse.get_pressed()

        if 475 < mouse_x < 475+250 and 750 < mouse_y < 750+100:
            button('main menu', 45, black, over_button_frame, 800)
            if mouse_click==1:
                #pygame.mixer.Sound.play(click)
                play_game=False
                selected=True
        else:
            button('main menu', 45, grey, button_frame, 800)
        

        pygame.display.update()
        clock.tick(15)
        
    pygame.mixer.music.unpause()
    
    return play_game, exit_game, False
                