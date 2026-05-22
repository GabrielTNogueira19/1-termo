import tkinter as tk
from tkinter import messagebox

# 1- Configurar evento

def solicitar_informacao():

    # .get serve para buscar o texto que foi digitado
    nome_usuario = campo_nome.get()
    idade_usuario = campo_idade.get()

    if nome_usuario == "" or idade_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite seu nome e idade!")
    else:
        messagebox.showinfo("Ficha", f"Olá {nome_usuario} você tem {idade_usuario} anos !!")

# 2- Configuração de janela

app = tk.Tk()
app.title("Tela de Usuário")
app.geometry("300x200")

# 3- Componentes

# Texto para que indica onde inserir o nome do usuario
lbl_nome_usuario = tk.Label(app, text="Digite seu nome:")
lbl_nome_usuario.grid(row=1, column=0, pady=10)

# Campo para inserir o nome d0 usuario
campo_nome = tk.Entry(app, font=("Arial", 12)) 
campo_nome.grid(row=1, column=1, pady=10)

# Texto para que indica onde inserir a idade do usuario
lbl_idade_usuario = tk.Label(app, text="Digite sua idade:")
lbl_idade_usuario.grid(row=2, column=0, pady=10)

# Campo para inserir a idade do usuario
campo_idade = tk.Entry(app, font=("Arial", 12)) 
campo_idade.grid(row=2, column=1, pady=10)

# Botão para realizar o cadastro
btn_cadastrar = tk.Button(app, text="Cadastrar", command=solicitar_informacao)
btn_cadastrar.grid(row=4, column=1, pady=10)

# Botão para fechar a página
btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.grid(row=6, column=1, pady=10)

# 4- rodar interface
app.mainloop()