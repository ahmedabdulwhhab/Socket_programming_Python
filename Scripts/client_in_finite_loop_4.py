import socket
from time import sleep
print("send message, Bye or bye to End")
s = socket.socket()
s.connect(('10.0.0.1',12349))
while True:
    #str = input(" ip_1 for h1  for ip address: ")        #python 3
    #str = raw_input("S: ")      #python 2
    str="t"
    s.send(str.encode());
    received_data=s.recv(1024).decode()
    print ("received data",received_data)
    sleep(3)
    ###########
    str="d"
    s.send(str.encode());
    received_data=s.recv(1024).decode()
    print ("received data",received_data)
    sleep(3)
    ###########
    str="ip_1"
    s.send(str.encode());
    received_data=s.recv(1024).decode()
    print ("received data",received_data)
    sleep(3)
    ###########
    str="ip_2"
    s.send(str.encode());
    received_data=s.recv(1024).decode()
    print ("received data",received_data)
    sleep(3)    
    ###########
    str="ip_3"
    s.send(str.encode());
    received_data=s.recv(1024).decode()
    print ("received data",received_data)
    sleep(3) 

s.close()

