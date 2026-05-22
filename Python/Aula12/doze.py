# Tkinter

# Componentes principais

# tk: janela
# label: Texto em rótulo
# button: Um botão de clique
# entry: Campo de entrada de texto

# biblioteca

import tkinter as tk
from tkinter import messagebox
# 1- Criar janela
janela = tk.Tk()
# janela.configure(bg="#F70000")
janela.title("Minha Primeira Janela em GUI") # Dando titulo a janela
janela.geometry("400x200") # Largura x Altura  

# 2- Criar a função que o botão vai executar(evento)

def mostrar_mensagem():
    messagebox.showinfo("Sucesso", "Você clicou no botão!!!")

# 3- Criar os componentes(widgets)

lbl_titulo = tk.Label(janela, text="Bem Vindo à Aula de Tkinter", font=("Arial", 14, "bold"), bg="#00FF2F")
btn_clique = tk.Button(janela, text="Clique Aqui", font=("Arial", 14, "bold"), bg="#00FF2f", fg="white", command=mostrar_mensagem)

# 4- Posicionar os componentes

# pady - posicionar vertical |
# padx - posicionar horizontal __

lbl_titulo.pack(pady=20, padx=50)
btn_clique.pack(pady=50, padx=100)

# 5- Rodar o loop da interface
janela.mainloop()
