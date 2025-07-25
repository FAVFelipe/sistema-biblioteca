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


# Executar o Projeto via Navegador (HTML + Flask + ngrok)

**Passo a Passo:**

- Abra o banco de dados no SQL Server Management Studio (SSMS).

- Teste a conexão com o banco de dados, garantindo que o BibliotecaDB esteja acessível.

- No SSMS, execute:

USE BibliotecaDB;

GO

SELECT name FROM sys.tables;

Isso garante que as tabelas foram criadas corretamente.

- Insira registros nas tabelas Alunos e Livros usando a interface gráfica Tkinter (opcional, mas recomendado).

- No terminal (cmd ou PowerShell), navegue até o diretório do backend:

cd "cd caminho/para/o/projeto/backend"


- Inicie o túnel com o ngrok:

ngrok http 5000


- Copie o link gerado pelo ngrok, algo como:

https://xxxxxx.ngrok-free.app


- Cole esse link no seu index.html, substituindo o endereço antigo no trecho:

fetch("https://xxxxxx.ngrok-free.app/emprestimo", {


- Execute o backend Flask:

python app.py


- Abra o index.html no navegador e preencha o formulário de empréstimo normalmente.
  

- (Opcional) Suba seu frontend no Netlify ou similar, colando o link do ngrok no HTML antes do deploy.
  

# Encerrando o Projeto
Pressione CTRL + C no terminal para encerrar o Flask e o ngrok.

Salve as alterações no código.

Feche o editor e o navegador.
