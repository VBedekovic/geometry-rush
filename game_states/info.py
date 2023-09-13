import pygame
from util.window import prozor_igre, clock
from util.display import white, grey, black, button_frame, over_button_frame, \
                            display_text, multiline_text, button
from util.loaded_files import pozadina
from classes.Powerup import coffee_sprite, krug_sprite, \
                            machinegun_sprite, shotgun_sprite, \
                            nuke_gumica_sprite, star_sprite, \
                            ghost_plus_sprite
from classes.MainCharacter import mc_ghost

def info_loop(go_info, exit_game):
    go_back=False
    while not go_back:

        for event in pygame.event.get():
            #izlaz
            if event.type==pygame.QUIT:
                exit_game=True
                go_back=True
                go_info=False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click, _ , _ =pygame.mouse.get_pressed()
        
        
        prozor_igre.fill(white)
        prozor_igre.blit(pozadina,(0,0))
        
        
        display_text('INFO', 75, grey, 75)

        prozor_igre.blit(mc_ghost, (150,150))
        multiline_text(['GHOST MODE:', '- aktivira se drzanjem', '  tipke space',
                        '- omogucuje prolaz kroz', '  napadace i daje ubrzanje',
                        '- ima ogranicenu upotrebu'], 225, 150, 25)

        prozor_igre.blit(ghost_plus_sprite, (150,375))
        multiline_text(['EXTRA TIME:', '- bacaju napadaci',
                        '- nadoda 4 sekunde','  na ghost mode'], 225, 375, 25)

        prozor_igre.blit(coffee_sprite, (150,550))
        multiline_text(['COFFEE:', '- bacaju napadaci',
                        '- daje veliko ubrzanje'], 225, 550, 25)

        prozor_igre.blit(krug_sprite, (725,150))
        multiline_text(['KRUG:', '- bacaju napadaci',
                        '- omogucuje pucnaje','  u osam',
                        '  smijerova odjednom'], 800, 150, 25)

        prozor_igre.blit(machinegun_sprite, (725,375))
        multiline_text(['MACHINE GUN:', '- bacaju napadaci',
                        '- omogucuje pucnaje','  vise metaka po sekundi'], 800, 375, 25)

        prozor_igre.blit(shotgun_sprite, (725,550))
        multiline_text(['SHOTGUN:', '- bacaju napadaci',
                        '- omogucuje pucanje',
                        '  vise metaka odjednom'], 800,550, 25)

        prozor_igre.blit(nuke_gumica_sprite, (50,725))
        multiline_text(['GUMICA:', '- bacaju napadaci',
                        '- izbrise sve napadace',
                        '  trenutno u igri',
                        '- najviše +10 na score'], 125, 725, 25)

        prozor_igre.blit(star_sprite, (825,725))
        multiline_text(['SUPER STAR:', '- bacaju napadaci',
                        '- shotgun',
                        '  machine gun',
                        '  i krug u jednom'], 900, 725, 25)
        
        
        if 475 < mouse_x < 475+250 and 850 < mouse_y < 850+100:
            button('back', 70, black, over_button_frame, 900)
            if mouse_click==1:
                go_back=True
                go_info=False
        else:
            button('back', 70, grey, button_frame, 900)


        pygame.display.update()
        clock.tick(15)
    
    return go_info, exit_game
