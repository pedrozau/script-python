from flask import Flask, render_template 

app = Flask("Project")

@app.route("/")

def olamundo():
    return render_template('index.html',name="Marcos"),200
   
app.run()