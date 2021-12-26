import os 
import time 

"""
@author: Pedro Zau
@description: this software  shutdown your computer 
@version: 0.1
"""
class  Computer:
    
    def __init__(self):
        pass

    def week(self):
        if(time.strftime("%w") == 0):
            return  1
        elif(time.strftime("%w") == 1):
            return 2
        elif(time.strftime("%w") == 2):
            return 3 
        elif(time.strftime("%w") == 3):
            return 4
        elif(time.strftime("%w") == 4):
            return 5
        elif(time.strftime("%w") == 5):
            return 6
        elif(time.strftime("%w") == 6):
            return 7
    
    def shut_down_week(self):
        while True:
            self.shut = time.strftime("%H:%M")
            if  self.shut == '19:30':
                os.system("shutdown -s")
                #print('OK 1')
            else:
                pass
                #time.sleep(1)
                #os.system("cls")
                #print(time.strftime("%H:%M:%S"))
            
               

    def shut_down(self):
        while True:
            self.shut = time.strftime("%H:%M")
            if  self.shut == '09:30' or  self.week() == 2 or self.week() == 3 or self.week() == 4 or self.week() == 5 or self.week() == 6:
                #os.system("shutdown -s")
                print('OK 2')
            else:
                pass
                #time.sleep(1)
                #os.system("cls")
                #print(time.strftime("%H:%M:%S"))
    def shut_down_sch(self):
        while True:
            self.shut = time.strftime("%H:%M")
            if  self.shut == '13:00'  or self.week() == 2 or self.week() == 3 or self.week() == 4 or self.week() == 5 or self.week() == 6:
                os.system("shutdown -s")
                #print('OK 3')
            else:
                pass
                #time.sleep(1)
                #os.system("cls")
                #print(time.strftime("%H:%M:%S"))


computer = Computer()
computer.shut_down()
computer.shut_down_week()
computer.shut_down_sch()