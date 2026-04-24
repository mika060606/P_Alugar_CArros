from flask import Flask, render_template
import os

app = Flask(__name__, static_folder='Imagens', static_url_path='/Imagens')

from routs import *

if __name__ == '__main__':
    app.run(debug=True)