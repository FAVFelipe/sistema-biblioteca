import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from models.emprestimo import inserir_emprestimo

def cadastrar_emprestimo():
    ra = entry_ra.get()
    codigo_livro = entry_codigo_livro.get()
    data_retirada = entry_data_retirada.get()
    data_entrega = entry_data_entrega.get()

    if not (ra and codigo_livro and data_retirada and data_entrega):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    try:
        inserir_emprestimo(int(ra), int(codigo_livro), data_retirada, data_entrega)
        messagebox.showinfo("Sucesso", "Empréstimo cadastrado com sucesso.")
        entry_ra.delete(0, tk.END)
        entry_codigo_livro.delete(0, tk.END)
        entry_data_retirada.delete(0, tk.END)
        entry_data_entrega.delete(0, tk.END)
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

tk.Label(janela, text="Data de Retirada (DD-MM-AAAA):").grid(row=2, column=0)
entry_data_retirada = tk.Entry(janela)
entry_data_retirada.grid(row=2, column=1)

tk.Label(janela, text="Data de Entrega (DD-MM-AAAA):").grid(row=3, column=0)
entry_data_entrega = tk.Entry(janela)
entry_data_entrega.grid(row=3, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_emprestimo).grid(row=4, columnspan=2, pady=10)

janela.mainloop()