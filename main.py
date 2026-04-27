from flask import Flask, config, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = config['SQLALCHEMY_DATABASE_URI']="postgresql://aluguel_carros_user:Q4ud9pshTLuXzXIEsZtPjeFibpZ2QIam@dpg-d7nih4cvikkc73b9o8n0-a/aluguel_carros"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {"sslmode": "require"}
}

app = Flask(__name__, static_folder='Imagens', static_url_path='/Imagens')

from routs import *

if __name__ == '__main__':
    app.run(debug=True)