import api
local_ip=api.get_ip()
server=api.socket_server(local_ip)
client=api.socket_client('192.168.2.121')
print('Communication established.')