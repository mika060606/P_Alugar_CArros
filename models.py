

from db import db   



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500), nullable=False)
    sobrenome = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(500), unique=True, nullable=False)
    numero_telefone = db.Column(db.String(15), nullable=False)
    senha = db.Column(db.String(500), nullable=False)
    cnf_senha = db.Column(db.String(500), nullable=False)
    termos = db.Column(db.Boolean, nullable=False)


    def __repr__(self):
        return f'<User {self.name}>'