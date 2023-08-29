import player
import pygame
import button
import main_game
import network
status=network.client_data(network.STATUS)
status.ready=False
Quit=network.client_data(network.QUIT)
blue=pygame.image.load("res/images/blue.png")
bg=(50,90,100)
pl=[]
id=0
num=0
ready_button=button.Button("Ready",(0,200,100))

def Lobby(window,net,ID,pl):

    left=False
    right=False
    status.ready=False
    ready_button.x=window.get_width()-ready_button.width_solved
    ready_button.y=ready_button.height
    scrolling=False
    scroll_right=False
    scroll_left=False
    scroll_speed=5
    running=True
    cards=[]
    n=len(pl)
    for p in pl:
        cards.append(player.PlayerCard_lobby(p))
    code=button.Button("Game ID: "+str(ID),(22,151,165))
    code.x=window.get_width()//2 -code.width//2
    code.y=code.height
    if len(pl)>0:
        w_max=cards[0].w
        for card in cards:
            if(card.w>w_max):
                w_max=card.w
        if(window.get_width()>(n+1)*w_max+blue.get_width()):
            scrolling=False
            x=window.get_width()//(n+1)
            add=x
            for card in cards:
                card.x=x-(blue.get_width()//2)
                card.y=window.get_height()//2 -card.h//2
                x+=add
        else:
            scrolling=True
            x=w_max
            for card in cards:
                card.x=x
                card.y=window.get_height()//2 -card.h//2
                x+=w_max
    
    while running:
        data=net.send(status)
        if data.type==network.HEADER:
            id=data.my_number
            num=data.number_of_players
            if num<len(pl):
                scrolling=False
                for i in range(len(pl)-num):
                    del pl[-1]
                    del cards[-1]
        elif data.type==network.PLAYER:
            if data.id<len(pl):
                pl[data.id].copy(data.player)
                cards[data.id].refresh(data.player)
            else:
                scrolling=False
                pl.append(player.Player("nj"))
                pl[-1].copy(data.player)
                cards.append(player.PlayerCard_lobby(data.player))
                if cards[-1].w>w_max:
                    w_max=cards[-1].w
            n=len(pl)
            if not scrolling:
                if(window.get_width()>n*w_max+blue.get_width()):
                    scrolling=False
                    x=window.get_width()//(n+1)
                    add=x
                    for card in cards:
                        card.x=x-(blue.get_width()//2)
                        card.y=window.get_height()//2 -card.h//2
                        x+=add
                else:
                    scrolling=True
                    x=w_max
                    for card in cards:
                        card.x=x
                        card.y=window.get_height()//2 -card.h//2
                        x+=w_max
        elif data.type==network.GAME_WINDOW :
            if data.window=="game":
                # status.ready=False
                main_game.Main_game(window,net)
                running=False

        pygame.display.update()
        window.fill(bg)
        code.draw(window)
        if(len(pl)>1):
            ready_button.check(pygame.mouse.get_pos())
            ready_button.draw(window)
        if scrolling:
            if left and cards[-1].x>window.get_width()//2:
                for c in cards:
                    c.x-=5
            if right and cards[0].x<window.get_width()//3:
                for c in cards:
                    c.x+=5
        for card in cards:
            card.draw(window)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running=False
                net.send(Quit)
                net.end()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                if ready_button.hover and len(pl)>1:
                    status.ready=True
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    right=True
                elif event.key==pygame.K_a:
                    left=True
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_d:
                    right=False
                elif event.key==pygame.K_a:
                    left=False
    