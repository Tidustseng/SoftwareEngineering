import socket
HOST = '192.168.' + raw_input('please type in your host ip address : 192.168.')
PORT = 8001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    # cmd = raw_input("Please input msg:")
    cmd = '1 2'
    s.send(cmd)
    data = s.recv(1024)
    print data
    s.close()