import pygame
import button
import card
font = pygame.font.Font('res/fonts/Chocolate Covered Raindrops BOLD.ttf', 100)
font2 = pygame.font.Font('res/fonts/Blending Attraction.otf', 12)
font3=pygame.font.Font('res/fonts/SaucerBB.ttf', 100)
img=pygame.image.load("res/images/playerCard.png")
img2=pygame.image.load("res/images/slot.png")
img3=pygame.image.load("res/images/dead.png")
hp_icon=pygame.image.load("res/images/hp_icon.png")
c_icon=pygame.image.load("res/images/c_icon.png")
t_icon=pygame.image.load("res/images/t_icon.png")
d_icon=pygame.image.load("res/images/d_icon.png")
s_icon=pygame.image.load("res/images/s_icon.png")

class Player:
    def __init__(self,name):
        self.name=name
        self.hp=100
        self.c=0
        self.t=0
        self.d=0
        self.s=0
        self.g=0
        self.damage=0
        self.defence=0
        self.heal=0
        self.played=False
        self.ready=False
        self.card=card.Card("C","R",0)
        self.id=0
        self.turn=False
    def copy(self,c):
        self.name=c.name
        self.hp=c.hp
        self.c=c.c
        self.t=c.t
        self.d=c.d
        self.s=c.s
        self.g=c.g
        self.damage=c.damage
        self.defence=c.defence
        self.heal=c.heal
        self.played=c.played
        self.ready=c.ready
        self.card=c.card
        self.id=c.id
        self.turn=c.turn
    def play(self):
        self.c-=self.card.cost_C
        self.t-=self.card.cost_T
        self.d-=self.card.cost_D
        self.s-=self.card.cost_S
        self.played=True
    def result(self,deal):
        return {"R" : {"R":"t"  ,  "P":"l"  ,  "S":"w"}  ,  "P" : {"R":"w"  ,  "P":"t"  ,  "S":"l"}  ,  "S" : {"R":"l"  ,  "P":"w"  ,  "S":"t"}}[self.card.type][deal]
    def evalu(self,out_come):
        self.damage=0
        self.defence=0
        self.heal=0
        if out_come=="w":
            self.g+=self.card.g_w
            if self.card.tier=="A":
                self.damage=self.card.w[0]
                self.defence=self.card.w[1]
                self.heal=self.card.w[2]
            else:
                if self.card.gain=="C" :
                    self.c+=self.card.w
                elif self.card.gain=="T" :
                    self.t+=self.card.w
                elif self.card.gain=="D" :
                    self.d+=self.card.w
                elif self.card.gain=="S" :
                    self.s+=self.card.w
        elif out_come=="t":
            self.g+=self.card.g_t
            if self.card.tier=="A":
                self.damage=self.card.t[0]
                self.defence=self.card.t[1]
                self.heal=self.card.t[2]
            else:
                if self.card.gain=="C" :
                    self.c=max(0,self.c+self.card.t)
                elif self.card.gain=="T" :
                    self.t=max(0,self.t+self.card.t)
                elif self.card.gain=="D" :
                    self.d=max(0,self.d+self.card.t)
                elif self.card.gain=="S" :
                    self.s=max(0,self.s+self.card.t)
        elif out_come=="l":
            self.g+=self.card.g_l
            if self.card.tier=="A":
                self.damage=self.card.l[0]
                self.defence=self.card.l[1]
                self.heal=self.card.l[2]
            else:
                if self.card.gain=="C" :
                    self.c=max(0,self.c+self.card.l)
                elif self.card.gain=="T" :
                    self.t=max(0,self.t+self.card.l)
                elif self.card.gain=="D" :
                    self.d=max(0,self.d+self.card.l)
                elif self.card.gain=="S" :
                    self.s=max(0,self.s+self.card.l)
class PlayerCard_lobby:
    def __init__(self,player):
        self.player=player
        self.x=0
        self.y=0
        if player.ready:
            colr=(0,255,0)
        else:
            colr=(255,0,0)
        self.name=button.Button(self.player.name,colr)
        self.w=max(self.name.width_solved,img.get_width())
        self.h=self.name.height+img.get_height()
    def refresh(self,player):
        self.player=player
        if player.ready:
            colr=(0,200,0)
        else:
            colr=(200,0,0)
        self.name=button.Button(self.player.name,colr)
        self.w=max(self.name.width_solved,img.get_width())
        self.h=self.name.height+img.get_height()
    def draw(self,window):
        window.blit(img,(self.x,self.y))
        self.name.x=self.x+img.get_width()//2 - self.name.width//2
        self.name.y=self.y+img.get_height()*1.1
        self.name.draw(window)
class PlayerCard_game:
    def __init__(self,player):
        self.player=player
        self.x=0
        self.y=0
        colr=(100,200,200)
        self.name=button.Button(self.player.name,colr)
        self.w=max(self.name.width_solved,img.get_width())
        self.h=self.name.height+img.get_height()
    def refresh(self,player):
        self.player=player
        self.w=max(self.name.width_solved,img.get_width())
        self.h=self.name.height+img.get_height()
    def draw(self,window):
        if(self.player.turn):
            colr=(100,200,200)
        else:
            colr=(200,200,200)
        self.name=button.Button(self.player.name,colr)
        if self.player.hp==0 :
            window.blit(img3,(self.x,self.y))
        elif self.player.played: 
            self.player.card.x=self.x
            self.player.card.y=self.y
            self.player.card.draw(window)
        else:
            window.blit(img2,(self.x,self.y))
            text=font3.render(str(self.player.g),True,(150,150,150))
            f=1
            if(text.get_width()>img2.get_width()*0.8):
                f=(img2.get_width()-10)/text.get_width()
                # text=pygame.transform.scale(text,(f*text.get_width(),f*text.get_height()))
            font_r = pygame.font.Font('res/fonts/SaucerBB.ttf', int(f*100))
            text=font_r.render(str(self.player.g),True,(150,150,150))
            window.blit(text,(self.x+img2.get_width()/2-text.get_width()/2,self.y+img2.get_height()/2-text.get_height()/2))
        text_hp=font2.render(str(self.player.hp),True,(80,20,20))
        c2=(80,80,0)
        text_c=font2.render(str(self.player.c),True,c2)
        text_t=font2.render(str(self.player.t),True,c2)
        text_d=font2.render(str(self.player.d),True,c2)
        text_s=font2.render(str(self.player.s),True,c2)
        
        self.name.x=self.x+img.get_width()//2 - self.name.width//2
        self.name.y=self.y+img.get_height()+hp_icon.get_height()+5
        self.name.draw(window)
        dx=img.get_width()//5
        x1=self.x+3
        x=self.x+dx/2
        y=self.y+img.get_height()+27
        y1=y-25
        

        window.blit(hp_icon,(x1,y1))
        window.blit(c_icon,(x1+dx,y1))
        window.blit(t_icon,(x1+2*dx,y1))
        window.blit(d_icon,(x1+3*dx,y1))
        window.blit(s_icon,(x1+4*dx,y1))

        window.blit(text_hp,(x-text_hp.get_width()/2,y))
        window.blit(text_c,(x+dx-text_c.get_width()/2,y))
        window.blit(text_t,(x+2*dx-text_t.get_width()/2,y))
        window.blit(text_d,(x+3*dx-text_d.get_width()/2,y))
        window.blit(text_s,(x+4*dx-text_s.get_width()/2,y))