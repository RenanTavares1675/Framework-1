from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request
from flask import make_response


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/cad/usuario")
def usuario():
	return render_template('usuario.html', titulo="Cadastro de Usuário")

@app.route("/cad/caduser", methods=['POST'] )
def caduser():
	return request.form

@app.route("/cad/anuncio")
def anuncio():
	return render_template('anuncio.html')

@app.route("/anuncios/pergunta")
def pergunta():
	return render_template('pergunta.html')

@app.route("/anuncios/compra")
def compra():
	return ""

@app.route("/anuncio/favoritos")
def favoritos():
	print("favorito inserido")
	return "<h4>Comprado</h4>"

@app.route("/config/categoria")
def categoria():
	return render_template('categoria.html')

@app.route("/relatorios/vendas")
def relVendas():
	return render_template('relVendas.html')

@app.route("/relatorios/compras")
def relCompras():
	return render_template('relCompras.html')
