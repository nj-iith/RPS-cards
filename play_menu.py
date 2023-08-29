
import pygame
import ip_input
import button
import network
import lobby
import player
import error_menu
p=[player.Player("player 1"),player.Player("player 2"),player.Player("player 3"),player.Player("player 4"),player.Player("player 5"),player.Player("player 6")]
data=None
net=network.Network()
init=network.client_data(network.INIT)


font = pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 75)
bg=(50,140,150)
create_button=button.Button("create",(100,190,200))
join_button=button.Button("join",(100,190,200))
exit_button=button.Button("back",(100,190,200))
black=(0,40,50)
nameF=open("bin/pname.bin",'r')
name=nameF.readline()
nameF.close()
def Play_menu(window):

    data=None
    create_button.x=window.get_width()//2-create_button.width_solved//2
    create_button.y=window.get_height()//2 - create_button.height
    join_button.x=window.get_width()//2-join_button.width_solved//2
    join_button.y=window.get_height()//2 + int(0.3*join_button.height)
    exit_button.x=window.get_width()//2 -exit_button.width_solved//2
    exit_button.y=window.get_height()/2 +int(1.6*exit_button.height)
   
    running=True
    while running:
        nameF=open("bin/pname.bin",'r')
        name=nameF.readline()
        nameF.close()
        ID=-1
        pygame.display.update()
        window.fill(bg)
        create_button.check(pygame.mouse.get_pos())
        create_button.draw(window)
        join_button.check((pygame.mouse.get_pos()))
        join_button.draw(window)
        exit_button.check(pygame.mouse.get_pos())
        exit_button.draw(window)

        if data!=None:
            if data.type==network.GAME_WINDOW :
                if data.window=="lobby":
                    p=list([player.Player(name)])
                    lobby.Lobby(window,net,data.id,p)
                    running=False
                elif data.window=="error" :
                    data=None
                    error_menu.Error_menu(window,"Can't find game :(    Try creating one ;)")
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                if create_button.hover:
                    init.host=True
                    init.name=name
                    net.connect()
                    net.send("not")
                    data=net.send(init)
                    print("hereeee")
                elif join_button.hover:
                    Done=False
                    while not Done:
                        gameid_txt=ip_input.IP_INPUT(window,"Enter game ID:","Next")
                        if gameid_txt==None:
                            Done=True
                        else:
                            try:
                                ID=int(gameid_txt)
                                init.host=False
                                init.name=name
                                init.id=ID
                                net.connect()
                                net.send("not")
                                data=net.send(init)
                                Done=True
                            except:
                                error_menu.Error_menu(window,"Game ID should be a number")
                    
                elif exit_button.hover:
                    running=False
