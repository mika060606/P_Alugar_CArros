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

        novo_usuario = User(id=1,name=name, sobrenome=sobrenome, email=email, numero_telefone=numero_telefone, senha=senha ,  cnf_senha=cnf_senha, termos=termos)
        
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            print("Usuario salvo com sucesso!")
        except Exception as e:
            db.session.rollback()
            print("Erro ao salvar:", e)

        return redirect('/login')


    return render_template('registrar.html')
         
