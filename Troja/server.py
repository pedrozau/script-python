import socket 

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.bind((HOST,PORT))
        s.listen(5) 
        client, addr = s.accept() 
        print('Got connection from ',addr)
        while True:
            data = input("#>")
            client.send(data.encode("UTF-8"))
            msg = client.recv(8192)
            print(msg.decode("UTF-8"))
    except ConnectionAbortedError:
          client, addr = s.accept() 
          print('Got connection from ',addr)


