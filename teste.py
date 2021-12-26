from hashlib import blake2b
from base64  import b64encode, b64decode
#h = blake2b()
#h.update(b'nguimbisenhadia1j')
#print(h.hexdigest())
#print(b64decode(b'1c7c62b9fee4913909d00361c360d88e03912c6ce712bfbbf510b3e0857d74f16c314404aa3514c4abb8fdd1c1491a7548097edcd80230475adbf3d5397f835a'))
"""
mypassword = '1c7c62b9fee4913909d00361c360d88e03912c6ce712bfbbf510b3e0857d74f16c314404aa3514c4abb8fdd1c1491a7548097edcd80230475adbf3d5397f835a'

with open('file.txt','r+') as file:
    for files in file.readlines():
        h = blake2b()
        h.update(b'{files}')
        passwrd = h.hexdigest()
        print(f'password --> {passwrd}')
        if passwrd == mypassword:
            print(f'password is [{files}]')
            break
        else:
            print('don`t find password')
"""
x = []
x = range(1,100)

for y in x:
    print(y)