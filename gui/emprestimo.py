import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from models.emprestimo import inserir_emprestimo, emprestimo_ja_existe

from datetime import datetime

def parse_data(data_str):
    for fmt in ('%d/%m/%Y', '%d-%m-%Y'):
        try:
            return datetime.strptime(data_str, fmt)
        except ValueError:
            continue
    raise ValueError("Formato de data inválido. Use DD/MM/AAAA ou DD-MM-AAAA.")

def cadastrar_emprestimo():
    ra = entry_ra.get()
    codigo_livro = entry_codigo_livro.get()
    data_retirada = entry_data_retirada.get()
    data_entrega = entry_data_entrega.get()

    if not (ra and codigo_livro and data_retirada and data_entrega):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return
    
      # Verifica se o empréstimo já existe
    if emprestimo_ja_existe(int(ra), int(codigo_livro)):
        messagebox.showerror("Erro", "Este empréstimo já existe para este aluno e livro.")
        return

    try:
        # Validação da lógica de datas
        retirada = parse_data(data_retirada)
        entrega = parse_data(data_entrega)

        if retirada > entrega:
            messagebox.showerror("Erro", "A data de retirada não pode ser maior que a data de entrega.")
            return

        # Se passou na validação, insere no banco
        inserir_emprestimo(int(ra), int(codigo_livro), data_retirada, data_entrega)
        messagebox.showinfo("Sucesso", "Empréstimo cadastrado com sucesso.")
        entry_ra.delete(0, tk.END)
        entry_codigo_livro.delete(0, tk.END)
        entry_data_retirada.delete(0, tk.END)
        entry_data_entrega.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro de data", "Insira as datas no formato correto: DD/MM/AAAA.")
    except Exception as e:
        erro_str = str(e)
        if "FOREIGN KEY" in erro_str or "conflicted" in erro_str:
            messagebox.showerror(
                "Erro de dados",
                "Não foi possível cadastrar o empréstimo.\nVerifique se o RA do aluno e o código do livro estão corretos e cadastrados no sistema."
            )
        else:
            messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")

janela = tk.Tk()
janela.title("Cadastro de Empréstimo")

tk.Label(janela, text="RA do Aluno:").grid(row=0, column=0)
entry_ra = tk.Entry(janela)
entry_ra.grid(row=0, column=1)

tk.Label(janela, text="Código do Livro:").grid(row=1, column=0)
entry_codigo_livro = tk.Entry(janela)
entry_codigo_livro.grid(row=1, column=1)

tk.Label(janela, text="Data de Retirada (DD/MM/AAAA):").grid(row=2, column=0)
entry_data_retirada = tk.Entry(janela)
entry_data_retirada.grid(row=2, column=1)

tk.Label(janela, text="Data de Entrega (DD/MM/AAAA):").grid(row=3, column=0)
entry_data_entrega = tk.Entry(janela)
entry_data_entrega.grid(row=3, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_emprestimo).grid(row=4, columnspan=2, pady=10)

janela.mainloop()