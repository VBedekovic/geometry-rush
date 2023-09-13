import pygame
from classes.util import prozor_igre, pokupljeno_zvuk, slika

coffee_sprite=pygame.image.load('sprites/powerup/coffee.png')
shotgun_sprite=pygame.image.load('sprites/powerup/shotgun.png')
machinegun_sprite=pygame.image.load('sprites/powerup/machine gun.png')
krug_sprite=pygame.image.load('sprites/powerup/krug.png')
ghost_plus_sprite=pygame.image.load('sprites/powerup/ghost plus.png')
nuke_gumica_sprite=pygame.image.load('sprites/powerup/nuke gumica.png')
star_sprite=pygame.image.load('sprites/powerup/super star.png')
class Powerup:
    def __init__(self, x, y, tip):
        self.x=x
        self.y=y
        self.tip=tip
        _, _, self.width, self.height=slika.get_rect()
        self.brisanje=False
        self.timer=60*10 #sec

    def draw(self):
        if self.timer>60*2 or (110>=self.timer and self.timer>=100) or (90>=self.timer and self.timer>=80) or (70>=self.timer and self.timer>=60) or (50>=self.timer and self.timer>=40) or (30>=self.timer and self.timer>=20) or (10>=self.timer and self.timer>=0):
            if self.tip=='coffee':
                prozor_igre.blit(coffee_sprite, (self.x, self.y))
            if self.tip=='shotgun':
                prozor_igre.blit(shotgun_sprite, (self.x, self.y))
            if self.tip=='machine gun':
                prozor_igre.blit(machinegun_sprite, (self.x, self.y))
            if self.tip=='krug':
                prozor_igre.blit(krug_sprite, (self.x, self.y))
            if self.tip=='extra ghost time':
                prozor_igre.blit(ghost_plus_sprite, (self.x, self.y))
            if self.tip=='nuke gumica':
                prozor_igre.blit(nuke_gumica_sprite, (self.x, self.y))
            if self.tip=='super star':
                prozor_igre.blit(star_sprite, (self.x, self.y))
        

    def collid_with_mc(self, x, mc_width, y, mc_height):
        if self.x > x+mc_width or self.x+self.width < x or self.y > y+mc_height or self.y+self.height < y:
            return False
        return True

    def collected(self, x, mc_width, y, mc_height):
        if self.collid_with_mc(x, mc_width, y, mc_height):
            self.brisanje=True
            if self.tip!='nuke gumica':
                pygame.mixer.Sound.play(pokupljeno_zvuk)
            return self.tip
        return None

    def status(self):
        self.timer-=1
        if self.timer==0:
            self.brisanje=True
