import socket

print("send message, Bye or bye to End")
s = socket.socket()
s.connect(('10.0.0.1',12345))
while True:
    str = input("t for time, d for date , IP for ip address: ")        #python 3
    #str = raw_input("S: ")      #python 2
    s.send(str.encode());
    if(str == "Bye" or str == "bye"):
        break
    print ("N:",s.recv(1024).decode())
s.close()
