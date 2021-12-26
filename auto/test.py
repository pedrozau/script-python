import threading 


def cont():

     i = 0
     i += 1
     print(i)
     timer = threading.Timer(5, cont)
    


