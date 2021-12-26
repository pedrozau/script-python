from flask import Flask,render_template 
app = Flask('Project')
@app.route('/')
def ex():
    
    return render_template('index.html',frutas = {0:"banana",1:"manga",2:"maça"})

app.run()