from flask import render_template,redirect
from main import app

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def home():
    return render_template('index.html')