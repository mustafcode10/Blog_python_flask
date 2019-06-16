from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ada85258046a985819107971857c112d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////site.db'
db = SQLAlchemy(app)
from flaskblog import routes