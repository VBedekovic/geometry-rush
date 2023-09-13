import pygame

#background
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

#sound
pygame.mixer.music.load('music/Slip.wav')
pygame.mixer.music.set_volume(0.1)
marker_zvuk=pygame.mixer.Sound('sound/drawing_on_paper_with_marker.wav')
gumica_zvuk=pygame.mixer.Sound('sound/eraser.wav')
pokupljeno_zvuk=pygame.mixer.Sound('sound/pokupljeno.wav')  #in util
hit_zvuk=pygame.mixer.Sound('sound/pogodak.wav')
game_over_zvuk=pygame.mixer.Sound('sound/game over.wav')


