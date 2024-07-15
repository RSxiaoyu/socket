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

def socket_server(address:str,port:int,listen:int=5) -> socket.socket:
    server=socket.socket()
    server.bind((address,port))
    server.listen(listen)
    return server
