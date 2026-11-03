# Elite Motors — Projeto Integrado

Sistema web de gerenciamento de veículos desenvolvido para o Projeto Integrado de DWS, POO e Banco de Dados. A estrutura original do site foi preservada: `css/`, `js/`, `pages/` e `index.html`. O back-end Flask foi acrescentado na pasta `app/`.

## Tecnologias
- Python 3.10+ e Flask
- Programação Orientada a Objetos (classes `Veiculo` e `Cliente`)
- SQLite com chaves primárias e estrangeiras
- HTML, CSS e JavaScript

## Estrutura
```text
Elite_Motors/
├── css/
│   └── style.css
├── js/
│   └── script.js
├── pages/
│   ├── pagina1.html
│   ├── pagina2.html
│   ├── sobre.html
│   ├── contato.html
│   ├── admin.html
│   └── veiculo_form.html
├── app/
│   ├── models/
│   └── routes/
├── database/
│   └── schema.sql
├── index.html
├── run.py
├── requirements.txt
└── .gitignore
```

## Como executar no Windows
1. Instale Python 3.10 ou superior.
2. Abra o terminal nesta pasta.
3. Crie e ative o ambiente virtual:
   ```powershell
   py -m venv .venv
   .venv\Scripts\activate
   ```
4. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
5. Inicie o sistema:
   ```powershell
   py run.py
   ```
6. Acesse `http://127.0.0.1:5000`. O SQLite e os veículos iniciais são criados automaticamente.

## Funcionalidades
- Página inicial com veículos em destaque carregados do banco.
- Catálogo com busca por marca ou modelo.
- Formulário de contato que grava mensagens no banco.
- Painel administrativo em `/admin` para cadastrar, editar e excluir veículos e consultar contatos.

## Banco de dados
O banco SQLite é criado em `database/elite_motors.db` na primeira execução. A estrutura está documentada em `database/schema.sql`. O arquivo `.db` não é enviado ao GitHub; ele será recriado automaticamente.

## GitHub e commits
Faça commits reais a cada parte desenvolvida, por exemplo:
```bash
git add .
git commit -m "Preserva estrutura original do site"
git push
```
Depois de implementar cada funcionalidade, registre uma nova atualização. Não crie commits artificiais retroativos.

## Colaborador
No GitHub, abra **Settings > Collaborators > Add people** e convide `leonardo.stephan@eaportal.org`.

## Observação acadêmica e segurança
O painel `/admin` está aberto nesta versão didática, sem autenticação. Não publique o sistema em produção sem implementar login, autorização e proteção adicional. Troque também a chave secreta em `app/__init__.py` antes de qualquer implantação pública.
