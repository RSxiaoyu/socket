import api
local_ip=api.get_ip()
print(local_ip)
server=api.socket_server(local_ip)
conn,address=server.accept()
print(f"{address} > {local_ip} established.")

target_address='192.168.2.121'
client=api.socket_client(target_address)
print(f"{local_ip} > {target_address} established.")

def recvMethod():
    while True:
        data=api.recv(conn)
        if data is not None:
            print(f'{data}')


def inputMethod():
    while True:
        api.send(client, input())

api.createThread(target=recvMethod)  # 子线程 阻塞接收消息
# api.createThread(target=inputMethod) # 子线程 阻塞等待输入