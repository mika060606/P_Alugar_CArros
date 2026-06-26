

from db import db   



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    numero_telefone = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.Text(500), nullable=False)

    termos = db.Column(db.Boolean, nullable=False)



    def __repr__(self):
        return f'<User {self.name}>'
    

class Carros(db.Model):
    __tablename__ = 'carros'

    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text(500), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    localizacao = db.Column(db.String(100), nullable=False)
    classificacao = db.Column(db.String(50), nullable=False)
    ativo = db.Column(db.Boolean, nullable=False, default=True)
    imagem = db.Column(db.String(200), nullable=True)



class Favoritos(db.Model):
    __tablename__ = 'favoritos'

    id = db.Column(db.Integer, primary_key=True)

    #cria as colunas para guardar os ids
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )

    carro_id = db.Column(
        db.Integer,
        db.ForeignKey('carros.id'),
        nullable=False
    )

    #ve se tem repetidos como (2,2 / 2,2)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'carro_id'),
    )