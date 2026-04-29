from flask import Flask, config, render_template
from db import db

import os



app = Flask(__name__, static_folder='Imagens', static_url_path='/Imagens')



app.config['SQLALCHEMY_DATABASE_URI']="postgresql://aluguel_carros_user:Q4ud9pshTLuXzXIEsZtPjeFibpZ2QIam@dpg-d7nih4cvikkc73b9o8n0-a.oregon-postgres.render.com/aluguel_carros"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "connect_args": {"sslmode": "require"}
}



from models import User

with app.app_context():
    db.create_all()

from routs import *

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)