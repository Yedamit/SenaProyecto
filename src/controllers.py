from flask import render_template
from app import app


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/lista-usuarios")
def lista_usuarios():
    return render_template('lista-usuarios.html')

