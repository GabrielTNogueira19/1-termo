# Gabriel Travaglini Nogueira Nº08

import tkinter as tk
from tkinter import messagebox


#############################################################################################################
# 1. Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"

# app = tk.Tk()
# app.title("Tela de Cadastro de Operador")
# app.geometry("600x400")

# def solicitar_informacao():

#     nome_operador = campo_nome.get()
#     turno_operador = campo_turno.get()

#     if nome_operador == "" or turno_operador == "":
#         messagebox.showwarning("Aviso", "Por favor digite seu nome e turno para realizar o cadastro!")
#     else:
#         messagebox.showinfo("Cadastro Concluído", f"Operador {nome_operador} registrado no Turno {turno_operador}. Boa jornada!")


# lbl_nome_usuario = tk.Label(app, text="Insira o seu nome para cadastro:", )
# lbl_nome_usuario.grid(row=1, column=0, pady=10)
# campo_nome = tk.Entry(app, font=("Arial", 12)) 
# campo_nome.grid(row=1, column=1, pady=10)

# lbl_menu = tk.Label(app, text="Menu de Turnos:\n A - Turno A \n B - Turno B \n C - Turno C")
# lbl_menu.grid(row=2, column=0, pady=10)
# lbl_idade_usuario = tk.Label(app, text="Informe seu turno dentre os disponíveis:")
# lbl_idade_usuario.grid(row=3, column=0, pady=10)
# campo_turno = tk.Entry(app, font=("Arial", 12)) 
# campo_turno.grid(row=3, column=1, pady=10)

# btn_cadastrar = tk.Button(app, text="Cadastrar", command=solicitar_informacao)
# btn_cadastrar.grid(row=4, column=1, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=6, column=1, pady=10)

# app.mainloop()

#############################################################################################################
# 2. Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.

# app = tk.Tk()
# app.title("Tela de Cálculo de Produção")
# app.geometry("380x200")

# def solicitar_informacao():

#     quantidade_pecas = int(campo_quantidade.get())

#     estimativa_pecas = quantidade_pecas * 8

#     if quantidade_pecas == "" or quantidade_pecas < 0:
#         messagebox.showwarning("Aviso", "Por favor digite uma quantidade valida de peças!")
#     else:
#         messagebox.showinfo("Cálculo Concluído", f"Com {quantidade_pecas} peças produzidas em 1 hora, a quantidade estimada para 8 horas é de {estimativa_pecas} peças!")


# lbl_pedir_quantidade = tk.Label(app, text="Informe a quantidade de peças produzidas em 1 hora de serviço:")
# lbl_pedir_quantidade.grid(row=1, column=0, pady=10, padx=10)

# campo_quantidade = tk.Entry(app, font=("Arial", 12)) 
# campo_quantidade.grid(row=2, column=0 ,pady=10, padx=10)

# btn_calcular = tk.Button(app, text="Calcular", command=solicitar_informacao)
# btn_calcular.grid(row=3, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column=0, pady=10)

# app.mainloop()

#############################################################################################################
# 3. Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# app = tk.Tk()
# app.title("Tela de Conversão de Unidade")
# app.geometry("650x200")

# def solicitar_informacao():

#     quantidade_bar = float(campo_bar.get())
#     valor_psi = float(campo_psi.get())

#     if valor_psi == "":
#         valor_psi = 14.5

#     valor_final = quantidade_bar * valor_psi

#     if quantidade_bar == "":
#         messagebox.showwarning("Aviso", "Por favor insira uma quantidade de Bar valida!")
#     else:
#         messagebox.showinfo("Cálculo Concluído", f"{quantidade_bar} Bar equivalem a {valor_final} PSI")


# lbl_pressao_bar = tk.Label(app, text="Insira a quantidade de Bar que deseja saber a conversão:", )
# lbl_pressao_bar.grid(row=1, column=0, pady=30)
# campo_bar = tk.Entry(app, font=("Arial", 12)) 
# campo_bar.grid(row=1, column=1, pady=10)

