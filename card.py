# import read_table
import time
import pickle
# ref_t=read_table.Read_table()
# file=open("bin/table.bin","wb")
# pickle.dump(ref_t,file)
# file.close()
file=open("bin/table.bin","rb")
ref=pickle.load(file)


import pygame
pygame.init()


class Card:
    
    def __init__(self,tier,Type,number):
        self.tier=tier
        self.type=Type
        self.number=number
        self.name=ref[tier][Type][number]["Name"]
        self.cost_C=ref[tier][Type][number]["cost_C"]
        self.cost_T=ref[tier][Type][number]["cost_T"]
        self.cost_D=ref[tier][Type][number]["cost_D"]
        self.cost_S=ref[tier][Type][number]["cost_S"]
        self.gain=ref[tier][Type][number]["gain"]
        self.w=ref[tier][Type][number]["w"]
        self.t=ref[tier][Type][number]["t"]
        self.l=ref[tier][Type][number]["l"]
        self.g_w=ref[tier][Type][number]["g_w"]
        self.g_t=ref[tier][Type][number]["g_t"]
        self.g_l=ref[tier][Type][number]["g_l"]
        self.locked= False
        self.x=0
        self.y=0
    def draw(self,window):
        font1 = pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 24)
        font2 = pygame.font.Font('res/fonts/Chocolate Covered Raindrops.ttf', 18)
        font3=pygame.font.Font('res/fonts/Blockletter.otf', 18)
        font4=pygame.font.Font('res/fonts/Blockletter.otf', 38)
        font5=pygame.font.Font('res/fonts/Blockletter.otf', 15)
        font6=pygame.font.Font('res/fonts/Blockletter.otf', 25)
        x=self.x
        y=self.y
        title= font1.render(self.name,True,(250,250,250))
        subtitle=font2.render({"R":"Rock","P":"Paper","S":"Scissors"}[self.type]  ,True,(0,0,0))

        ccost=font3.render(str(self.cost_C),True,(255,255,255))
        tcost=font3.render(str(self.cost_T),True,(255,255,255))
        dcost=font3.render(str(self.cost_D),True,(255,255,255))
        scost=font3.render(str(self.cost_S),True,(255,255,255))
        if(self.tier =='B' or self.tier=='C'):
            w=font4.render(('+' if self.w>0 else '')+str(self.w),True,(255,255,255))
            t=font4.render(('+' if self.t>0 else '')+str(self.t),True,(255,255,255))
            l=font4.render(('+' if self.l>0 else '')+str(self.l),True,(255,255,255))
        else:
            w0=font6.render(str(self.w[0]),True,(255,255,255))
            w1=font6.render(str(self.w[1]),True,(255,255,255))
            w2=font6.render(str(self.w[2]),True,(255,255,255))
            l0=font6.render(str(self.l[0]),True,(255,255,255))
            l1=font6.render(str(self.l[1]),True,(255,255,255))
            l2=font6.render(str(self.l[2]),True,(255,255,255))
            t0=font6.render(str(self.t[0]),True,(255,255,255))
            t1=font6.render(str(self.t[1]),True,(255,255,255))
            t2=font6.render(str(self.t[2]),True,(255,255,255))

        gw=font5.render(str(self.g_w),True,(255,255,255))
        gt=font5.render(str(self.g_t),True,(255,255,255))
        gl=font5.render(str(self.g_l),True,(255,255,255))

        body=pygame.image.load({"C":"res/images/blue.png" , "B":"res/images/purple.png" , "A":"res/images/red.png"}[self.tier])
        gain=pygame.image.load({"C":"res/images/gain_C.png","T":"res/images/gain_T.png","D":"res/images/gain_D.png","S":"res/images/gain_S.png","B":"res/images/gain_B.png"}[self.gain])
        lock=pygame.image.load("res/images/lock.png")

        window.blit(body,(x,y))
        window.blit(gain,(x,y))

        window.blit(title,(x+(body.get_width()/2)-(title.get_width()/2),y+(body.get_width()/50)))
        window.blit(subtitle,(x+(body.get_width()/2)-(subtitle.get_width()/2),y+title.get_height()*0.9))

        window.blit(ccost,(x+(body.get_width()*0.14)-ccost.get_width()/2,y+body.get_height()*0.29-ccost.get_height()/2))
        window.blit(tcost,(x+(body.get_width()*0.30)-tcost.get_width()/2,y+body.get_height()*0.29-tcost.get_height()/2))
        window.blit(dcost,(x+(body.get_width()*0.46)-dcost.get_width()/2,y+body.get_height()*0.29-dcost.get_height()/2))
        window.blit(scost,(x+(body.get_width()*0.62)-scost.get_width()/2,y+body.get_height()*0.29-scost.get_height()/2))
        if(self.tier =='B' or self.tier=='C'):
            window.blit(w,(x+(body.get_width()*0.4)-w.get_width()/2,y+body.get_height()*0.49-w.get_height()/2))
            window.blit(t,(x+(body.get_width()*0.4)-t.get_width()/2,y+body.get_height()*0.7-t.get_height()/2))
            window.blit(l,(x+(body.get_width()*0.4)-l.get_width()/2,y+body.get_height()*0.9-l.get_height()/2))
        else:
            window.blit(w0,(x+(body.get_width()*0.35)-w0.get_width()/2,y+body.get_height()*0.48-w0.get_height()/2))
            window.blit(t0,(x+(body.get_width()*0.35)-t0.get_width()/2,y+body.get_height()*0.68-t0.get_height()/2))
            window.blit(l0,(x+(body.get_width()*0.35)-l0.get_width()/2,y+body.get_height()*0.88-l0.get_height()/2))

            window.blit(w1,(x+(body.get_width()*0.59)-w1.get_width()/2,y+body.get_height()*0.48-w1.get_height()/2))
            window.blit(t1,(x+(body.get_width()*0.59)-t1.get_width()/2,y+body.get_height()*0.68-t1.get_height()/2))
            window.blit(l1,(x+(body.get_width()*0.59)-l1.get_width()/2,y+body.get_height()*0.88-l1.get_height()/2))

            window.blit(w2,(x+(body.get_width()*0.85)-w2.get_width()/2,y+body.get_height()*0.48-w2.get_height()/2))
            window.blit(t2,(x+(body.get_width()*0.85)-t2.get_width()/2,y+body.get_height()*0.68-t2.get_height()/2))
            window.blit(l2,(x+(body.get_width()*0.85)-l2.get_width()/2,y+body.get_height()*0.88-l2.get_height()/2))

        window.blit(gw,(x+(body.get_width()*0.15)-gw.get_width()/2,y+body.get_height()*0.49-gw.get_height()/2))
        window.blit(gt,(x+(body.get_width()*0.15)-gt.get_width()/2,y+body.get_height()*0.7-gt.get_height()/2))
        window.blit(gl,(x+(body.get_width()*0.15)-gl.get_width()/2,y+body.get_height()*0.9-gl.get_height()/2))
        if self.locked:
            window.blit(lock,(x,y))
    def click(self,pos):
        x=pos[0]
        y=pos[1]
        body=pygame.image.load("res/images/blue.png")
        width=body.get_width()
        height=body.get_height()
        if (not self.locked) :
            if self.x<=x<=self.x+width and self.y<=y<=self.y+height :
                return True
            else:
                return False
        else:
            return False
    def copy(self,c):
        self.tier=c.tier
        self.type=c.type
        self.number=c.number
        self.name=c.name
        self.cost_C=c.cost_C
        self.cost_T=c.cost_T
        self.cost_D=c.cost_D
        self.cost_S=c.cost_S
        self.gain=c.gain
        self.w=c.w
        self.t=c.t
        self.l=c.l
        self.g_w=c.g_w
        self.g_t=c.g_t
        self.g_l=c.g_l

class god:
    def __init__(self):
        self.card=None
        self.img=None
        self.x=100
        self.y=100
        self.dealt=False
    def refresh(self):
        if self.dealt:
            self.img=self.card
        else:
            self.img=("R","P","S")[int((time.time()*8)%3)]
    def draw(self,window):
        if self.img!=None:
            img=pygame.image.load("res/images/dealer_"+self.img+".png")
            window.blit(img,(self.x,self.y))

