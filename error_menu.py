import pygame
import button
font=pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 75)
bg=(255,150,150)
bg2=(150,255,150)
t_c=(0,0,0)

def Error_menu(window,message):
    butt=button.Button("OK",(100,60,60))
    butt.x=window.get_width()//2 -butt.width//2
    butt.y=window.get_height()//2 -butt.height//2
    text=font.render(message,True,t_c)
    running=True
    t_x=window.get_width()//2 -text.get_width()//2
    t_y=window.get_height()//2 -text.get_height()//2-butt.height
    while running:
        pygame.display.update()
        window.fill(bg)
        window.blit(text,(t_x,t_y))
        butt.draw(window)
        butt.check(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and butt.hover :
                running=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running=False
def Error_menu_green(window,message):
    butt=button.Button("OK",(60,100,60))
    butt.x=window.get_width()//2 -butt.width//2
    butt.y=window.get_height()//2 -butt.height//2
    text=font.render(message,True,t_c)
    running=True
    t_x=window.get_width()//2 -text.get_width()//2
    t_y=window.get_height()//2 -text.get_height()//2-butt.height
    while running:
        pygame.display.update()
        window.fill(bg2)
        window.blit(text,(t_x,t_y))
        butt.draw(window)
        butt.check(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and butt.hover :
                running=False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                running=False