# lbl_valor_psi = tk.Label(app, text="Informe quantos PSI equivalem a 1 Bar (Caso deixado em branco PSI será 14,5):")
# lbl_valor_psi.grid(row=2, column=0, pady=30)
# campo_psi = tk.Entry(app, font=("Arial", 12)) 
# campo_psi.grid(row=2, column=1, pady=10)

# btn_calcular = tk.Button(app, text="Cálcular", command=solicitar_informacao)
# btn_calcular.grid(row=3, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=3, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# app = tk.Tk()
# app.title("Tela de Média de Qualidade")
# app.geometry("380x300")

# def solicitar_informacao():

#     valor_1 = float(campo_1.get())
#     valor_2 = float(campo_2.get())
#     valor_3 = float(campo_3.get())

#     if valor_1 == "" or valor_1 < 0 or valor_2 == "" or valor_2 < 0 or valor_3 == "" or valor_3 < 0:
#         messagebox.showwarning("Aviso", "Por favor insira um valor válido em cada uma das notas")
#     else:
#         media = (valor_1 + valor_2 + valor_3) / 3
#         messagebox.showinfo("Cálculo Concluído", f"Com as notas {valor_1}, {valor_2} e {valor_3} a média resulta em {media :.2f} de média")


# lbl_valor_1 = tk.Label(app, text="Insira a primeira nota de inspeção", )
# lbl_valor_1.grid(row=1, column=0, pady=30)
# campo_1 = tk.Entry(app, font=("Arial", 12)) 
# campo_1.grid(row=1, column=1, pady=10)

# lbl_valor_2 = tk.Label(app, text="Insira a segunda nota de inspeção:")
# lbl_valor_2.grid(row=2, column=0, pady=30)
# campo_2 = tk.Entry(app, font=("Arial", 12)) 
# campo_2.grid(row=2, column=1, pady=10)

# lbl_valor_3 = tk.Label(app, text="Insira a terceira nota de inspeção:")
# lbl_valor_3.grid(row=3, column=0, pady=30)
# campo_3 = tk.Entry(app, font=("Arial", 12)) 
# campo_3.grid(row=3, column=1, pady=10)

# btn_calcular = tk.Button(app, text="Cálcular", command=solicitar_informacao)
# btn_calcular.grid(row=4, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# 5. Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

app = tk.Tk()
app.title("Tela de Conversão de Unidade")
app.geometry("380x300")

def solicitar_informacao():

    valor_1 = float(campo_1.get())
    valor_2 = float(campo_2.get())
    valor_3 = float(campo_3.get())

    if valor_1 == "" or valor_1 < 0 or valor_2 == "" or valor_2 < 0 or valor_3 == "" or valor_3 < 0:
        messagebox.showwarning("Aviso", "Por favor insira um valor válido em cada uma das notas")
    else:
        media = (valor_1 + valor_2 + valor_3) / 3
        messagebox.showinfo("Cálculo Concluído", f"Com as notas {valor_1}, {valor_2} e {valor_3} a média resulta em {media :.2f} de média")


lbl_valor_1 = tk.Label(app, text="Insira a primeira nota de inspeção", )
lbl_valor_1.grid(row=1, column=0, pady=30)
campo_1 = tk.Entry(app, font=("Arial", 12)) 
campo_1.grid(row=1, column=1, pady=10)

lbl_valor_2 = tk.Label(app, text="Insira a segunda nota de inspeção:")
lbl_valor_2.grid(row=2, column=0, pady=30)
campo_2 = tk.Entry(app, font=("Arial", 12)) 
campo_2.grid(row=2, column=1, pady=10)

lbl_valor_3 = tk.Label(app, text="Insira a terceira nota de inspeção:")
lbl_valor_3.grid(row=3, column=0, pady=30)
campo_3 = tk.Entry(app, font=("Arial", 12)) 
campo_3.grid(row=3, column=1, pady=10)

btn_calcular = tk.Button(app, text="Cálcular", command=solicitar_informacao)
btn_calcular.grid(row=4, column=0, pady=10)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.grid(row=4, column= 1, pady=10)

app.mainloop()