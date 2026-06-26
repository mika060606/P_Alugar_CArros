import re

from flask import render_template, redirect, request, flash, session
from sqlalchemy import or_
from db import db
from main import app
from models import Carros, Favoritos, User
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
            session['user_authenticated'] = True
            session['user_name'] = usuario.name
            flash("Login bem sucedido!", "success")
            return redirect('/index')
        else:
            flash("Email ou senha incorretos.", "error")
            return render_template('login.html', username=email)

    return render_template('login.html')


@app.route('/index')
def home():
    carros = Carros.query.filter_by(ativo=True).all()
    return render_template(
        'index.html',carros=carros,
        user_authenticated=session.get('user_authenticated', False),
        user_name=session.get('user_name')
    )


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')



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
            flash("As senhas não coincidem. Por favor, tente novamente.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)
        
        # Email
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'

        if not re.match(email_regex, email):
            flash("Email inválido.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        # Número de telefone
        if not numero_telefone.isdigit():
            flash("O número de telefone deve conter apenas números.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        if len(numero_telefone) < 9:
            flash("O número de telefone deve ter pelo menos 9 dígitos.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        # Força da senha
        if len(senha) < 8:
            flash("A senha deve ter pelo menos 8 caracteres.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        if not re.search(r'[A-Z]', senha):
            flash("A senha deve conter pelo menos uma letra maiúscula.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        if not re.search(r'[a-z]', senha):
            flash("A senha deve conter pelo menos uma letra minúscula.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        if not re.search(r'\d', senha):
            flash("A senha deve conter pelo menos um número.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

        # caractere especial
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
            flash("A senha deve conter pelo menos um caractere especial.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)



        
        #verificar email,numero

        usuario = User.query.filter(
        or_(User.email == email, User.numero_telefone == numero_telefone)
        ).first()
        
        if usuario:
            flash("Email ou número de telefone já estão em uso. Por favor, escolha outro.", "error")
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)
        
        #query
        senha_hash = generate_password_hash(senha)
        novo_usuario = User(name=name, sobrenome=sobrenome, email=email, numero_telefone=numero_telefone, senha=senha_hash , termos=termos)
        

        # fazer a query na bd
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            flash("Conta criada com sucesso!", "success")
            print("Usuario salvo com sucesso!")
            return redirect('/login')
        except Exception as e:
            db.session.rollback()
            flash("Erro ao conectar com a base de dados. Tente novamente.", "error")
            print("Erro ao salvar:", e)
            return render_template('registrar.html', nome=name, sobrenome=sobrenome, email=email, numero=numero_telefone)

    #Carregar a html

    return render_template('registrar.html')
         


#pega o id do carro
@app.route('/favorito/<int:carro_id>', methods=['POST'])
def favorito(carro_id):

    #ve na session que é iniciada e ve se ta logado
    if not session.get('user_authenticated'):
        flash("Você precisa estar logado para favoritar um carro.", "error")
        return redirect('/login')

    user_id = session.get('user_id')  
    
    #cria a instancia para ver se ja existe o favorito
    favorito_existente = Favoritos.query.filter_by(user_id=user_id, carro_id=carro_id).first()

    if favorito_existente:
        db.session.delete(favorito_existente)
        db.session.commit()
        flash("Carro removido dos favoritos.", "success")
    else:
        novo_favorito = Favoritos(user_id=user_id, carro_id=carro_id)
        db.session.add(novo_favorito)
        db.session.commit()
        flash("Carro adicionado aos favoritos.", "success")

    return redirect(request.referrer or '/index')