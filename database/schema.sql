CREATE TABLE IF NOT EXISTS veiculos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    ano INTEGER NOT NULL CHECK (ano >= 1900),
    quilometragem INTEGER NOT NULL DEFAULT 0 CHECK (quilometragem >= 0),
    preco REAL NOT NULL CHECK (preco >= 0),
    cambio TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Disponível',
    imagem TEXT,
    descricao TEXT,
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT,
    mensagem TEXT NOT NULL,
    veiculo_interesse TEXT,
    veiculo_id INTEGER REFERENCES veiculos(id) ON DELETE SET NULL,
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
