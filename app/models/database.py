import sqlite3
from pathlib import Path


def conectar(caminho):
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)
    conexao = sqlite3.connect(caminho)
    conexao.row_factory = sqlite3.Row
    conexao.execute('PRAGMA foreign_keys = ON')
    return conexao


def inicializar_banco(caminho):
    with conectar(caminho) as db:
        db.executescript(Path(__file__).resolve().parents[2].joinpath('database', 'schema.sql').read_text(encoding='utf-8'))
        total = db.execute('SELECT COUNT(*) FROM veiculos').fetchone()[0]
        if total == 0:
            exemplos = [
                ('Porsche', '911 Carrera', 2022, 8500, 899900, 'Automático', 'Disponível', 'https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1000&q=85', 'Esportivo premium em excelente estado.'),
                ('BMW', 'M4 Competition', 2023, 5200, 789900, 'Automático', 'Disponível', 'https://images.unsplash.com/photo-1555215695-3004980ad54e?auto=format&fit=crop&w=1000&q=85', 'Performance e sofisticação.'),
                ('Lamborghini', 'Huracán', 2021, 9100, 2490000, 'Automático', 'Disponível', 'https://images.unsplash.com/photo-1544636331-e26879cd4d9b?auto=format&fit=crop&w=1000&q=85', 'Superesportivo de presença marcante.'),
                ('Audi', 'R8', 2019, 18000, 1050000, 'Automático', 'Disponível', 'https://images.unsplash.com/photo-1504215680853-026ed2a45def?auto=format&fit=crop&w=1000&q=85', 'Design e desempenho em um só veículo.')]
            db.executemany("INSERT INTO veiculos (marca, modelo, ano, quilometragem, preco, cambio, status, imagem, descricao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", exemplos)
