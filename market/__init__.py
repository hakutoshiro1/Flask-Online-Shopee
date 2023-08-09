from flask import Flask, render_template  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b40873395f84ad5f6b424f67'
db=SQLAlchemy(app)
app.app_context().push()

from market import routes