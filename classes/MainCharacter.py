#more module than class (for now...)
import pygame
from util.window import prozor_igre


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
    