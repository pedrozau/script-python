import bcrypt 

password = b"nguimbi"

#hashed = bcrypt.hashpw(password,bcrypt.gensalt())
hashed_pass = b'$2b$12$EVw4e.NYBwTK0Q.DwxrxPe/Ig36USDfDMT09inTXnYArv.iTVibI6'

if(bcrypt.checkpw(password,hashed_pass)):
    print('password is  OK')
else:
    print('Password icorrect !!')


