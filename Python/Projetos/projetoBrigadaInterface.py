import tkinter as tk
from tkinter import messagebox

# 1- Configurar evento

def solicitar_informacao():

    # .get serve para buscar o texto que foi digitado
    nome_usuario = campo_nome.get()
    setor_usuario = campo_idade.get()
    treinamento_usuário = campo_treinamento.get()

    if nome_usuario == "" or setor_usuario == "":
        messagebox.showwarning("Aviso", "Por favor digite seu nome e idade!")
    else:
        messagebox.showinfo("Ficha", f"Olá {nome_usuario} você tem {idade_usuario} anos !!")

# 2- Configuração de janela

app = tk.Tk()
app.title("Tela de Usuário")
app.geometry("600x400")

# print("=======================================")
# print("1 - Cadastrar Funcionário")
# print("2 - Listar EPIs por Setor")
# print("3 - Verificar Status do Treinamento")
# print("4 - Resumo dos Funcionários")
# print("5 - Sair")


btn_opcao1 = tk.Button(app, text="--1- ", command=solicitar_informacao)
btn_opcao1.grid(row=0, column=0, pady=10)
lbl_cadastrar_usuário = tk.Label(app, text="Cadastrar Usuário", font=("Arial", 14, "bold"))
lbl_cadastrar_usuário.grid(row=0, column=1, padx=10)

btn_opcao1 = tk.Button(app, text="--2-", command=solicitar_informacao)
btn_opcao1.grid(row=0, column=0, pady=10)
lbl_cadastrar_usuário = tk.Label(app, text="Listar EPIs por Setor", font=("Arial", 14, "bold"))
lbl_cadastrar_usuário.grid(row=0, column=1, padx=10)

btn_opcao1 = tk.Button(app, text="--3-", command=solicitar_informacao)
btn_opcao1.grid(row=0, column=0, pady=10)
lbl_cadastrar_usuário = tk.Label(app, text="Cadastrar Usuário", font=("Arial", 14, "bold"))
lbl_cadastrar_usuário.grid(row=0, column=1, padx=10)

btn_opcao1 = tk.Button(app, text="--4-", command=solicitar_informacao)
btn_opcao1.grid(row=0, column=0, pady=10)
lbl_cadastrar_usuário = tk.Label(app, text="Cadastrar Usuário", font=("Arial", 14, "bold"))
lbl_cadastrar_usuário.grid(row=0, column=1, padx=10)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=6, column=1, pady=10)

# 4- rodar interface
app.mainloop()