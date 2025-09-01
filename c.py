import socket 
import time
import re

HEADER=64
FORMAT='ascii'
DISCONNECT_MESSAGE="<GoodBye>"

PORT=5050
SERVER="172.20.10.3"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


    

def sendmsg(msg):
    message = msg.encode(FORMAT)
    msg_length=len(message)
    send_length= str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    

username=input("enter your username : = ")
username = username.encode(FORMAT)
username_length=len(username)
send_length= str(username_length).encode(FORMAT)
send_length += b' ' * (HEADER-len(send_length))
client.send(send_length)
client.send(username)
res=client.recv(64).decode(FORMAT)
if res=="invalid username : closing connection":
    print(f"response received : {res}")
else:
    print(f"response received : {res}")
    password=input("enter your password : = ")
    password = password.encode(FORMAT)
    password_length=len(password)
    send_length= str(password_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))
    client.send(send_length)
    client.send(password)
    res=client.recv(64).decode(FORMAT)
    if res=="invalid password : closing connection":
        print(f"response received : {res}")
    else:
        print(f"response received : {res}")
        connected=True
        while connected:
            print()
            msg=input("enter your message (enter <GoodBye> to disconnect): ")
            email_re=r'[a-zA-Z0-9._]+@[a-zA-Z]+[.][a-zA-Z]{2,3}'
            pr1=r'\b\+91\-[1-9][0-9]{9}\b'
            pr2=r'\b[1-9][0-9]{9}\b'

            email=re.findall(email_re,msg)
            p1=re.findall(pr1,msg)
            p2=re.findall(pr2,msg)

            if len(email) != 0  or len(p1) != 0 or len(p2) != 0:
                if len(email) != 0:
                    print('you are not allowed to share email address with the chat help')
                if len(p1) != 0 or len(p2) != 0:
                    print('you are not allowed to share phone number with the chat help')
            else:
                sendmsg(msg)
                if msg==DISCONNECT_MESSAGE:
                    res=client.recv(2048).decode(FORMAT)
                    print(res)
                    connected=False
                else:
                    res=client.recv(64)
                    while res != b' '*64 and connected:
                        if res.decode(FORMAT).strip() == '<GoodBye>':
                            connected=False
                            break
                        print(res.decode(FORMAT),end="")
                        time.sleep(0.5)
                        res=client.recv(64)
                    print()
                
                
            
