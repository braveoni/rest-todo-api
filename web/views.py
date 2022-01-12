from flask import json
from flask.json import jsonify
from . import app, db, auth
from .models import User, Todo
from flask import request
from werkzeug.security import generate_password_hash


def success():
    return jsonify(status='Success')


def fail():
    return jsonify(status='Fail')



@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())


@app.route('/user/', methods=['POST'])
def user():
    if request.method == 'POST':
        db.session.add(User(username=request.form['username'], password=generate_password_hash(request.form['password'])))
        db.session.commit()

        return success()
    
    return fail()


@app.route('/todo/', methods=['GET', 'POST'])
@app.route('/todo/<int:task_id>/', methods=['PUT', 'DELETE'])
@auth.login_required
def todo_list(task_id=None):
    if request.method == 'GET':
        data = db.session.query(Todo).filter_by(username=auth.current_user()).all()
        return jsonify(tuple({key: value for key, value in zip(['id', 'task_name', 'task_status'], [row.id, row.task_name, row.task_status])} for row in data))

    if request.method == 'POST':
        db.session.add(Todo(username=auth.current_user(), task_name=request.form['task_name']))
        db.session.commit()
        return success()
    
    if request.method == 'PUT':
        if task_id:
            print(request.form)
            record = db.session.query(Todo).filter_by(username=auth.current_user(), id=task_id).first()
            record.task_status = request.form['task_status']  == 'True'
            db.session.commit()
            return success()
        
        return fail()

    if request.method == 'DELETE':
        if task_id:
            db.session.query(Todo).filter_by(username=auth.current_user(), id=task_id).delete()
            db.session.commit()
            return success()
        
        return fail()
