from flask import Flask,render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    isActive = db.Column(db.Boolean, default = True)


@app.route('/')
def index ():
    return render_template('index.html')


@app.route('/about')
def about ():
    return render_template('about.html')


@app.route('/create')
def create ():
    return render_template('create.html')


@app.route('/detail')
def detail ():
    return render_template('detail.html')


if __name__=='__main__':
    app.run(debug=True)