
import pygame
import ip_input
import button
import main_game
import play_menu
nameF=open("bin/pname.bin",'r')
name=nameF.readline()
nameF.close()
font = pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 75)
bg=(50,140,150)
playbutton=button.Button("Play",(100,190,200))
cn_button=button.Button("Change Name",(100,190,200))
exit_button=button.Button("Exit",(100,190,200))
black=(0,40,50)
def MM(window):
    playbutton.x=window.get_width()//2-playbutton.width_solved//2
    playbutton.y=window.get_height()//2 - playbutton.height
    cn_button.x=window.get_width()//2-cn_button.width_solved//2
    cn_button.y=window.get_height()//2 + int(0.3*cn_button.height)
    exit_button.x=window.get_width()//2 -exit_button.width_solved//2
    exit_button.y=window.get_height()/2 +int(1.6*exit_button.height)
   
    running=True
    while running:
        nameF=open("bin/pname.bin",'r')
        name=nameF.readline()
        nameF.close()
        text=font.render("player:"+name,True,black)
        pygame.display.update()
        window.fill(bg)
        window.blit(text,(0,0))
        playbutton.check(pygame.mouse.get_pos())
        playbutton.draw(window)
        cn_button.check((pygame.mouse.get_pos()))
        cn_button.draw(window)
        exit_button.check(pygame.mouse.get_pos())
        exit_button.draw(window)
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                if playbutton.hover:
                    play_menu.Play_menu(window)
                elif cn_button.hover:
                    NEW=ip_input.IP_INPUT(window,"Enter name:","Change")
                    if NEW!=None and NEW!="":
                        nameF=open("bin/pname.bin","w")
                        nameF.write(NEW)
                        nameF.close()
                elif exit_button.hover:
                    running=False
