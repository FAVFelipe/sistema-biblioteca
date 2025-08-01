📚 Sistema de Cadastro de Empréstimos (CRUD)

Este projeto é um sistema de gerenciamento de empréstimos de livros, com cadastro de alunos, livros e controle de empréstimos, utilizando Python + SQL Server. Disponível tanto com interface web (HTML + Flask) quanto desktop (Tkinter).

🚀 Tecnologias Utilizadas

Python 3

Flask

Tkinter (GUI)

HTML/CSS

SQL Server Express

Ngrok (exposição do servidor local)

Netlify (hospedagem front-end)

🔧 Configuração e Execução

📌 Pré-requisitos

Python instalado

SQL Server Express + SSMS

Ngrok

Netlify (opcional para hospedagem do front-end)

🌐 Modo Web (Flask + HTML)

1. Inicializar o banco de dados

Abra o SQL Server Management Studio (SSMS).

Conecte ao servidor local.

Execute:
USE BibliotecaDB;
GO
SELECT name FROM sys.tables;

Certifique-se de que as tabelas Alunos, Livros e Emprestimos existem.

Insira dados de exemplo nas tabelas Alunos e Livros (via GUI ou SSMS).

2. Executar o servidor Flask

No terminal/cmd:
cd C:\Users\seudiretoriodoprojeto/

3. Expor localmente com Ngrok

Em outro terminal:
ngrok http 5000

Copie o link HTTPS gerado (ex: https://xxxxx.ngrok-free.app) e cole no fetch() do seu index.html.

4. Executar o front-end

Abra o index.html no navegador (ou hospede no Netlify).

Preencha os campos e envie o formulário para cadastrar um empréstimo.

🖥️ Modo Desktop (Tkinter)

Passos:
Execute o script Python com GUI (por exemplo: emprestimo_gui.py):
python emprestimo_gui.py

A interface permite:

Cadastro de empréstimos com campos validados.

Visualização de empréstimos existentes (lista).

Validações: campos obrigatórios, lógica de datas, duplicidade.

🧹 Limpar a Tabela de Empréstimos (para testes)

No SSMS, execute:
DELETE FROM Emprestimos;
DBCC CHECKIDENT ('Emprestimos', RESEED, 0);

🛑 Encerrar o Projeto

No terminal: CTRL + C para encerrar app.py e ngrok.

Salve alterações e feche o projeto.

✅ Funcionalidades e Validações

Cadastro, listagem e validação de empréstimos.

Verificação de:

Campos obrigatórios

Formatos de data

Datas inconsistentes (ex: retirada após entrega)

Duplicidade de RA + Código do Livro

Interface Web e Tkinter disponíveis.
