from flask import Flask, current_app
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

with app.app_context():
    print(current_app.name)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self) -> str:
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route("/")
def home():
    return "Hello, Flask"

@app. route('/books')
def get_books():

    return 