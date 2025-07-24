from models.aluno import criar_tabela_aluno
from models.livro import criar_tabela_livros
from models.emprestimo import criar_tabela_emprestimos

if __name__ == "__main__":
    try:
        criar_tabela_aluno()
        criar_tabela_livros()
        criar_tabela_emprestimos()
        print("Tabelas criadas com sucesso.")
    except Exception as e:
        print(f"Erro ao criar tabelas: {e}")
