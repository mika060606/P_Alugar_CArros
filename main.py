from flask import Flask
from db import db

import os



# config do flask
app = Flask(__name__, static_folder='Imagens', static_url_path='/Imagens')

app.config['SQLALCHEMY_DATABASE_URI']="postgresql://aluguel_carros_e894_user:xmELj51Wgkt7UQO7xavslicoYXEWu8SX@dpg-d8p7h7gk1i2s73ev1240-a/aluguel_carros_e894"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {"sslmode": "require"}
}

#atualizar db
db.init_app(app)

from models import User

with app.app_context():
    db.create_all()

from routs import *

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)