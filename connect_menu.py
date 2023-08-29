import socket
import pickle
import ip_input
import error_menu
def Connect_menu(window):
    file=open("bin/ip.bin","rb")
    IP=pickle.load(file)
    file.close()
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((IP,5555))
        s.send(pickle.dumps("test"))
        s.close()
        return True
    except:
        done=False
        while not done:
            IP=ip_input.IP_INPUT(window,"Server IP:","Connect")
            if IP==None:
                return False
            try:
                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((IP,5555))
                s.send(pickle.dumps("test"))
                s.close()
                file=open("bin/ip.bin","wb")
                pickle.dump(IP,file)
                file.close()
                done=True
                return True
            except:
                error_menu.Error_menu(window,"Can,t connect try again")

