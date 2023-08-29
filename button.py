
import pygame
from math import sin,cos,radians
pygame.init()




font = pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 80)
class Button:
    def __init__(self,text,color):
        self.t=(max(0,color[0]-90),max(0,color[1]-90),max(0,color[2]-90))

        self.text=font.render(text,True,self.t)
        self.width=self.text.get_width()
        self.height=self.text.get_height()
        self.width_solved=self.width+self.height
        self.x=0
        self.y=0
        self.c1=(min(255,color[0]+10),min(255,color[1]+10),min(255,color[2]+10))
        self.c2=(max(0,color[0]-15),max(0,color[1]-15),max(0,color[2]-15))
        self.c3=(max(0,color[0]-100),max(0,color[1]-100),max(0,color[2]-100))
        
        self.hover=False
    def draw(self,window):
        c1=self.c1
        c2=self.c2
        c3=self.c3
        t=self.t
        x=self.x
        y=self.y
        w=self.width
        h=self.height
        margin=2
        pygame.draw.rect(window,c3,[x,y,w,h/2])
        
        pygame.draw.rect(window,c3,[x,y+h/2,w,h/2 +1])
        pygame.draw.circle(window,c3,[x,y+h/2],h/2)
        pygame.draw.circle(window,c3,[x+w,y+h/2],h/2)
        if self.hover:
            x+=margin
            y+=margin
            top=c2
            bottom=c1

        else:
            x-=margin
            y-=margin
            top=c1
            bottom=c2
        pygame.draw.circle(window,top,[x,y+h/2],h/2)
        pygame.draw.circle(window,bottom,[x+w,y+h/2],h/2)
        pygame.draw.polygon(window,top,[(x,y),(x+w,y),(x,y+h)])
        pygame.draw.polygon(window,bottom,[(x+w,y+h),(x+w,y),(x,y+h)])
        window.blit(self.text,(x,y))
    def check(self,pos):
        if self.x-self.height/2<=pos[0]<=self.x+self.width+self.height/2 and self.y<=pos[1]<=self.y+self.height:
            self.hover=True
        else:
            self.hover=False
