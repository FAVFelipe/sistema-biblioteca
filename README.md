# Sistema de Biblioteca - Projeto Teste

Este é um sistema simples de gerenciamento de biblioteca desenvolvido como parte de um **Projeto Teste de Processo Seletivo**. O objetivo principal é demonstrar domínio em desenvolvimento backend e frontend, incluindo **CRUD de Alunos, Livros e Empréstimos**, modelagem de dados, validações e boas práticas.

## Objetivos do Projeto

O projeto consiste em:

1. **Cadastro de Aluno**
   - Campos: RA, Nome, Email, Telefone, Data de Nascimento

2. **Cadastro de Livros**
   - Campos: Código, Título, Autor, Categoria, Editora

3. **Cadastro de Empréstimos**
   - Campos: Código, RA, Código do Livro, Data de Retirada, Data de Entrega

4. **Funcionalidades Livres**
   - Integração web com HTML/CSS simples
   - Integração via API com Flask
   - Formatação de datas em padrão brasileiro
   - Validação de entrada no frontend e tratamento de erros no backend

## Tecnologias Utilizadas

### Backend
- Python 3.x
- Flask
- pyodbc (para conexão com SQL Server)
- SQL Server Express
- Ngrok (para disponibilizar API local via HTTPS)

### Frontend
- HTML5 + CSS3 básico
- JavaScript puro (`fetch`, manipulação DOM)
- Hospedagem via Netlify

## Modelagem de Dados

### Alunos
| Campo            | Tipo        |
|------------------|-------------|
| RA               | INT (PK)    |
| Nome             | VARCHAR     |
| Email            | VARCHAR     |
| Telefone         | VARCHAR     |
| DataNascimento   | DATE        |

### Livros
| Campo            | Tipo        |
|------------------|-------------|
| Código           | INT (PK)    |
| Título           | VARCHAR     |
| Autor            | VARCHAR     |
| Categoria        | VARCHAR     |
| Editora          | VARCHAR     |

### Empréstimos
| Campo            | Tipo        |
|------------------|-------------|
| Código           | INT (PK)    |
| RA               | INT (FK)    |
| Código do Livro  | INT (FK)    |
| Data Retirada    | DATE        |
| Data Entrega     | DATE        |


## 🚀 Como executar localmente

1. Clone o repositório ou baixe os arquivos
2. Execute o servidor Flask:
   ```bash
   python app.py
