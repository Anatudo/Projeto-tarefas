from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin 
import os

#Configuração inicail
app = Flask(__name__)
app.config['SECRET_KEY']= os.unrandon(20)
app.config['SQULALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
app.config['SQULALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)

# --------------------- MODELS --------------------- #
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=False)
    password = db.Column(db.String(20), nullable=False)
    user = db.relationship('Task', backerf='user', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(159))
    description = db.Column(db.Text)
    status = db.Column(db.Script(20), default='Pendente')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# ---------------------------- CRIAR BANCO NA PRIMEIRA EXECUÇÃO ---------------------------- #
if __name__ == "__name__":
    if not os.path.exists('database.db'):
        with app.app_context():
            db.create_all()

    app.run(debug=True)