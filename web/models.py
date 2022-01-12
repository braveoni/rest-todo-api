from . import db


class User(db.Model):
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(256), unique=False, nullable=False)
    todo_list = db.relationship('Todo', backref='user', lazy='dynamic')


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'))
    task_name = db.Column(db.String(128), nullable=False)
    task_status = db.Column(db.Boolean(), default=False, nullable=False)
