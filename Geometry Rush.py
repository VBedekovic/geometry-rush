import pygame, random, ctypes

ctypes.windll.user32.SetProcessDPIAware()


pygame.init()

display_width=1200          #in util
display_height=1000         #in util

#boje
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
grey=(128,128,128)
crimson=(220,20,60)


######prozor
from classes.util import prozor_igre
#prozor_igre=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Geometry Rush')
game_icon=pygame.image.load('images/gameIcon.png')
pygame.display.set_icon(game_icon)
pozadina=pygame.image.load('images/pozadina.jpg')
pozadina_igre_load_1=pygame.image.load('images/pozadina granica 1.jpg')
pozadina_igre_load_2=pygame.image.load('images/pozadina granica 2.jpg')
pozadina_igre=pygame.image.load('images/pozadina granica final.jpg')
pozadina=pozadina.convert_alpha()
pozadina_igre_load_1=pozadina_igre_load_1.convert_alpha()
pozadina_igre_load_2=pozadina_igre_load_2.convert_alpha()
pozadina_igre=pozadina_igre.convert_alpha()
transparent=pygame.image.load('images/transparent.png')
transparent.set_alpha(100)

clock=pygame.time.Clock()

#izračuni   #in util
def vel_kut45(vel):
    br=(vel*(2**(1/2)))/2
    return br

def vel_kut_pol45(vel):
    a=vel*0.92388   #cos(45/2)
    b=vel*0.38627   #sin(45/2)   
    return a, b

#tekst
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
        
    
#button
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

def ghost_vrijeme(t):
    sekunde=t//60
    font = pygame.font.SysFont('Bauhaus 93',35)
    if sekunde>3:
        text = font.render('ghost-time left: {:02d}s'.format(sekunde), True, black)
    elif t!=0:
        text = font.render('ghost-time left: {:02d}s'.format(sekunde), True, crimson)
    else:
        text = font.render('ghost-time left: none'.format(sekunde), True, crimson)
    text_rect=text.get_rect()
    text_rect.center=((display_width/2), 975)
    
    prozor_igre.blit(text, text_rect)
        

######score
def enemies_erased(count):
    font = pygame.font.SysFont('Bauhaus 93',30)
    text = font.render('Erased enemies: '+str(count), True, black)
    prozor_igre.blit(text, (0,0))

        
def scoreboard_dat(ime, score):
    with open('scoreboard.txt', 'r') as dat:
        redovi=dat.readlines()

    if len(redovi)!=0:
        for i in range(len(redovi)):
            redovi[i]=redovi[i][5:]

    redovi.append('{:12s}{}\n'.format(ime, score))

    redovi.sort(key=lambda x: int(x[12:-1]), reverse=True)

    for i in range(len(redovi)):
        redovi[i]='{:>4} '.format(str(i+1)+'.')+redovi[i]

    with open('scoreboard.txt', 'w') as dat:
        dat.writelines(redovi)

def high_score_beaten(score):
    with open('scoreboard.txt', 'r') as dat:
        broj=dat.readline()

    if broj!='':
        broj=int(broj[17:-1])

    if broj=='':
        return True
        
    if score > broj:
        return True
    
    return False
    

#####timer
def sat(t):
    minute=t//60
    sekunde=t%60
    font = pygame.font.SysFont('Bauhaus 93',30)
    text = font.render('{:02d}:{:02d}'.format(minute, sekunde), True, black)
    prozor_igre.blit(text, (1120,0))


#####zvuk
pygame.mixer.music.load('music/Slip.wav')
pygame.mixer.music.set_volume(0.1)
marker_zvuk=pygame.mixer.Sound('sound/drawing_on_paper_with_marker.wav')
gumica_zvuk=pygame.mixer.Sound('sound/eraser.wav')
pokupljeno_zvuk=pygame.mixer.Sound('sound/pokupljeno.wav')  #in util
hit_zvuk=pygame.mixer.Sound('sound/pogodak.wav')
game_over_zvuk=pygame.mixer.Sound('sound/game over.wav')


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


