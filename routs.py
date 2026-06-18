import re

from flask import render_template,redirect,request
from sqlalchemy import or_
from db import db
from main import app
from models import User
from werkzeug.security import check_password_hash, generate_password_hash   


@app.route('/')
def index():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['username']
        senha = request.form['password']

        usuario = User.query.filter(User.email == email).first()

        if usuario and check_password_hash(usuario.senha, senha):
            return redirect('/index')
        else:
            return "Email ou senha incorretos."

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
        

        #confirmar senha

        if (senha != cnf_senha):
            return "As senhas não coincidem. Por favor, tente novamente."
        
        # Email
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

        if not re.match(email_regex, email):
            return "Email inválido."

        # Número de telefone
        if not numero_telefone.isdigit():
            return "O número de telefone deve conter apenas números."

        if len(numero_telefone) < 9:
            return "O número de telefone deve ter pelo menos 9 dígitos."



        # Força da senha
        if len(senha) < 8:
            return "A senha deve ter pelo menos 8 caracteres."

        if not re.search(r'[A-Z]', senha):
            return "A senha deve conter pelo menos uma letra maiúscula."

        if not re.search(r'[a-z]', senha):
            return "A senha deve conter pelo menos uma letra minúscula."

        if not re.search(r'\d', senha):
            return "A senha deve conter pelo menos um número."

        # caractere especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            return "A senha deve conter pelo menos um caractere especial."



        
        #verificar email,numero

        usuario = User.query.filter(
        or_(User.email == email, User.numero_telefone == numero_telefone)
        ).first()
        
        if usuario:
            return "Email ou número de telefone já estão em uso. Por favor, escolha outro."
        
        #query
        senha_hash = generate_password_hash(senha)
        novo_usuario = User(name=name, sobrenome=sobrenome, email=email, numero_telefone=numero_telefone, senha=senha_hash , termos=termos)
        

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
         
