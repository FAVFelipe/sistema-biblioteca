# criar_tabelas.py
from database.conexao import conectar

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # Remoção segura (ordem: filho → pai)
    cursor.execute("IF OBJECT_ID('Emprestimos', 'U') IS NOT NULL DROP TABLE Emprestimos;")
    cursor.execute("IF OBJECT_ID('Livros', 'U') IS NOT NULL DROP TABLE Livros;")
    cursor.execute("IF OBJECT_ID('Alunos', 'U') IS NOT NULL DROP TABLE Alunos;")

    # Criar tabela Alunos
    cursor.execute("""
    CREATE TABLE Alunos (
        ra INT PRIMARY KEY,
        nome NVARCHAR(100),
        email NVARCHAR(100),
        telefone NVARCHAR(20),
        data_nascimento DATE
    )
    """)

    # Criar tabela Livros
    cursor.execute("""
    CREATE TABLE Livros (
        codigo INT PRIMARY KEY IDENTITY(1,1),
        titulo NVARCHAR(150),
        autor NVARCHAR(100),
        categoria NVARCHAR(100),
        editora NVARCHAR(100)
    )
    """)

    # Criar tabela Emprestimos com FKs
    cursor.execute("""IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Emprestimos' AND xtype='U')
BEGIN
    CREATE TABLE Emprestimos (
        codigo INT PRIMARY KEY IDENTITY(1,1),
        ra INT NOT NULL,
        codigo_livro INT NOT NULL,
        data_retirada DATE,
        data_entrega DATE,
        FOREIGN KEY (ra) REFERENCES Alunos(ra),
        FOREIGN KEY (codigo_livro) REFERENCES Livros(codigo)
    );
END
""")

    conexao.commit()
    cursor.close()
    conexao.close()
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    criar_tabelas()