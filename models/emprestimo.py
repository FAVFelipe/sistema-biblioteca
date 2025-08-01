import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.conexao import conectar  # ajuste para o seu caminho

def emprestimo_ja_existe(ra, codigo_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    query = """
    SELECT COUNT(*) FROM Emprestimos
    WHERE ra = ? AND codigo_livro = ?
    """
    cursor.execute(query, (ra, codigo_livro))
    resultado = cursor.fetchone()[0]
    conexao.close()

    return resultado > 0

#inserir empréstimo

from database.conexao import conectar

def criar_tabela_emprestimos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

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
        print("Tabela Emprestimos criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabela Emprestimos{e}")

if __name__ == "__main__":
    criar_tabela_emprestimos()

def inserir_emprestimo(ra, codigo_livro, data_retirada, data_entrega):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO Emprestimos (ra, codigo_livro, data_retirada, data_entrega)
        VALUES (?, ?, ?, ?)
    """, (ra, codigo_livro, data_retirada, data_entrega))

    conexao.commit()
    conexao.close()
