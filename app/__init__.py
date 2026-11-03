from flask import Flask, send_from_directory
from pathlib import Path
from .routes.main import main_bp
from .routes.admin import admin_bp
from .routes.contato import contato_bp
from .models.database import inicializar_banco

ROOT = Path(__file__).resolve().parent.parent

def create_app():
    # Os templates ficam na raiz (index.html) e em pages/, preservando
    # a estrutura original do site. CSS e JS continuam nas pastas originais.
    app = Flask(__name__, template_folder=str(ROOT), static_folder=None)
    app.config['SECRET_KEY'] = 'elite-motors-chave-local-altere-antes-de-publicar'
    app.config['DATABASE'] = str(ROOT / 'database' / 'elite_motors.db')
    inicializar_banco(app.config['DATABASE'])

    def moeda(valor):
        texto = f'{valor:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'R$ {texto}'
    app.jinja_env.filters['moeda'] = moeda

    @app.get('/css/<path:filename>')
    def arquivo_css(filename):
        return send_from_directory(ROOT / 'css', filename)
    @app.get('/js/<path:filename>')
    def arquivo_js(filename):
        return send_from_directory(ROOT / 'js', filename)

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(contato_bp)
    return app
