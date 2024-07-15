from api import *

server=socket_server('192.168.2.121',8000)


class Client:
    def __init__(self,socket_client) -> None:
        self.conn,self.address=socket_client

def broadcast():
    while True:
        data=input()
        for client in clients:
            send(client.conn,f'Server > {data}')
def receive():
    while True:
        for client in clients:
            data=recv(client.conn)
            print(data)
            if data is not None:
                print(f'{client.address} > {data}')

def clientThread():
    while True:
        client=Client(server.accept())
        if client not in clients:
            clients.append(client)

clients=[]
createThread(clientThread)
createThread(broadcast)


