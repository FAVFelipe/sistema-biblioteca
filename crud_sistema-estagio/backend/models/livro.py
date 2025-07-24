import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# inserir livro

from database.conexao import conectar

def criar_tabela_livros():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Livros' AND xtype='U')
        CREATE TABLE Livros (
            codigo INT PRIMARY KEY IDENTITY(1,1),
            titulo NVARCHAR(150),
            autor NVARCHAR(100),
            categoria NVARCHAR(100),
            editora NVARCHAR(100)
        )
    """)

        conexao.commit()
        cursor.close()
        conexao.close()
        print("Tabela Livros criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabela Livros: {e}")

if __name__ == "__main__":
    criar_tabela_livros()

def inserir_livro(titulo, autor, categoria, editora):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO Livros (titulo, autor, categoria, editora)
            VALUES (?, ?, ?, ?)
        """, (titulo, autor, categoria, editora))

        conexao.commit()
    finally:
        cursor.close()
        conexao.close()
