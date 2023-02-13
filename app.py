#M04 Lab
#Author: Joey Roberts
#Date: 2/12/2023
# Using Flask to manipulate database

#Imports
from flask import Flask, current_app
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

# attempting to get the interpreter to allow me to commit changes
with app.app_context():
    print(current_app.name)

# configuration file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

# Creates book table with column headers
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
# How the interpreter shows the database info
    def __repr__(self) -> str:
        return f"{self.book_name} - {self.author} - {self.publisher}"

# HTML home page of server    
@app.route("/")
def home():
    return "Hello, Flask"

@app. route('/books')
def get_books():

    return 
