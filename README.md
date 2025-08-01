Inicializar o projeto passo-a-passo (via web):
1. Abra o banco de dados SSMS;
2. Teste a conexão com o banco de dados;
3. Execute no SSMS: USE BibliotecaDB;
GO
SELECT name FROM sys.tables;
4. Crie e insira os dados nas tabelas Alunos e Livros em gui;
5. No cmd, vá ao dir do projeto -> cd C:\Users\lipef\OneDrive\Área de Trabalho\TEC\crud_sistema-estagio\backend;
6. Rode "ngrok http 5000" no cmd;
7. Copie e cole o link gerado no index.html;
8. Rode o app.py;
9. Abra o navegador e acesse o link gerado no index.html;
10. Salve o projeto, crie um novo projeto no netlify e cadastre o emprestimo.

Encerrar projeto CRUD
1. CTRL + C no cmd e terminal para encerrar o debug;
2. Salvar o projeto e fechar.

Comando para zerar tabela de empréstimos no SSMS:
DELETE FROM Emprestimos;
DBCC CHECKIDENT ('Emprestimos', RESEED, 0);