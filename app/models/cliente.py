from .database import conectar

class Cliente:
    """Registra contatos recebidos pelo formulário do site."""
    def __init__(self, nome, email, telefone, mensagem, veiculo_interesse='', veiculo_id=None):
        self.nome = nome.strip()
        self.email = email.strip().lower()
        self.telefone = telefone.strip()
        self.mensagem = mensagem.strip()
        self.veiculo_interesse = veiculo_interesse.strip()
        self.veiculo_id = int(veiculo_id) if veiculo_id else None

    def salvar(self, caminho):
        with conectar(caminho) as db:
            db.execute("INSERT INTO contatos (nome, email, telefone, mensagem, veiculo_interesse, veiculo_id) VALUES (?, ?, ?, ?, ?, ?)", (self.nome, self.email, self.telefone, self.mensagem, self.veiculo_interesse, self.veiculo_id))
