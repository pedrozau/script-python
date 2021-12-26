from flask import Flask,render_template,url_for, request,jsonify,redirect 
import mysql.connector 
import bcrypt 
app = Flask(__name__) 


@app.route('/')
def index():
    return render_template('login.html'),200

@app.route('/auth',methods=['POST'])
def login():
    connection = mysql.connector.connect(user="root",password='',host='127.0.0.1',database='login')
    cursor = connection.cursor() 
    result = ("SELECT * FROM login  ")
    cursor.execute(result) 
    if request.method == "POST":
        user_name = request.form['user']
        password = request.form['password']
        new_pass = b'{}'.format(password)
        for (id,user,senha) in cursor:
            if user_name == user:
                if bcrypt.checkpw(new_pass,senha):
                    redirect(url_for('checks'))
                else:
                    redirect(url_for('index'))
            else:
                redirect(url_for('index'))
        

        
        
        
    

    return "check login"
                    
@app.route('/check')
def checks():

    return render_template('check.html',data=db())

        
def db():

    connection = mysql.connector.connect(user="root",password='',host='127.0.0.1',database='login')
   
    cursor = connection.cursor() 
    result = ("SELECT * FROM login  ")
    cursor.execute(result) 
    data = []
    for (id,user,senha) in cursor:
        datas = {}
        datas['id'] = id
        datas['user'] = user
        datas['senha'] = senha

        data.append(datas)
    

    return data 





if __name__ == "__main__":
    app.run(debug=True)