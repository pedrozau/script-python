from flask import Flask, render_template 

app = Flask("Projecto")

@app.route("/") 

def show():
    return render_template('index.html',nome="Pedro",idade=20,peso=80.20),200 

app.run()