def game_loop(play_game, exit_game):
    sekunde=0
    sekunda_tick=0
    score=None
    paused=False
    play_again=False
    
    #player
    x=(display_width*0.5)-25
    y=(display_height*0.5)-25
    mc_width=50
    mc_height=50
    #mc_hitbox=(x,y)
    x_pomak=0
    y_pomak=0
    vel=3
    smjer_slike='center'

    #pucanje
    metak_po_s=2
    metak_vel=7
    smjer_x=0
    smjer_y=0
    metak_tick=60/metak_po_s
    meci=[]

    #enemy
    enemy_vel=1.5
    enemy_width=50
    enemy_height=50
    spawn_rate=3                    #promjenjivo
    spawn_tick=60*spawn_rate
    enemies=[]
    erased_enemies=[]
    erased_num=0    #score
    veci_enemy_vel=True

    #powerups
    powerup_dur=8 #sec #boi
    coffee_active=False
    machinegun_timer=60*powerup_dur
    machinegun_active=False
    _timer=60*powerup_dur
    shotgun_active=False
    shotgun_timer=60*powerup_dur
    krug_active=False
    krug_timer=60*powerup_dur
    mega_gumica_active=False
    ghost_active=False
    ghost_timer=60*10 #sec
    activate=set()
    powerups=[]
    luck_num=180

    #odbrojavanje
    otkucaj=0
    pygame.mixer.Sound.play(marker_zvuk)
    while otkucaj<3*60:
        otkucaj+=1
        prozor_igre.fill(white)      #pozadina (mora biti prva)
        if otkucaj >= 0:
            prozor_igre.blit(pozadina,(0,0))
        if otkucaj > 3*60*1/4:
            prozor_igre.blit(pozadina_igre_load_1,(0,0))
        if otkucaj > 3*60*2/4:
            prozor_igre.blit(pozadina_igre_load_2,(0,0))
        if otkucaj > 3*60*3/4:
            prozor_igre.blit(pozadina_igre,(0,0))
        
        multiline_text(['w a s d - pomicanje',
                        'strjelice - pucanje',
                        'space - ghost mode'], 350, (display_height*0.25), 60)
        
        mc(x, y, smjer_slike)
        
        pygame.display.update()
        clock.tick(60) #fps
        
    pygame.mixer.music.play(-1)
    
    #mainloop
    #play_game=True
    while play_game:
        #input igrača  
        for event in pygame.event.get():
            #izlaz
            if event.type==pygame.QUIT:
                play_game=False
                play_again=False
                exit_game=True

            #mc kretanje
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    x_pomak=-1
                    smjer_slike='left'
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_a and x_pomak!=1:
                    x_pomak=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    x_pomak=1
                    smjer_slike='right'
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_d and x_pomak!=-1:
                    x_pomak=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    y_pomak=-1
                    smjer_slike='up'
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_w and y_pomak!=1:
                    y_pomak=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    y_pomak=1
                    smjer_slike='down'
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_s and y_pomak!=-1:
                    y_pomak=0

            #mc pucanje
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    smjer_x=-1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT and smjer_x!=1:
                    smjer_x=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    smjer_x=1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT and smjer_x!=-1:
                    smjer_x=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    smjer_y=-1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_UP and smjer_y!=1:
                    smjer_y=0
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_DOWN:
                    smjer_y=1
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_DOWN and smjer_y!=-1:
                    smjer_y=0

            #ghost power-up
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    ghost_active=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    ghost_active=False

            #esc
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    paused=True
                    
                  
        #granice za mc       
        if x > display_width-50-mc_width and x_pomak==1:
            x_pomak=0
        if x < 50 and x_pomak==-1:
            x_pomak=0
        if y > display_height-50-mc_height and y_pomak==1:
            y_pomak=0
        if y < 50 and y_pomak==-1:
            y_pomak=0


        #enemy spawn
        if spawn_tick==60*spawn_rate:
            spawn_point=random.randint(1,24)
            #x gore #zadnji x --> zadnji x + 50 + 170 (=+220)
            if spawn_point==1:
                enemy_x=25
                enemy_y=-100
            if spawn_point==2:
                enemy_x=245
                enemy_y=-100
            if spawn_point==3:
                enemy_x=465
                enemy_y=-100
            if spawn_point==4:
                enemy_x=685
                enemy_y=-100
            if spawn_point==5:
                enemy_x=905
                enemy_y=-100
            if spawn_point==6:
                enemy_x=1125
                enemy_y=-100
            #x dolje
            if spawn_point==18:
                enemy_x=25
                enemy_y=1050
            if spawn_point==17:
                enemy_x=245
                enemy_y=1050
            if spawn_point==16:
                enemy_x=465
                enemy_y=1050
            if spawn_point==15:
                enemy_x=685
                enemy_y=1050
            if spawn_point==14:
                enemy_x=905
                enemy_y=1050
            if spawn_point==13:
                enemy_x=1125
                enemy_y=1050
            #y desno  #zadnji y --> zadnji y + 50 + 130 (=+180)
            if spawn_point==7:
                enemy_x=1250
                enemy_y=25
            if spawn_point==8:
                enemy_x=1250
                enemy_y=205
            if spawn_point==9:
                enemy_x=1250
                enemy_y=385
            if spawn_point==10:
                enemy_x=1250
                enemy_y=565
            if spawn_point==11:
                enemy_x=1250
                enemy_y=745
            if spawn_point==12:
                enemy_x=1250
                enemy_y=925
            #y lijevo
            if spawn_point==24:
                enemy_x=-100
                enemy_y=25
            if spawn_point==23:
                enemy_x=-100
                enemy_y=205
            if spawn_point==22:
                enemy_x=-100
                enemy_y=385
            if spawn_point==21:
                enemy_x=-100
                enemy_y=565
            if spawn_point==20:
                enemy_x=-100
                enemy_y=745
            if spawn_point==19:
                enemy_x=-100
                enemy_y=925
            
            enemies.append(Enemy(enemy_x, enemy_y, enemy_vel))
            spawn_tick=60*spawn_rate
        spawn_tick-=1
        if spawn_tick==0:
            spawn_tick=60*spawn_rate
                
        #powerups
        if coffee_active and coffee_timer!=0:
            vel=5
            coffee_timer-=1
        else:
            vel=3
            coffee_active=False

        if machinegun_active and machinegun_timer!=0:
            metak_po_s=6
            machinegun_timer-=1
        else:
            metak_po_s=2
            machinegun_active=False

        if shotgun_active and shotgun_timer!=0:
            shotgun_timer-=1
        else:
            shotgun_active=False

        if krug_active and krug_timer!=0:
            krug_timer-=1
        else:
            krug_active=False

        if ghost_active:
            if coffee_active:
                vel=7
            else:
                vel=4.5

        #metak
        if not ghost_active:                      #kada nedodirljiv, zabrani pucanje
            if smjer_x!=0 or smjer_y!=0:
                if metak_tick==60/metak_po_s:
                    if krug_active:
                        meci.append(Metak(x+15, y+15, 1, 0, metak_vel, False))
                        meci.append(Metak(x+15, y+15, -1, 0, metak_vel, False))
                        meci.append(Metak(x+15, y+15, 0, 1, metak_vel, False))
                        meci.append(Metak(x+15, y+15, 0, -1, metak_vel, False))
                        meci.append(Metak(x+15, y+15, 1, 1, metak_vel, False))
                        meci.append(Metak(x+15, y+15, -1, -1, metak_vel, False))
                        meci.append(Metak(x+15, y+15, 1, -1, metak_vel, False))
                        meci.append(Metak(x+15, y+15, -1, 1, metak_vel, False))
                        if shotgun_active:
                            meci.append(Metak(x+15, y+15, 1, 0, metak_vel, True, 'right'))
                            meci.append(Metak(x+15, y+15, -1, 0, metak_vel, True, 'right'))
                            meci.append(Metak(x+15, y+15, 0, 1, metak_vel, True, 'right'))
                            meci.append(Metak(x+15, y+15, 0, -1, metak_vel, True, 'right'))
                            meci.append(Metak(x+15, y+15, 1, 0, metak_vel, True, 'left'))
                            meci.append(Metak(x+15, y+15, -1, 0, metak_vel, True, 'left'))
                            meci.append(Metak(x+15, y+15, 0, 1, metak_vel, True, 'left'))
                            meci.append(Metak(x+15, y+15, 0, -1, metak_vel, True, 'left'))
                            
                    else:     
                        meci.append(Metak(x+15, y+15, smjer_x, smjer_y, metak_vel, False))
                        if shotgun_active:
                            if smjer_x==1 and smjer_y==1:
                                meci.append(Metak(x+15, y+15, 0, 1, metak_vel, True, 'right'))
                                meci.append(Metak(x+15, y+15, 1, 0, metak_vel, True, 'left'))
                            if smjer_x==1 and smjer_y==0:
                                meci.append(Metak(x+15, y+15, 1, 0, metak_vel, True, 'left'))
                                meci.append(Metak(x+15, y+15, 1, 0, metak_vel, True, 'right'))
                            if smjer_x==1 and smjer_y==-1:
                                meci.append(Metak(x+15, y+15, 1, 0, metak_vel, True, 'right'))
                                meci.append(Metak(x+15, y+15, 0, -1, metak_vel, True, 'left'))
                            if smjer_x==0 and smjer_y==-1:
                                meci.append(Metak(x+15, y+15, 0, -1, metak_vel, True, 'left'))
                                meci.append(Metak(x+15, y+15, 0, -1, metak_vel, True, 'right'))
                            if smjer_x==-1 and smjer_y==-1:
                                meci.append(Metak(x+15, y+15, 0, -1, metak_vel, True, 'right'))
                                meci.append(Metak(x+15, y+15, -1, 0, metak_vel, True, 'left'))
                            if smjer_x==-1 and smjer_y==0:
                                meci.append(Metak(x+15, y+15, -1, 0, metak_vel, True, 'left'))
                                meci.append(Metak(x+15, y+15, -1, 0, metak_vel, True, 'right'))
                            if smjer_x==-1 and smjer_y==1:
                                meci.append(Metak(x+15, y+15, -1, 0, metak_vel, True, 'right'))
                                meci.append(Metak(x+15, y+15, 0, 1, metak_vel, True, 'left'))
                            if smjer_x==0 and smjer_y==1:
                                meci.append(Metak(x+15, y+15, 0, 1, metak_vel, True, 'left'))
                                meci.append(Metak(x+15, y+15, 0, 1, metak_vel, True, 'right'))
                                
                    metak_tick-=1
                
                
        if metak_tick!=60/metak_po_s:
            metak_tick-=1
        if metak_tick==0:
            metak_tick=60/metak_po_s


        #mc kretanje za vel
        if x_pomak==0 or y_pomak==0:  
            x+=x_pomak*vel
            y+=y_pomak*vel
        else:
            vel_xy=vel_kut45(vel)  #da vektor vel ostane isti
            x+=x_pomak*vel_xy
            y+=y_pomak*vel_xy

        #crtanje na ekran i provjere
        prozor_igre.fill(white)      #pozadina (mora biti prva)
        prozor_igre.blit(pozadina_igre,(0,0))
        

        new_powerups=[]
        for powerup in powerups:
            powerup.draw()
            powerup.status()
            power=powerup.collected(x, mc_width, y, mc_height )
            if power=='super star':
                activate.add('shotgun')
                activate.add('machine gun')
                activate.add('krug')
            else:   
                activate.add(power)
            if not powerup.brisanje:
                new_powerups.append(powerup)
        powerups=new_powerups


        if 'coffee' in activate:
            activate.remove('coffee')
            coffee_active=True
            coffee_timer=60*powerup_dur
        if 'shotgun' in activate:
            activate.remove('shotgun')
            shotgun_active=True
            shotgun_timer=60*powerup_dur
        if 'machine gun' in activate:
            activate.remove('machine gun')
            machinegun_active=True
            machinegun_timer=60*powerup_dur
        if 'krug' in activate:
            activate.remove('krug')
            krug_active=True
            krug_timer=60*powerup_dur
        #super star --> sve iznad (osim kave)

        if 'extra ghost time' in activate:
            activate.remove('extra ghost time')
            ghost_timer+=60*4 #sec
            
        if 'nuke gumica' in activate:
            pygame.mixer.Sound.play(gumica_zvuk)
            num=len(enemies)
            if num>10:              #ograničeno na 10 bodova max
                num=10
            erased_num+=num
            activate.remove('nuke gumica')
            for enemy in enemies:
                erased_enemies.append(enemy)
            enemies=[]
            
            
        new_meci=[]
        for metak in meci:
            metak.shoot()
            metak.status()
            for enemy in enemies:
                if metak.pogodak(enemy):
                    pygame.mixer.Sound.play(hit_zvuk)
                    enemies.remove(enemy)
                    erased_enemies.append(enemy)
                    erased_num+=1
                    metak.brisanje=True
                    break
            if not metak.brisanje:
                new_meci.append(metak)
        meci=new_meci
                                    

        sekunda_tick+=1
        if sekunda_tick==60:
            sekunde+=1
            sekunda_tick=0
        sat(sekunde)                #timer
        enemies_erased(erased_num)  #score
        

        if ghost_active and ghost_timer!=0:
            ghost_timer-=1
        if ghost_timer==0:
            ghost_active=False
        ghost_vrijeme(ghost_timer)


        if sekunde%5 == 0 and  sekunda_tick == 30 and spawn_rate > 0.4 and sekunde!=0:
            spawn_rate-=0.2
            #luck_num+=2
            spawn_rate=float('{:.2f}'.format(spawn_rate))
            

        if erased_num%5==0 and enemy_vel < 2.5 and erased_num!=0 and veci_enemy_vel:
            enemy_vel+=0.05
            enemy_vel=float('{:.2f}'.format(enemy_vel))
            veci_enemy_vel=False
        elif erased_num%5!=0:
            veci_enemy_vel=True

           

        for enemy in enemies:
            if enemy.move_type==1:
                enemy.movement_a(x,y)
            if enemy.move_type==2:
                enemy.movement_b(x,y)
            if enemy.move_type==3:
                enemy.movement_c(x,y)
            if enemy.check_collision_with_other_enemy(enemies):
                enemy.avoid_other_enemy_movement(enemies, x, y)
            enemy.backup=(enemy.x, enemy.y)
            enemy.draw()

        new_erased_enemies=[]
        for enemy in erased_enemies:
            erase_timer=enemy.erased()
            if erase_timer!=0:
                new_erased_enemies.append(enemy)
            if erase_timer==0:
                sretan_broj=random.randint(1,luck_num)
                if sretan_broj in [1,100]:
                    tip='super star'
                elif sretan_broj in [2,50,99]:
                    tip='nuke gumica'
                elif sretan_broj in [59,19,41,86]:
                    tip='extra ghost time'
                elif sretan_broj in [3,4,5,6]:
                    tip='krug'
                elif sretan_broj in [98,97,96,95,18]:
                    tip='machine gun'
                elif sretan_broj in [51,52,49,48,47,53]:
                    tip='shotgun'
                elif sretan_broj in [8,9,60,30,24,55,69]:
                    tip='coffee'
                else:
                    tip=None

                if tip!=None:
                    powerups.append(Powerup(enemy.x, enemy.y, tip))
            
        erased_enemies=new_erased_enemies
                                    
                
        if x_pomak==0 and y_pomak==0:
            smjer_slike='center'
        mc(x, y, smjer_slike, ghost_active)

        #enemy dotaknul mc (game over)
        if not ghost_active:
            for enemy in enemies:
                if not(x > enemy.x+enemy.width or x+mc_width < enemy.x or
                       y > enemy.y+enemy.height or y+mc_height < enemy.y):
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(game_over_zvuk)
                    play_game=False
                    play_again=True
                    score=erased_num*sekunde
                    
                    prozor_igre.blit(mc_erased,(x,y))
                    pygame.display.update()
                    t=30*2
                    while t > 0:
                        t-=1
                        clock.tick(30)
                
        if paused:
            pygame.mixer.music.pause()
            prozor_igre.blit(transparent, (0,0))
            pygame.image.save(prozor_igre, 'pause background.jpg')
            score=erased_num*sekunde
            play_game, exit_game, paused=pause_game_loop(play_game, exit_game, score)
        
            
        pygame.display.update()
        clock.tick(60) #fps
        
    pygame.mixer.music.stop()
    
    return play_game, play_again, exit_game, score

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
