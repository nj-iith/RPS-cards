import socket
import time
import random
from _thread import *
import pickle
import player
import network
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
games=[]

class game:
    def __init__(self):
        self.started=False
        self.dealt=False
        self.players=[]
        self.deal=None
        self.last_deal=0
        self.dlt_q=[]
        self.total_damage=0
        self.numbers={"R":0 ,"P":0, "S":0}
    def all_ready(self):
        out=True
        for p in self.players:
            out=out and p.ready
        return out
    def all_played(self):
        out=True
        for p in self.players:
            out=out and (p.played or p.hp==0)
        return out
    def alive(self):
        out=0
        for p in self.players:
            if(p.hp>0):
                out+=1
        return out
    def winner_id(self):
        for i in range(len(self.players)):
            if self.players[i].hp>0:
                return i

def client_handle(conn):
    
    id=-1
    game_id=-1
    count=-1
    running=True
    gw=network.server_data(network.GAME_WINDOW)
    header=network.server_data(network.HEADER)
    p=network.server_data(network.PLAYER)
    dealer=network.server_data(network.DEALER)


    while running:
        try:
            data =pickle.loads(conn.recv(4096))
            if data.type==network.INIT:
                count=-1
                # print(data.host)
                if data.host:
                    id=0
                    g=game()
                    g.players.append(player.Player(data.name))
                    games.append(g)
                    game_id=len(games)-1
                    gw.window="lobby"
                    gw.id=game_id
                    conn.send(pickle.dumps(gw))
                else:
                    game_id=data.id
                    if game_id<len(games) and not games[game_id].started:
                        games[game_id].players.append(player.Player(data.name))
                        id=len(games[game_id].players)-1
                        gw.window="lobby"
                        gw.id=game_id
                        conn.send(pickle.dumps(gw))
                    else:
                        gw.window="error"
                        conn.send(pickle.dumps(gw))
                    
            elif data.type==network.STATUS:
                games[game_id].players[id].ready=data.ready
                if gw.window=="lobby" and games[game_id].all_ready():
                    if id==0:
                        games[game_id].started=True
                    gw.window="game"
                    
                    count=-1
                    conn.send(pickle.dumps(gw))
                elif gw.window=="game" and games[game_id].alive()<=1 :
                    if games[game_id].alive()==0 :
                        gw.window="everybody died. Play again if wanna find who is the real winner"
                        conn.send(pickle.dumps(gw))
                    elif games[game_id].alive()==1:
                        if games[game_id].winner_id()==id:
                            gw.window="Congratulationsss!!!! time to sleep with peace, champion"
                        else:
                            gw.window=games[game_id].players[games[game_id].winner_id()].name + " out played u all, Better luck next time"
                        conn.send(pickle.dumps(gw))
                else:

                    if count==-1:
                        header.number_of_players=len(games[game_id].players)
                        header.my_number=id
                        conn.send(pickle.dumps(header))
                        count=0
                    else:
                        if count<len(games[game_id].players):
                            p.player=games[game_id].players[count]
                            p.id=count
                            conn.send(pickle.dumps(p))
                            count+=1
                        else:
                            dealer.deal=games[game_id].deal
                            dealer.dealt=games[game_id].dealt
                            conn.send(pickle.dumps(dealer))
                            count=-1
                


            elif data.type==network.CARD:
                games[game_id].players[id].g+=games[game_id].numbers[data.card.type]
                games[game_id].numbers[data.card.type]+=1
                games[game_id].players[id].card.copy(data.card)
                games[game_id].players[id].play()

                # do_normal_stuff()
                if count==-1:
                    header.number_of_players=len(games[game_id].players)
                    header.my_number=id
                    conn.send(pickle.dumps(header))
                    count=0
                else:
                    if count<len(games[game_id].players):
                        p.player=games[game_id].players[count]
                        p.id=count
                        conn.send(pickle.dumps(p))
                        count+=1
                    else:
                        header.number_of_players=len(games[game_id].players)
                        header.my_number=id
                        conn.send(pickle.dumps(header))
                        count=0
            # normal stuff done
            elif data.type==network.QUIT:
                if(id==0 and len(games[game_id].players)==1):
                    # print("game done")
                    del games[game_id]
                    conn.send(pickle.dumps(header))
                    # print("num of active games=",len(games))
                    return
                for i in range(id,len(games[game_id].players)):
                    games[game_id].dlt_q.append(i)
                    header.number_of_players=len(games[game_id].players)
                    header.my_number=id
                    conn.send(pickle.dumps(header))
                return

            
            if id==0:
                min_g=games[game_id].players[0].g
                for plyr in games[game_id].players:
                    if plyr.g<min_g:
                        min_g=plyr.g
                for plyr in games[game_id].players:
                    plyr.g-=min_g


                max_g=0
                for plyr in games[game_id].players:
                    if not plyr.played and plyr.g>max_g:
                        max_g=plyr.g
                for i in range(len(games[game_id].players)):
                    if not games[game_id].players[i].played and games[game_id].players[i].g==max_g and games[game_id].players[i].hp>0:
                        high_p=i
                        break
                for i in range(len(games[game_id].players)):
                    games[game_id].players[i].turn=(i==high_p)
                    # print("plyr"+str(i)+" turn is "+str(i==high_p))
                if games[game_id].all_played():
                    if games[game_id].dealt :
                        if time.time()-games[game_id].last_deal > 5:
                            games[game_id].numbers["R"]=0
                            games[game_id].numbers["P"]=0
                            games[game_id].numbers["S"]=0
                            games[game_id].dealt=False
                            for i in range(len(games[game_id].players)):
                                games[game_id].players[i].evalu(games[game_id].players[i].result(games[game_id].deal))
                            for i in range(len(games[game_id].players)) :
                                # print(games[game_id].players[i].damage)
                                for j in range(0,len(games[game_id].players)-1):
                                    if j<i :
                                        k=j
                                    else:
                                        k=j+1
                                    games[game_id].players[i].hp-=max(0,games[game_id].players[k].damage-games[game_id].players[i].defence)
                                if games[game_id].players[i].hp<0:
                                    games[game_id].players[i].hp=0
                                else:
                                    games[game_id].players[i].hp=min(100,games[game_id].players[i].hp+games[game_id].players[i].heal)
                                games[game_id].players[i].played=False
                            
                    else:
                        games[game_id].dealt=True
                        games[game_id].deal=random.choice(["R","P","S"])
                        games[game_id].last_deal=time.time()




            if(len(games[game_id].dlt_q)>0):
                # print("dlt q=",games[game_id].dlt_q)
                if id==0 and len(games[game_id].dlt_q)==1 :
                    del games[game_id].players[games[game_id].dlt_q[0]]
                    del games[game_id].dlt_q[0]
                elif games[game_id].dlt_q[-1] == id :
                    # print("player",id,"became player",id-1)
                    id-=1
                    del games[game_id].dlt_q[-1]

        except:
            running=False
    #pass
    
def client_connect(conn):
    data =pickle.loads(conn.recv(4096))
    if data=="test" :
        return
    else:
        conn.send(pickle.dumps("grrrr"))
        client_handle(conn)



IP=get_ip()
print("IP of server:"+IP)
s.bind((IP, 5555))
s.listen()
while True:
    conn,addr =s.accept()
    start_new_thread(client_connect,tuple([conn]))