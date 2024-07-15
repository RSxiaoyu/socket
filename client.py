from api import *


def recvMethod():
    while True:
        data=recv(client)
        if data is not None:
            print(f'{data}')


def inputMethod():
    while True:
        send(client, input())


client=socket_client('192.168.2.121')
print(f"Client > Connected.")

createThread(target=recvMethod)  # 子线程 阻塞接收消息
createThread(target=inputMethod) # 子线程 阻塞等待输入
