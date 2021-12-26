import bcrypt 


password =  b"nguimbi"

hashed = bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed)