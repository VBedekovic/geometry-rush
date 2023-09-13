import pygame, random
from classes.util import prozor_igre, vel_kut45

angry_enemy=pygame.image.load('sprites/enemy/angry_kocka.png')
erased_enemy_1=pygame.image.load('sprites/enemy/sad_kocka.png')
erased_enemy_2=pygame.image.load('sprites/enemy/sad_kocka_bye1.png')
erased_enemy_3=pygame.image.load('sprites/enemy/sad_kocka_bye2.png')
erased_enemy_4=pygame.image.load('sprites/enemy/sad_kocka_bye3.png')
erased_enemy_5=pygame.image.load('sprites/enemy/sad_kocka_sad_bye.png')
erased_enemy_final=pygame.image.load('sprites/enemy/sad_kocka_final_bye.png')
class Enemy:
    br=0
    def __init__(self, x, y, vel):
        self.x=x
        self.y=y
        self.backup=(x,y)
        self.width=50
        self.height=50
        #self.color=color
        self.smjer_x=0
        self.smjer_y=0
        self.vel=vel
        Enemy.br+=1
        self.id=Enemy.br
        self.upit, self.upit_2=bool(random.getrandbits(1)), bool(random.getrandbits(1))
        self.timer=60*2
        self.erase_timer=60*1.5
        self.move_type=random.randint(1,3)
        
        
        
    def movement_a(self, x, y):
        #x
        if self.x > x:
            self.smjer_x = -1
        elif self.x < x:
            self.smjer_x = 1
        elif self.x == x:
            self.smjer_x = 0
        #y
        if self.y < y:
            self.smjer_y = 1
        elif self.y > y:
            self.smjer_y = -1
        elif self.y == y:
            self.smjer_y = 0
        #izračun
        if self.smjer_x==0 or self.smjer_y==0:
            self.x+=self.smjer_x*self.vel
            self.y+=self.smjer_y*self.vel
        else:
            vel_xy=vel_kut45(self.vel)
            self.x+=self.smjer_x*vel_xy
            self.y+=self.smjer_y*vel_xy

    def movement_b(self, x, y):
        x-=45
        y-=45
        #x
        if self.x > x:
            self.smjer_x = -1
        elif self.x < x:
            self.smjer_x = 1
        elif self.x == x:
            self.smjer_x = 0
        #y
        if self.y < y:
            self.smjer_y = 1
        elif self.y > y:
            self.smjer_y = -1
        elif self.y == y:
            self.smjer_y = 0
        #izračun
        if self.smjer_x==0 or self.smjer_y==0:
            self.x+=self.smjer_x*self.vel
            self.y+=self.smjer_y*self.vel
        else:
            vel_xy=vel_kut45(self.vel)
            self.x+=self.smjer_x*vel_xy
            self.y+=self.smjer_y*vel_xy

    def movement_c(self, x, y):
        x+=45
        y+=45
        #x
        if self.x > x:
            self.smjer_x = -1
        elif self.x < x:
            self.smjer_x = 1
        elif self.x == x:
            self.smjer_x = 0
        #y
        if self.y < y:
            self.smjer_y = 1
        elif self.y > y:
            self.smjer_y = -1
        elif self.y == y:
            self.smjer_y = 0
        #izračun
        if self.smjer_x==0 or self.smjer_y==0:
            self.x+=self.smjer_x*self.vel
            self.y+=self.smjer_y*self.vel
        else:
            vel_xy=vel_kut45(self.vel)
            self.x+=self.smjer_x*vel_xy
            self.y+=self.smjer_y*vel_xy
        

    def collision_with_other_enemy(self, other):
        if self.x > other.x+other.width or self.x+self.width < other.x or self.y > other.y+other.height or self.y+self.height < other.y:
            return False
        return True


    def check_collision_with_other_enemy(self, enemies):
        for other_enemy in enemies:
            if self.id != other_enemy.id:
                if self.collision_with_other_enemy(other_enemy):
                    return True
        return False
                
    def avoid_movement(self):
        #izračun
        if self.smjer_x==0 or self.smjer_y==0:
            self.x+=self.smjer_x*self.vel
            self.y+=self.smjer_y*self.vel
        else:
            vel_xy=vel_kut45(self.vel)
            self.x+=self.smjer_x*vel_xy
            self.y+=self.smjer_y*vel_xy
        

    def avoid_other_enemy_movement(self, other_enemies, x, y):
        if self.timer==60*1.5:
            self.upit=bool(random.getrandbits(1))
            self.upit_2=bool(random.getrandbits(1))
        self.timer-=1
        if self.timer==0:
            self.timer=60*1.5
        #upit=bool(random.getrandbits(1))
        if self.upit:
            self.smjer_x=0
            #upit_2=bool(random.getrandbits(1))
            if self.upit_2:
                self.smjer_y=1
            else:
                self.smjer_y=-1
            self.avoid_movement()
            sudar=self.check_collision_with_other_enemy(other_enemies)
            if sudar:
                self.x, self.y= self.backup
                if not self.upit_2:
                    self.smjer_y=1
                else:
                    self.smjer_y=-1
                self.avoid_movement()
                sudar=self.check_collision_with_other_enemy(other_enemies)
                if sudar:
                    self.x, self.y= self.backup
        else:
            self.smjer_y=0
            #upit_2=bool(random.getrandbits(1))
            if self.upit_2:
                self.smjer_x=1
            else:
                self.smjer_x=-1
            self.avoid_movement()
            sudar=self.check_collision_with_other_enemy(other_enemies)
            if sudar:
                self.x, self.y= self.backup
                if self.upit_2:
                    self.smjer_x=1
                else:
                    self.smjer_x=-1
                self.avoid_movement()
                sudar=self.check_collision_with_other_enemy(other_enemies)
                if sudar:
                    self.x, self.y= self.backup

        if sudar:
            if not self.upit:
                self.smjer_x=0
                #upit_2=bool(random.getrandbits(1))
                if self.upit_2:
                    self.smjer_y=1
                else:
                    self.smjer_y=-1
                self.avoid_movement()
                sudar=self.check_collision_with_other_enemy(other_enemies)
                if sudar:
                    self.x, self.y= self.backup
                    if not self.upit_2:
                        self.smjer_y=1
                    else:
                        self.smjer_y=-1
                    self.avoid_movement()
                    sudar=self.check_collision_with_other_enemy(other_enemies)
                    if sudar:
                        self.x, self.y= self.backup
            else:
                self.smjer_y=0
                #upit_2=bool(random.getrandbits(1))
                if self.upit_2:
                    self.smjer_x=1
                else:
                    self.smjer_x=-1
                self.avoid_movement()
                sudar=self.check_collision_with_other_enemy(other_enemies)
                if sudar:
                    self.x, self.y= self.backup
                    if self.upit_2:
                        self.smjer_x=1
                    else:
                        self.smjer_x=-1
                    self.avoid_movement()
                    sudar=self.check_collision_with_other_enemy(other_enemies)
                    if sudar:
                        self.x, self.y= self.backup


        
        #self.x, self.y=self.backup
                        #stajanje na mjestu


    def draw(self):
        #pygame.draw.rect(prozor_igre, self.color, [self.x, self.y, self.width, self.height])
        prozor_igre.blit(angry_enemy, (self.x, self.y))

    def erased(self):
        if self.erase_timer > (5/6)*60*2:
            prozor_igre.blit(erased_enemy_1, (self.x, self.y))
        elif self.erase_timer > (4/6)*60*2:
            prozor_igre.blit(erased_enemy_2, (self.x, self.y))
        elif self.erase_timer > (3/6)*60*2:
            prozor_igre.blit(erased_enemy_3, (self.x, self.y))
        elif self.erase_timer > (2/6)*60*2:
            prozor_igre.blit(erased_enemy_4, (self.x, self.y))
        elif self.erase_timer > (1/6)*60*2:
            prozor_igre.blit(erased_enemy_5, (self.x, self.y))
        elif self.erase_timer > 0:
            prozor_igre.blit(erased_enemy_final, (self.x, self.y))
            
        self.erase_timer-=1
        return self.erase_timer