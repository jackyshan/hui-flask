# -*- coding: UTF-8 -*- 

from flask import Flask, render_template, redirect, url_for, request
from models import Zixun
from database import db_session

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

@app.route('/article_add', methods=["GET", "POST"])
def article_add():
    if request.method == 'POST':
        print '---------->>>>hello'
        title = request.form['articletitle']
        category = request.form['selectcategory']
        source = request.form['sources']
        update_time = request.form['commentdatemin']

        zixun = Zixun(title, category, source, update_time)
        db_session.add(zixun)
        db_session.commit()
        print '数据保存成功'
        
        return ''
    return render_template('article-add.html')    


if __name__ == '__main__':
    app.run(debug=True)