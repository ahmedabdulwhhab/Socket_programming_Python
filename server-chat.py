import socket

port = 12345
"""
manually confirm port is not used.
#find the process using the port
lsof -i :8000
#and kill it
kill -9 process_id
"""
print("waiting client to send message, Bye or bye to End")
s = socket.socket()
print("socket.socke()==",s)
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
while True:
    rcvdData = c.recv(1024).decode()
    print ("S:",rcvdData)
    if(rcvdData=='t'):
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        c.send(current_time.encode())
    elif(rcvdData=='d'):
        from datetime import date
        today = date.today()
        #dd/mm/YY
        d1 = today.strftime("%d/%m/%Y")
        c.send(d1.encode())
    else:
        sendData = input("N: ")
        c.send(sendData.encode())
        if(sendData == "Bye" or sendData == "bye"):
            break
c.close()
