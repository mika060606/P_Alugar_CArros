from flask import render_template,redirect,request
from sqlalchemy import or_
from db import db
from main import app
from models import User
from werkzeug.security import generate_password_hash   


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
        if termos == 'on':
            termos = True
        else:
            termos = False
        

        #verificar email,numero

        usuario = User.query.filter(
        or_(User.email == email, User.numero_telefone == numero_telefone)
        ).first()
        
        if usuario:
            return "Email ou número de telefone já estão em uso. Por favor, escolha outro."
        
        #query
        senha_hash = generate_password_hash(senha)
        novo_usuario = User(name=name, sobrenome=sobrenome, email=email, numero_telefone=numero_telefone, senha=senha_hash ,  cnf_senha=cnf_senha, termos=termos)
        

        # fazer a query na bd
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            print("Usuario salvo com sucesso!")
        except Exception as e:
            db.session.rollback()
            print("Erro ao salvar:", e)

        return redirect('/login')

    #Carregar a html

    return render_template('registrar.html')
         
