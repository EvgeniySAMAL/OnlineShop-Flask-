from flask import Flask,render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY.DATABASE_URI']='sqlite///shop.db'

@app.route('/')
def index ():
    return render_template('index.html')


@app.route('/about')
def about ():
    return render_template('about.html')


@app.route('/detail')
def detail ():
    return render_template('detail.html')


if __name__=='__main__':
    app.run(debug=True)