from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from ..models.cliente import Cliente

contato_bp = Blueprint('contato', __name__)

@contato_bp.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        mensagem = request.form.get('mensagem', '').strip()
        if not nome or not email or not mensagem:
            flash('Preencha nome, e-mail e mensagem.', 'error')
        else:
            veiculo_id = request.form.get('veiculo_id') or None
            try:
                veiculo_id = int(veiculo_id) if veiculo_id else None
            except ValueError:
                veiculo_id = None
            cliente = Cliente(nome, email, request.form.get('telefone', ''), mensagem, request.form.get('veiculo_interesse', ''), veiculo_id)
            cliente.salvar(current_app.config['DATABASE'])
            flash('Mensagem enviada! Nossa equipe entrará em contato.', 'success')
            return redirect(url_for('contato.contato'))
    return render_template('pages/contato.html')
