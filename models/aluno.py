import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from database.conexao import conectar

def criar_tabela_aluno():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Alunos' AND xtype='U')
    CREATE TABLE Alunos (
        ra INT PRIMARY KEY,
        nome NVARCHAR(100),
        email NVARCHAR(100),
        telefone NVARCHAR(20),
        data_nascimento DATE
        )
    """)

        conexao.commit()
        cursor.close()
        conexao.close()
        print("Tabela Alunos criada com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabela Alunos: {e}")

if __name__ == "__main__":
    criar_tabela_aluno()

def inserir_aluno(ra, nome, email, telefone, data_nascimento):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO Alunos (ra, nome, email, telefone, data_nascimento)
        VALUES (?, ?, ?, ?, ?)
    """, (ra, nome, email, telefone, data_nascimento))
    conexao.commit()
    cursor.close()
    conexao.close()