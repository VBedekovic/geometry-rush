import pygame

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



#zvuk
pokupljeno_zvuk=pygame.mixer.Sound('sound/pokupljeno.wav')



slika=pygame.image.load('sprites/mc/mc_slika.png')
