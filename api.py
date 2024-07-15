import socket
import struct
from threading import Thread

def send(client: socket, data: bytes or str):
    """
    
    """
    if isinstance(data, str):
        data = data.encode()
    client.send(struct.pack("i", len(data)))
    client.send(data)


def recv(client: socket) -> str:
    recv = client.recv(4)
    if recv == b"":
        return None
    data_len = struct.unpack("i", recv)[0]
    return client.recv(data_len).decode()

def createThread(target=None,args=()):
    Thread(target=target,args=args).start()

def socket_server(address:str,port:int=8000,listen:int=5) -> socket.socket:
    server=socket.socket()
    server.bind((address,port))
    server.listen(listen)
    return server

def socket_client(address:str,port:int=8000) -> socket.socket:
    client = socket.socket()
    client.connect((address,port))
    return client

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google的公共DNS服务器
        ip = s.getsockname()[0]
    except Exception as e:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip
