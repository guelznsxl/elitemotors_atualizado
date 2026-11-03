from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from ..models.database import conectar
from ..models.veiculo import Veiculo

admin_bp = Blueprint('admin', __name__)

@admin_bp.get('/')
def painel():
    caminho = current_app.config['DATABASE']
    veiculos = Veiculo.todos(caminho)
    with conectar(caminho) as db:
        contatos = db.execute('SELECT contatos.*, veiculos.marca AS marca_veiculo, veiculos.modelo AS modelo_veiculo FROM contatos LEFT JOIN veiculos ON contatos.veiculo_id = veiculos.id ORDER BY contatos.criado_em DESC LIMIT 8').fetchall()
        total_contatos = db.execute('SELECT COUNT(*) FROM contatos').fetchone()[0]
    return render_template('pages/admin.html', veiculos=veiculos, contatos=contatos, total_contatos=total_contatos)

@admin_bp.route('/veiculo/novo', methods=['GET', 'POST'])
def novo_veiculo():
    if request.method == 'POST':
        try:
            veiculo = Veiculo(request.form['marca'], request.form['modelo'], request.form['ano'], request.form['quilometragem'], request.form['preco'], request.form['cambio'], request.form['status'], request.form.get('imagem', ''), request.form.get('descricao', ''))
            veiculo.salvar(current_app.config['DATABASE'])
            flash('Veículo cadastrado com sucesso!', 'success')
            return redirect(url_for('admin.painel'))
        except (ValueError, KeyError):
            flash('Confira os campos numéricos e tente novamente.', 'error')
    return render_template('pages/veiculo_form.html', veiculo=None)

@admin_bp.route('/veiculo/<int:veiculo_id>/editar', methods=['GET', 'POST'])
def editar_veiculo(veiculo_id):
    caminho = current_app.config['DATABASE']
    veiculo = Veiculo.buscar_por_id(caminho, veiculo_id)
    if not veiculo:
        flash('Veículo não encontrado.', 'error')
        return redirect(url_for('admin.painel'))
    if request.method == 'POST':
        try:
            atualizado = Veiculo(request.form['marca'], request.form['modelo'], request.form['ano'], request.form['quilometragem'], request.form['preco'], request.form['cambio'], request.form['status'], request.form.get('imagem', ''), request.form.get('descricao', ''), id=veiculo_id)
            atualizado.salvar(caminho)
            flash('Veículo atualizado!', 'success')
            return redirect(url_for('admin.painel'))
        except (ValueError, KeyError):
            flash('Confira os campos e tente novamente.', 'error')
    return render_template('pages/veiculo_form.html', veiculo=veiculo)

@admin_bp.post('/veiculo/<int:veiculo_id>/excluir')
def excluir_veiculo(veiculo_id):
    Veiculo.excluir(current_app.config['DATABASE'], veiculo_id)
    flash('Veículo excluído.', 'success')
    return redirect(url_for('admin.painel'))
