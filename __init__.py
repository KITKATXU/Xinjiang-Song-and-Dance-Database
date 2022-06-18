# -*- coding: utf-8 -*-
import os
# import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#from mypassword import pwd


pwd='qaz011211'
app = Flask(__name__,static_folder='static')

user1 = 'root'
database = 'xinjiang'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@127.0.0.1:3306/%s' % (user1, pwd, database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    from watchlist.models import User
    user = User.query.get(int(user_id))
    return user


login_manager.login_view = 'login'
login_manager.login_message = 'Your custom message'


@app.context_processor
def inject_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(user=user)



from watchlist import views, errors, commands