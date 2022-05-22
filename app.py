from distutils.log import debug
from email.policy import default
import json
from operator import mod
from pickle import GET
from pyexpat import model
from turtle import title
from urllib import response
from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

from sqlalchemy import JSON, desc, false, null

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=Flask)
    desc = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['POST'])
def hello_world():

    if request.method == 'POST':
        title = request.form['todoTitle']
        desc = request.form['todoDesc']

        todo = Todo(title=title , desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodo = Todo.query.all()

    return render_template('index.html', allTodo=allTodo)

@app.route('/addtodo', methods=['GET', 'POST'])
def addNewTodo():

    try:
        reJ = request.form
        title = reJ['title']
        desc = reJ['desc']

        todo = Todo(title=title , desc=desc)
        db.session.add(todo)
        db.session.commit()

        return jsonify({"response " : "success"})
    except Exception:
        return jsonify({"response " : "error"}) 

@app.route('/update')
def update():

    return "This is update page"

@app.route('/delete/<int:sno>')
def deleteFunction(sno):
    try:
        todo = Todo.query.filter_by(sno=sno).first()
        db.session.delete(todo)
        db.session.commit()
        return jsonify({"response" : "success"})

    except Exception:
        return jsonify({"response " : "error"})

class allTodoSchema(ma.Schema):
    class Meta:
        fields = ("sno", "title", "desc" , "date")

class TodoSchema(ma.Schema):
    class Meta:

        fields = ("sno", "title", "desc" , "date")

@app.route('/showalltodo', methods = ['GET'])
def showAllData():

    allTodo = Todo.query.all()

    todoSchema = allTodoSchema(many=True)
    output = todoSchema.dump(allTodo)

    return jsonify({'allTodo ' : output})

@app.route('/showtodo/<int:sno>', methods = ['GET'])
def showTodo(sno):

    singleTodo = Todo.query.filter_by(sno=sno).first()
    todoSchema = allTodoSchema()
    output = todoSchema.dump(singleTodo)

    return jsonify({'allTodo ' : output})    

@app.route('/learnpost', methods=['GET','POST'])
def learnpost():

    try:
        reJ = request.form
        name = reJ['name'] 
        return jsonify({"response " : "success"})
    except Exception:
        return jsonify({"response " : "error"}) 


if __name__ == "__main__":
    app.run(debug=True) 