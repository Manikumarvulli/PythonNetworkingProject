from threading import Thread #to reduce time complexity
import socket#end to end connection two way communication
host = input('host > ')#ip or domain name
from_port = int(input('start scan from port > '))
to_port = int(input('finish scan to port > '))
counting_open = []
counting_close = []
threads = []
class  Finding_unsedports:
    def scan(port):
        s = socket.socket()
        result = s.connect_ex((str(host),port))#0 or eerno
        #print(('checking ports > '+(str(port))))
        if result == 0:
            counting_open.append(port)
            #print((str(port))+' -> is open')
            peer = s.getpeername()#it gives hostname and port as tuple
            print(peer)
            s.close()
        else:
            counting_close.append(port)
            #print((str(port))+' -> is closed')
            s.close()

    for i in range(from_port, to_port+1):
        t = Thread(target=scan, args=[i])
        threads.append(t)
        t.start()

    [x.join() for x in threads]


print("open ports={}".format(counting_open))
print("closed ports={}".format(counting_close))
Finding_unsedports()