#!/usr/bin/python3
import socket

host = ''
port = 19893
buff_size = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (host, port)
sock.bind(server_address)
print(sock)

while True:
    print("waiting for requests...")
    data_sock, address = conn_sock.accept()
    print("echo request from %s port %s" % address)
    message = data_sock.recv(BUFF_SIZE)

    try :
        num =int(data)
        if num %2:
            answer = "Odd Number"
        else:
            answer = "Even Number"

    except Exception as e:
            answer:str = "Not Number"

socket.sendto(message,client_address)
sock.close()