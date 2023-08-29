import pygame
import error_menu
import main_game
import ip_input
import main_menu
import lobby
import player
import connect_menu
p=[player.Player("player 1"),player.Player("player 2"),player.Player("player 3"),player.Player("player 4"),player.Player("player 5"),player.Player("player 6")]
pygame.init()
clk=pygame.time.Clock()

window=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#window=pygame.display.set_mode((1000, 700))
Icon = pygame.image.load('res/logo.png')
pygame.display.set_icon(Icon)
pygame.display.set_caption('RPS Battle cards')
# window=pygame.display.set_mode([100,100])
# print(ip_input.IP_INPUT(window,"Enter name: ","Next"))
# main_game.Main_game(window)
Sts=connect_menu.Connect_menu(window)
if Sts:
    main_menu.MM(window)
# error_menu.Error_menu(window,"hai")
# lobby.Lobby(window,4545,p)
pygame.quit()
    