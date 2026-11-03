from .database import conectar

class Veiculo:
    """Representa um veículo do estoque da Elite Motors."""
    def __init__(self, marca, modelo, ano, quilometragem, preco, cambio, status='Disponível', imagem='', descricao='', id=None):
        self.id = id
        self.marca = marca.strip()
        self.modelo = modelo.strip()
        self.ano = int(ano)
        self.quilometragem = int(quilometragem)
        self.preco = float(preco)
        self.cambio = cambio
        self.status = status
        self.imagem = imagem.strip()
        self.descricao = descricao.strip()

    @classmethod
    def _from_row(cls, row):
        dados = dict(row)
        campos = ('id', 'marca', 'modelo', 'ano', 'quilometragem', 'preco', 'cambio', 'status', 'imagem', 'descricao')
        return cls(**{campo: dados[campo] for campo in campos})

    @classmethod
    def todos(cls, caminho, busca=''):
        with conectar(caminho) as db:
            if busca:
                termo = f'%{busca}%'
                rows = db.execute('SELECT * FROM veiculos WHERE marca LIKE ? OR modelo LIKE ? ORDER BY id DESC', (termo, termo)).fetchall()
            else:
                rows = db.execute('SELECT * FROM veiculos ORDER BY id DESC').fetchall()
        return [cls._from_row(r) for r in rows]

    @classmethod
    def buscar_por_id(cls, caminho, veiculo_id):
        with conectar(caminho) as db:
            row = db.execute('SELECT * FROM veiculos WHERE id = ?', (veiculo_id,)).fetchone()
        return cls._from_row(row) if row else None

    def salvar(self, caminho):
        dados = (self.marca, self.modelo, self.ano, self.quilometragem, self.preco, self.cambio, self.status, self.imagem, self.descricao)
        with conectar(caminho) as db:
            if self.id:
                db.execute("UPDATE veiculos SET marca=?, modelo=?, ano=?, quilometragem=?, preco=?, cambio=?, status=?, imagem=?, descricao=? WHERE id=?", (*dados, self.id))
            else:
                cursor = db.execute("INSERT INTO veiculos (marca, modelo, ano, quilometragem, preco, cambio, status, imagem, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", dados)
                self.id = cursor.lastrowid
        return self

    @staticmethod
    def excluir(caminho, veiculo_id):
        with conectar(caminho) as db:
            db.execute('DELETE FROM veiculos WHERE id = ?', (veiculo_id,))
