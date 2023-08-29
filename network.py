import socket
import pickle
import card
GAME_WINDOW=0
HEADER=1
PLAYER=2
DEALER=3

INIT=0
STATUS=1
CARD=2
QUIT=3
class server_data:
    def __init__(self,type):
        self.type=type
        if type==GAME_WINDOW:
            self.window=None
            self.id=0
        elif type==HEADER:
            self.number_of_players=0
            self.my_number=0
        elif type==PLAYER:
            self.player=None
            self.id=0
        elif type==DEALER:
            self.deal=None
            self.dealt=False
class client_data:
    def __init__(self,type):
        self.type=type
        if type==INIT:
            self.name=None
            self.host=False
            self.id=0
        elif type==STATUS:
            self.ready=False
            self.played=False
        elif type==CARD:
            self.card=card.Card("C","R",0)
        elif type==QUIT:
            pass

class Network:
    def __init__(self):
        self.s=None
        pass
    def connect(self):
        file=open("bin/ip.bin","rb")
        IP=pickle.load(file)
        file.close()
        self.s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((IP,5555))


    def send(self,message):
        self.s.send(pickle.dumps(message))
        return pickle.loads(self.s.recv(2048*2))
    def end(self):
        self.s.close()
