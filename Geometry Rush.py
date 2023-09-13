import pygame, random, ctypes

ctypes.windll.user32.SetProcessDPIAware()

pygame.init()

pygame.display.set_caption('Geometry Rush')
game_icon=pygame.image.load('images/gameIcon.png')
pygame.display.set_icon(game_icon)

from game_states.main_menu import main_menu_loop
from game_states.game import game_loop
from game_states.play_again import play_again_loop
from game_states.scoreboard import scoreboard_loop
from game_states.info import info_loop   

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
