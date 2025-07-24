import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from models.aluno import inserir_aluno

def cadastrar():
    ra = entry_ra.get()
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    nascimento = entry_nascimento.get()

    if not (ra and nome and email and telefone and nascimento):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    try:
        inserir_aluno(ra, nome, email, telefone, nascimento)
        messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso.")
        for entry in [entry_ra, entry_nome, entry_email, entry_telefone, entry_nascimento]:
            entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar aluno: {e}")

janela = tk.Tk()
janela.title("Cadastro de Aluno")

tk.Label(janela, text="RA:").grid(row=0, column=0)
entry_ra = tk.Entry(janela)
entry_ra.grid(row=0, column=1)

tk.Label(janela, text="Nome:").grid(row=1, column=0)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=1, column=1)

tk.Label(janela, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(janela)
entry_email.grid(row=2, column=1)

tk.Label(janela, text="Telefone:").grid(row=3, column=0)
entry_telefone = tk.Entry(janela)
entry_telefone.grid(row=3, column=1)

tk.Label(janela, text="Data de Nascimento:").grid(row=4, column=0)
entry_nascimento = tk.Entry(janela)
entry_nascimento.grid(row=4, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=5, columnspan=2, pady=10)

janela.mainloop()