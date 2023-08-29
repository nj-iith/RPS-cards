import pygame
import pyperclip
import button
bg=(50,90,100)
pygame.init()
font = pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 75)
logo=pygame.image.load('res/logo_low_res.png')
white=(205,245,255)
black=(0,40,50)
def IP_INPUT(window,prompt,sub_text):
    running=True
    a=""
    sub_button=button.Button(sub_text,(100,140,150))
    sub_button.x=int(window.get_width()*0.7)
    sub_button.y=int(window.get_height()*0.2)
    back_button=button.Button("back",(100,140,150))
    back_button.x=int(window.get_width()*0.05)
    back_button.y=int(window.get_height()*0.05)
    while running:
        pygame.display.update()
        window.fill(bg)
        text=font.render(prompt+a,True,black)
        x,y =window.get_width()//2-text.get_width()//2,window.get_height()*0.8-text.get_height()//2
        margin=8

        pygame.draw.rect(window, black,[min(x,window.get_width()*0.1)-margin, y-margin, max(text.get_width(),window.get_width()*0.8)+2*margin , text.get_height()+2*margin], 0)
        pygame.draw.circle(window, black,[min(x,window.get_width()*0.1), y+text.get_height()/2], (text.get_height()/2)+margin)
        pygame.draw.circle(window, black,[min(x,window.get_width()*0.1)+max(text.get_width(),window.get_width()*0.8), y+text.get_height()/2], (text.get_height()/2)+margin)


        pygame.draw.rect(window, white,[min(x,window.get_width()*0.1), y, max(text.get_width(),window.get_width()*0.8) , text.get_height()], 0)
        pygame.draw.circle(window, white,[min(x,window.get_width()*0.1), y+text.get_height()/2], text.get_height()/2)
        pygame.draw.circle(window, white,[min(x,window.get_width()*0.1)+max(text.get_width(),window.get_width()*0.8), y+text.get_height()/2], text.get_height()/2)
        window.blit(text,(x,y))
        window.blit(logo,(window.get_width()//2 - logo.get_width()//2 , window.get_height()//2-logo.get_height()//2))
        sub_button.draw(window)
        sub_button.check(pygame.mouse.get_pos())
        back_button.draw(window)
        back_button.check(pygame.mouse.get_pos())
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 :
                if sub_button.hover:
                    running=False
                    return a
                elif back_button.hover:
                    return None

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER:
                    running=False
                    return a
                elif event.key==pygame.K_BACKSPACE:
                    a=a[0:-1]
                elif (event.mod & pygame.KMOD_CTRL):
                    if event.key==pygame.K_v:
                        a+=pyperclip.paste()
                    elif event.key==pygame.K_n:
                        a=""
                elif (event.key>=pygame.K_SPACE and event.key<=pygame.K_z) or  (event.key>=pygame.K_KP1 and event.key<=pygame.K_KP9) or event.key==pygame.K_KP0  or event.key==pygame.K_KP_PERIOD:
                    a+=event.unicode