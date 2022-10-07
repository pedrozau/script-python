import os 
import shutil 


dele = 'C:/Users/Mr.Pedro/Desktop/'

try:
    while(True):
        for root, dirs , files in os.walk(dele):
            for file in files:

                 if file in range(99,10006):
                     print(f'{file}')
                     os.remove(file)
    
except:
       print("Error!!")