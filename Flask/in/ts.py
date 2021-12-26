import requests as  req 
import pandas as pd 

datas = req.get('http://127.0.0.1/TODO/show.php') 

data = datas.json()

def insert(dats):
    d = req.post('http://127.0.0.1/TODO/add.php',data=dats)
    print(d.text)

#print(data)
with open('todo.txt','w+') as fl:
    for  dete in data:
        json_data = dict(dete)
    
        fl.write('id: '+json_data['id']+'\n'+'todos: '+json_data['todos']+'\n')
        print('id: '+json_data['id']+'\n'+'todos: '+json_data['todos']+'\n')


#insert({'todo':'lover'})

readfile = pd.read_csv('./wine.csv')
print(readfile.head(5))
        

     