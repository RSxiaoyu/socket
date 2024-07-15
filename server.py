from api import *

server=socket_server('192.168.2.121',8000)

class Client:
    def __init__(self,conn,address) -> None:
        self.conn=conn
        self.address=address

def broadcast():
    while True:
        data=input()
        for client in clients:
            send(client.conn,data)

clients=[]

def clientThread():
    while True:
        client=Client(server.accept())
        if client not in clients:
            clients.append(client)


createThread(clientThread)
createThread(broadcast)

client,address=server.accept()
