from flask import Flask, render_template, redirect, url_for, request
from models import Zixun

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':

        # Check the password and log the user in
        # [...]

        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/article-list')
def article_list():
    zixuns = Zixun.query.all()
    return render_template('article-list.html', zixuns = zixuns)

@app.route('/article_add')
def article_add():
    return render_template('article-add.html')    


if __name__ == '__main__':
    app.run()