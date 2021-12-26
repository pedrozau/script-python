import mysql.connector
conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tarefa')
cursor = conexao.cursor()
consulta = ("select * from task")
cursor.execute(consulta)
for curs in cursor:
    print(curs)


cursor.close()
conexao.close()