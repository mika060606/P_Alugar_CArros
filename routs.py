from flask import render_template,redirect,request
import db
from main import app
from models import User

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/Registrar', methods=['GET', 'POST'])
def cadastro():

    #inputs

    if request.method == 'POST':
        name = request.form['nome']
        sobrenome = request.form['sobrenome']
        email = request.form['email']
        numero_telefone = request.form['numero']
        senha = request.form['senha']
        cnf_senha = request.form['confirmar_senha']
        termos = request.form.get('termos') 

        novo_usuario = User(name=name, sobrenome=sobrenome, email=email, numero_telefone=numero_telefone, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect('/login')


    return render_template('registrar.html')
         
