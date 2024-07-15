from api import *

server=socket_server('192.168.2.121',8000)

# clients=[]



# while True:
#     conn,address=server.accept()
#     if address not in clients:
#         clients.append(address)

client,address=server.accept()

while True:
    data=input()
    send(client,data)