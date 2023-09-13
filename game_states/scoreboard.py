import pygame
from util.window import prozor_igre, clock
from util.display import white, grey, black, \
                            button_frame, over_button_frame, \
                            display_text, multiline_text, button
from util.loaded_files import pozadina

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
