import pygame
import card
import network
import player
import error_menu


id=0
num=0
status=network.client_data(network.STATUS)
Quit=network.client_data(network.QUIT)
card_data=network.client_data(network.CARD)
pygame.init()
bg=(50,90,100)
clk=pygame.time.Clock()
# window=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
def Main_game(window,net):

	left=False
	right=False

	dealer=card.god()
	
	pl=[]
	status.ready=True
	status.played=False

	#player card stuff
	scrolling=False
	scroll_right=False
	scroll_left=False
	scroll_speed=5
	running=True
	cards_p=[]
	n=len(pl)
	w_max=0

	blue=pygame.image.load("res/images/blue.png")
	x=(window.get_width()/2)-(blue.get_width()/2)
	y=(window.get_height())-blue.get_height()


	dealer.x=window.get_width()//2 -50
	dealer.y=window.get_height()-blue.get_height()-150


	cards=[]
	for t in ('C','B','A'):
		for i in range({'C':4, 'B':6, 'A':6}[t]):
			for type in ('R','P','S'):
				cards.append(card.Card(t,type,i))
	i=0
	for c in cards:
		c.y=y
		c.x=i
		i+=blue.get_width()+5

	running = True
	w=0
	scroll_right=False
	scroll_left=False
	scroll_speed=5
	 
	while running:
		#communicatin stuff
		try:
			data=net.send(status)
		except:
			pass
		if data.type==network.GAME_WINDOW and data.window!="game":
			error_menu.Error_menu_green(window,data.window)
			running=False
			break
		elif data.type==network.HEADER:
			
			id=data.my_number
			num=data.number_of_players
			if num<len(pl):
				scrolling=False
				for i in range(len(pl)-num):
					del pl[-1]
					del cards_p[-1]
		elif data.type==network.PLAYER:
			if data.id<len(pl):
				pl[data.id].copy(data.player)
				try:
					cards_p[data.id].refresh(data.player)
				except:
					pass
			else:
				scrolling=False
				pl.append(player.Player("nj"))
				pl[-1].copy(data.player)
				cards_p.append(player.PlayerCard_game(data.player))
				if cards_p[-1].w>w_max:
					w_max=cards_p[-1].w
			n=len(pl)
			if not scrolling:
				if(window.get_width()>n*w_max+blue.get_width()):
					scrolling=False
					x=window.get_width()//(n+1)
					add=x
					for c in cards_p:
						c.x=x-(blue.get_width()//2)
						c.y=0 #window.get_height()//2 -c.h//2
						x+=add
				else:
					scrolling=True
					x=w_max
					for c in cards_p:
						c.x=x
						c.y=0
						x+=w_max
		elif data.type==network.DEALER:
			dealer.dealt=data.dealt
			dealer.card=data.deal
		#normal stuff
		window.fill(bg)
		dealer.refresh()
		dealer.draw(window)
		
		
		for c in cards:
			if c.x> -blue.get_width() and c.x<window.get_width():
				c.draw(window)
		if scroll_right:
			count+=1
			if count>60:
				scroll_right=False
				scroll_speed=5
			if cards[0].x<0:
				for c in cards:
					c.x+=scroll_speed
			else:
				temp=cards[0].x
				for c in cards:
					c.x-=temp
		if scroll_left:
			count+=1
			if count>60:
				scroll_left=False
				scroll_speed=5
			if cards[-1].x>window.get_width()*0.85:
				for c in cards:
					c.x-=scroll_speed

		for c in cards_p:
			c.draw(window)
		pygame.display.update()
		clk.tick(100)
		
		try:
			for c in cards:
				if c.click(pygame.mouse.get_pos()) and pl[id].turn:
					c.y=y-10
				else:
					c.y=y
			for c in cards:
				try:
					c.locked=(pl[id].c<c.cost_C) or (pl[id].t<c.cost_T) or (pl[id].d<c.cost_D) or (pl[id].s<c.cost_S)
				except:
					c.locked=c.cost_C>0
		except:
			pass
		if scrolling:
			if left :
				for c in cards_p:
					c.x-=25
			if right :
				for c in cards_p:
					c.x+=25
		for event in pygame.event.get():
			if event.type==pygame.MOUSEWHEEL:
				if event.y==-1 :
					if scroll_left :
						if count<25:
							scroll_speed+=10
						count=0
					elif scroll_right:
						scroll_right=False
						count=0
						scroll_speed=5
					else:
						scroll_left=True
						scroll_right=False
						count=0
						scroll_speed=5
				elif event.y==1 :
					if scroll_right:
						if count<25:
							scroll_speed+=10
						count=0
					elif scroll_left:
						scroll_left=False
						count=0
						scroll_speed=5
					else:
						scroll_right=True
						scroll_left=False
						count=0
						scroll_speed=5
			elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1 :
				for c in cards:
					if c.click(pygame.mouse.get_pos()) and pl[id].turn:
						card_data.card.copy(c)
						net.send(card_data)
			elif event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
				net.send(Quit)
				del pl
				running = False
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
    
		
