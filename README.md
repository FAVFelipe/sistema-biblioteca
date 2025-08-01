## Sistema de Biblioteca - CRUD com Flask, SQL Server, Tkinter e Web

Este projeto é um sistema simples de biblioteca que permite cadastrar, listar e gerenciar alunos, livros e empréstimos. Ele foi desenvolvido como parte de um processo seletivo para estágio na área de desenvolvimento de sistemas.  



**Funcionalidades:**

Cadastro de Alunos, Livros e Empréstimos

Interface gráfica (Tkinter)

Interface web (HTML + JavaScript)

API em Flask (backend)

Conexão com banco de dados SQL Server

Validações de entrada

Prevenção de empréstimos duplicados


**Tecnologias Utilizadas:**

Python 3.10+

Flask (API REST)

Tkinter (interface local)

HTML + JS (fetch) (interface web)

SQL Server Express (banco de dados local)

Ngrok (expor servidor local para a web)

Validações Implementadas


**Front-end:**

Todos os campos obrigatórios

Tipagem correta dos dados (números, datas)

Envio via fetch com JSON


**Back-end:**

Conversão segura de datas para o formato dd/mm/yyyy

Verificação se a data de retirada é anterior à data de entrega

Verificação de empréstimo duplicado (mesmo RA e código do livro)

Mensagens de erro claras via try/except


**Estrutura do Projeto**

crud_sistema-estagio/
│

├── backend/
│   ├── app.py                
│   └── models/
│       └── emprestimo.py     
│
├── gui.py 

├── frontend/
├── index.html   

└── README.md                 
