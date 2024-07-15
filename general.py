import api
local_ip=api.get_ip()
server=api.socket_server(local_ip)
client=api.socket_client('192.168.2.128')
print('Communication established.')

def recvMethod():
    while True:
        data=api.recv(server)
        if data is not None:
            print(f'{data}')


def inputMethod():
    while True:
        api.send(client, input())

api.createThread(target=recvMethod)  # 子线程 阻塞接收消息
api.createThread(target=inputMethod) # 子线程 阻塞等待输入