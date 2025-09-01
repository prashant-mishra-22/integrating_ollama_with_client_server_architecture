import socket
import threading
import ollama

HEADER=64
FORMAT='ascii'
DISCONNECT_MESSAGE="<GoodBye>"
PORT=5050
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)


def collect_cuss_words():
    cuss_words = []
    fhand=open('cuss_words.txt','r')
    for line in fhand:
        words=line.strip()
        cuss_words.append(words)
    return cuss_words
cuss_words=collect_cuss_words()

def create_response(msg):
    olc=ollama.Client()
    llm="llama3.2"
    result=olc.generate(model=llm,prompt=msg)
    res= result.response
    res=res.encode(FORMAT)
    lines=[]
    pos=0
    while len(res)>0:
        if len(res)>64:
            lines.append(res[0:64])
            res=res[64:]
        else:
            lines.append(res+ (b' '*(64-len(res))))
            res=[]
    return lines

def handle_client(conn,addr):
    print(f"\n[NEW CONNECTION] {addr} is requesting to connect")
    connected = True
    username_length=conn.recv(HEADER).decode(FORMAT)
    username_length=int(username_length)
    username=conn.recv(username_length).decode(FORMAT)
    if username != '****':
        connected=False
        conn.send("invalid username : closing connection".encode(FORMAT))
    else:
        conn.send(" username accepted".encode(FORMAT))
        password_length=conn.recv(HEADER).decode(FORMAT)
        password_length=int(password_length)
        password=conn.recv(password_length).decode(FORMAT)
        if password != '****':
            connected=False
            conn.send("invalid password : closing connection".encode(FORMAT))
        else:
            conn.send(" password accepted".encode(FORMAT))
    if connected:
        print(f"\n[NEW CONNECTION] {addr} is connected.")
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        msg_length=int(msg_length)
        msg=conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            print(f"\n[DISCONNECT MESSAGE] {addr} send request to disconnect ")
            connected=False
            print(f"\n[DISCONNECT] {addr} is disconnected")
            conn.send("[DISCONNECTED]disconnected from server".encode(FORMAT))           
        else :
            words=msg.split(' ')
            flagc=False
            for word in words:
                if word in cuss_words:
                    flagc=True
            
            if flagc :
                res='[WARNING] use of cuss words are not allowed'
                res = res.encode(FORMAT)
                res = res + b' '*(64-len(res))
                conn.send(res)
                res='<GoodBye>'
                res = res.encode(FORMAT)
                res = res + b' '*(64-len(res))
                conn.send(res)
                connected=False
            else:
                print(f"\n[MESSAGE] {addr} send a message : {msg}")
                lines=[]
                lines=create_response(msg)
                for line in lines:
                    conn.send(line)
                conn.send(b' '*64)
            
    conn.close()




def start():
    server.listen()
    print(f"\n[LISTENING] server is listening on {ADDR}")
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"\n[ACTIVE CONNECTIONS ]{threading.active_count()-1}")


print(f"\n[STARTING] server is starting ...")
start()
