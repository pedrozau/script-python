import socket 
import os
import sys
import re 

"""

"""

class Scanner:

    def __init__(self, host):
        self.host = host 
        
    
    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, vl):
        change_host = re.compile(r'http://www')
        host_ch = change_host.sub('',vl)
        self._host = host_ch
         


    def sockete(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def scann(self):
        port = [80,443,21,23,22,25,53,67,68,69,110,123,137,138,139,143,161,162,179,389]
        client = self.sockete()
        
        for ports in port:
            client.settimeout(1)
            code = client.connect_ex((self.host, ports))
            if code == 0:
                print(f'[*] {self.host} ---- [{ports}] OPEN')
            else:
                print(f'[*] {self.host} ---- [{ports}] CLOSED')
        



try:
    
    argumento = sys.argv[1]  # 'http://127.0.0.1' 
    scanner = Scanner(argumento)
    scanner.scann()
except:
    print("-----------  Argumento não foi passada -----------")
    print("[*] exemplo: python portscan  facebook.com")
