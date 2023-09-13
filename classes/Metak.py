import pygame
from util.trigonometry import vel_kut45, vel_kut_pol45
from util.window import prozor_igre, display_width, display_height

slika_metak=pygame.image.load('sprites/mc/gumica.png')
class Metak:
    def __init__(self, x, y, smjer_x, smjer_y, vel, is_shotgun, side=None):
        self.x=x
        self.y=y
        self.width=20     ##
        self.height=20    ##
        self.smjer_x=smjer_x
        self.smjer_y=smjer_y
        self.vel=vel
        self.brisanje=False
        self.shotgun=is_shotgun
        self.side=side
        

    def shoot(self):        
        prozor_igre.blit(slika_metak,(self.x, self.y))
        
        if not self.shotgun:
            if self.smjer_x==0 or self.smjer_y==0:
                self.x+=self.smjer_x*self.vel
                self.y+=self.smjer_y*self.vel
            else:
                vel_xy=vel_kut45(self.vel)
                self.x+=self.smjer_x*vel_xy
                self.y+=self.smjer_y*vel_xy
        else:
            veca_str, manja_str=vel_kut_pol45(self.vel)
            
            #+y right
            if self.smjer_y==1 and self.side=='right':
                self.x+=1*manja_str
                self.y+=1*veca_str
            #+x left
            if self.smjer_x==1 and self.side=='left':
                self.x+=1*veca_str
                self.y+=1*manja_str
            #+x right
            if self.smjer_x==1 and self.side=='right':
                self.x+=1*veca_str
                self.y+=-1*manja_str
            #-y left
            if self.smjer_y==-1 and self.side=='left':
                self.x+=1*manja_str
                self.y+=-1*veca_str
            #-y right
            if self.smjer_y==-1 and self.side=='right':
                self.x+=-1*manja_str
                self.y+=-1*veca_str
            #-x left
            if self.smjer_x==-1 and self.side=='left':
                self.x+=-1*veca_str
                self.y+=-1*manja_str
            #-x right
            if self.smjer_x==-1 and self.side=='right':
                self.x+=-1*veca_str
                self.y+=1*manja_str
            #+y left
            if self.smjer_y==1 and self.side=='left':
                self.x+=-1*manja_str
                self.y+=1*veca_str

    def status(self):
        if self.x<50 or self.x>display_width-50 or self.y<50 or self.y>display_height-50:
            self.brisanje=True

    def pogodak(self, enemy):
        if self.x > enemy.x+enemy.width or self.x < enemy.x or self.y > enemy.y+enemy.height or self.y+self.height < enemy.y:
            return False
        return True
