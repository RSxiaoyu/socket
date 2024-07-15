from api import *


def recvMethod():
    while True:
        data=recv(client)
        if data is not None:
            print(f'{data}')


def inputMethod():
    while True:
        send(client, input())


client = socket.socket()
client.connect(("192.168.2.121", 8000))
print(f"Client > Connected.")

createThread(target=recvMethod)  # 子线程 阻塞接收消息
createThread(target=inputMethod) # 子线程 阻塞等待输入
