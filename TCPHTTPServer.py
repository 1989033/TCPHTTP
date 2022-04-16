#!/usr/bin/python3
import socket

host = ''
port = 19893
buff_size = 1024
backlog = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host,port)
sock.bind(server_address)
sock.listen(backlog)

while True:
    print("waiting for requests...")
    data_sock, address = sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data_sockrecv(buff_size)
    print(message.decode())
    if message:
        server_response = "<HTML><BODY><H1> Hello, World! </H1></BODY></HTML>"
        data_sock.sendall(server_response.encode())
        print("++++++++++")
    else:
        print("----------")
    data_sock.close()

