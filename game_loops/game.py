import pygame, random
from game_loops.pause import pause_game_loop

from classes.MainCharacter import mc, mc_erased
from classes.Enemy import Enemy
from classes.Metak import Metak
from classes.Powerup import Powerup

from util.window import prozor_igre, display_width, display_height, clock
from util.display import white, \
                            multiline_text, sat, ghost_vrijeme, enemies_erased
from util.trigonometry import vel_kut45
from util.loaded_files import marker_zvuk, \
                                pozadina_igre, \
                                pozadina, \
                                pozadina_igre_load_1, \
                                pozadina_igre_load_2, \
                                transparent, \
                                gumica_zvuk, \
                                hit_zvuk, \
                                game_over_zvuk
                                

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