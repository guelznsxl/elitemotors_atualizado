from flask import Blueprint, current_app, render_template, request
from ..models.veiculo import Veiculo

main_bp = Blueprint('main', __name__)

@main_bp.get('/')
def inicio():
    veiculos = Veiculo.todos(current_app.config['DATABASE'])[:3]
    return render_template('index.html', veiculos=veiculos)

@main_bp.get('/carros')
def carros():
    busca = request.args.get('q', '').strip()
    veiculos = Veiculo.todos(current_app.config['DATABASE'], busca)
    return render_template('pages/pagina1.html', veiculos=veiculos, busca=busca)

@main_bp.get('/ofertas')
def ofertas():
    return render_template('pages/pagina2.html')

@main_bp.get('/sobre')
def sobre():
    return render_template('pages/sobre.html')
