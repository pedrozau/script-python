from flask import Flask, render_template, url_for,request,redirect,session,jsonify
import mysql.connector 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/api")
def  task():
    ''' 
    link:http://127.0.0.1/omega/public/image/
    '''
    #return jsonify({'login':db()})
    return render_template('ex.html',datas=db())

@app.route('/app')
def show():
    return render_template('form.html')


@app.route('/creat',methods=['POST','GET'])
def  test():
    if request.method == 'POST':

        todo = request.form['todo']
        
        creat_db(todo)
    
        return redirect(url_for('voir'))

@app.route('/show')
def voir():

    return jsonify({'todo':show_db()})


def creat_db(todo):

    conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='todo')
    cursor = conexao.cursor()
    datas = [todo]
    comando_sql = "INSERT INTO `todo` (`id`, `todo`) VALUES (NULL, %s);"
    cursor.execute(comando_sql, datas)
    conexao.commit()
    cursor.close()
    conexao.close()

def show_db():
    conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='todo')
    cursor = conexao.cursor()
    consulta = ("select * from todo")
    cursor.execute(consulta)
    datas = []
    for (id,todo) in cursor:
        data = {}
        data['id'] = id 
        data['nome'] = todo 
       

        datas.append(data)



    return datas


    cursor.close()
    conexao.close()

def db():
    conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='omega')
    cursor = conexao.cursor()
    consulta = ("select * from  login ")
    cursor.execute(consulta)
    datas = []
    for (id,nome,senha,foto) in cursor:
        data = {}
        data['id'] = id 
        data['nome'] = nome 
        data['senha'] = senha 
        data['foto'] = foto 

        datas.append(data)



    return datas


    cursor.close()
    conexao.close()
        
        
      


if __name__ == "__main__":
    app.run(debug=True)