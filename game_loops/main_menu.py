import pygame
from util.window import prozor_igre, clock
from util.display import white, black, grey, crimson, title, button, over_button_frame, button_frame, over_button_frame_red
from util.loaded_files import pozadina


def main_menu_loop(play_game, go_scoreboard, go_info, exit_game):
    in_loop=True
    mouse_wait_time=30*0.3
    mouse_click=0
    while in_loop:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                in_loop=False
                exit_game=True



            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    play_game=True
                    in_loop=False


        #crtanje na ekran i interakcija
        prozor_igre.fill(white)
        prozor_igre.blit(pozadina,(0,0))
        
        title('GEOMETRY RUSH')

        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_wait_time!=0:
            mouse_wait_time-=1
        else:
            mouse_click, _ , _ =pygame.mouse.get_pressed()  # dobije se tuple (0,0,0) --> (lijevi klik, srednji klik, desni klik)
                                                        # pritiskom 0 prelazi u 1
        # x=475 | y=250,450,650,850 | w=250 | h=100
        if 475 < mouse_x < 475+250 and 250 < mouse_y < 250+100:
            button('start', 70, black, over_button_frame, 300)
            if mouse_click==1:
                play_game=True
                in_loop=False
        else:
            button('start', 70, grey, button_frame, 300)
            
        if 475 < mouse_x < 475+250 and 450 < mouse_y < 450+100:         
            button('score', 70, black, over_button_frame, 500)
            if mouse_click==1:
                go_scoreboard=True
                in_loop=False
        else:
            button('score', 70, grey, button_frame, 500)

        if 475 < mouse_x < 475+250 and 650 < mouse_y < 650+100:         
            button('info', 70, black, over_button_frame, 700)
            if mouse_click==1:
                go_info=True
                in_loop=False
        else:
            button('info', 70, grey, button_frame, 700)

        if 475 < mouse_x < 475+250 and 850 < mouse_y < 850+100:
            button('exit', 70, crimson, over_button_frame_red, 900)
            if mouse_click==1:
                in_loop=False
                exit_game=True
        else:
            button('exit', 70, grey, button_frame, 900)

        pygame.display.update()
        clock.tick(15) #fps
        

    return play_game, go_scoreboard, go_info, exit_game
