import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from models.livro import inserir_livro

def cadastrar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    categoria = entry_categoria.get()
    editora = entry_editora.get()

    if not (titulo and autor and categoria and editora):
        messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
        return

    try:
        inserir_livro(titulo, autor, categoria, editora)
        messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso.")
        for entry in [entry_titulo, entry_autor, entry_categoria, entry_editora]:
            entry.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar livro: {e}")

janela = tk.Tk()
janela.title("Cadastro de Livro")

tk.Label(janela, text="Título:").grid(row=1, column=0)
entry_titulo = tk.Entry(janela)
entry_titulo.grid(row=1, column=1)

tk.Label(janela, text="Autor:").grid(row=2, column=0)
entry_autor = tk.Entry(janela)
entry_autor.grid(row=2, column=1)

tk.Label(janela, text="Categoria:").grid(row=3, column=0)
entry_categoria = tk.Entry(janela)
entry_categoria.grid(row=3, column=1)

tk.Label(janela, text="Editora:").grid(row=4, column=0)
entry_editora = tk.Entry(janela)
entry_editora.grid(row=4, column=1)

tk.Button(janela, text="Cadastrar", command=cadastrar_livro).grid(row=5, columnspan=2, pady=10)

janela.mainloop()