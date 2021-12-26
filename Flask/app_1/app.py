from flask import Flask, render_template,request,session

app = Flask("Projecto")
app.secret_key = "2001NGUIMBI01PEDRO01ZAU"
@app.route("/")
def ola_mundo():
    return render_template("index.html",my_name="Pedro",my_age=20),200

@app.route("/api/")
@app.route("/api/<key>/<token>")
def api(key=None,token=None):
    return  " Keys:{}  Token: {} ".format(key,token),200
@app.route("/mget/")
def mget():
    return render_template("Mget.html"),200
@app.route("/mpost/")
def mpost():
    return render_template("Mpost.html"),200
@app.route("/receber/",methods=['GET','POST'])
def recebe():
    if request.method == "GET":
        #return "Name is {} and Age {} ".format(request.args.get('name'),request.args.get('age')),200
        
        return render_template("recebe.html",name=request.args.get('name'),age=2021-int(request.args.get('age'))),200
    elif request.method == "POST":
        return "Your name is {} and Your age {} ".format(request.form['name'],request.form['age']),200
         
        # return render_template("recebe.html",name= resquest.form['name'],age= request.form['age']),200
    else:
        return "Não definido",200
@app.route("/session/")
def sess():
    return "session start"

app.run()

