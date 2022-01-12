from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_object('web.config.Config')
auth = HTTPBasicAuth()
db = SQLAlchemy(app)

from . import views


from web.models import User

@auth.verify_password
def verify_password(username, password):
    user = db.session.query(User).filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        return username