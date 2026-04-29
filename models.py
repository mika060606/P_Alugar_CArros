

from db import db   



class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    numero_telefone = db.Column(db.int(10), nullable=False)
    senha = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<User {self.name}>'