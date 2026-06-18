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

# app = tk.Tk()
# app.title("Tela de Termostato Inteligente")
# app.geometry("500x200")

# def solicitar_informacao():

#     temperatura = float(campo_temperatura.get())

#     if temperatura == "" or temperatura < 0:
#         messagebox.showwarning("Aviso", "Por favor insira uma temperatura válida!")
#     else:
#         return temperatura

# def verificar_temperatura():

#     temperatura = solicitar_informacao()

#     if temperatura < 40:
#         messagebox.showwarning("Aviso", "Motor em baixa carga!")
    
#     elif temperatura >= 40 and temperatura <= 70:
#         messagebox.showinfo("Informando", "Motor em temperatura normal!")
    
#     else:
#          messagebox.showwarning("Aviso", "ALERTA: Temperatura elevada! Resfriamento Ativado!")

# lbl_temperatura = tk.Label(app, text="Insira a temperatura atual do motor em graus celcius:")
# lbl_temperatura.grid(row=1, column=0, pady=30, padx=10)
# campo_temperatura = tk.Entry(app, font=("Arial", 12)) 
# campo_temperatura.grid(row=1, column=1, pady=10)

# btn_conferir = tk.Button(app, text="Conferir", command=verificar_temperatura)
# btn_conferir.grid(row=4, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# app = tk.Tk()
# app.title("Tela de Classificação de Lotes")
# app.geometry("500x200")

# def solicitar_informacao():

#     codigo = campo_codigo.get()

#     if codigo == "":
#         messagebox.showwarning("Aviso", "Por favor insira um código válido")
#     else:
#         return codigo

# def ler_codigo():

#     codigo = solicitar_informacao().upper()

#     if codigo.startswith("A"):
#         messagebox.showinfo("Produto Lido", "Produto classificado como ALIMENTO")
    
#     elif codigo.startswith("E"):
#         messagebox.showinfo("Produto Lido", "Produto classificado como ELETRÔNICO")
    
#     else:
#          messagebox.showwarning("Produto Não Identificado", "Produto classificado como DESCONHECIDO!")

# lbl_codigo = tk.Label(app, text="Insira o código do lote do produto a ser classificado:")
# lbl_codigo.grid(row=1, column=0, pady=30, padx=10)
# campo_codigo = tk.Entry(app, font=("Arial", 12)) 
# campo_codigo.grid(row=1, column=1, pady=10)

# btn_ler_codigo = tk.Button(app, text="Ler Código", command=ler_codigo)
# btn_ler_codigo.grid(row=4, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# 7. Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# app = tk.Tk()
# app.title("Tela de Segurança de Operação")
# app.geometry("650x300")

# def solicitar_informacao(informacao):

#     sensor_porta = campo_sensor_porta.get()
#     botao_emergencia = campo_botao_emergencia.get()

#     if sensor_porta == "" or botao_emergencia == "":
#         messagebox.showwarning("Aviso", "Por favor insira os retornos do sensor e botão para prosseguir com a checagem!")
#     else:
#         if informacao == 1:
#             return sensor_porta.lower()
#         elif informacao == 2:
#             return botao_emergencia.lower()

# def verificar_status():

#     sensor_porta = solicitar_informacao(1)
#     botao_emergencia = solicitar_informacao(2)

#     if sensor_porta == "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Iniciar Máquina", "Requisitos atendidos. Iniciando máquina!")
    
#     elif sensor_porta == "fechada" and botao_emergencia != "desligado":
#         messagebox.showinfo("Iniciar Máquina Barrado", "Requisitos não atendidos. Desligue o botão de emergência para iniciar a máquina!")
    
#     elif sensor_porta != "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Iniciar Máquina Barrado", "Requisitos não atendidos. Feche a porta para iniciar a máquina!")
    
#     elif sensor_porta != "fechada" and botao_emergencia != "desligado":
#         messagebox.showinfo("Iniciar Máquina Barrado", "Requisitos não atendidos. Feche a porta e desligue o botão de emergência para iniciar a máquina!")

# lbl_sensor_porta = tk.Label(app, text="Insira o retorno do 'sensor_porta' (insira apenas 'Aberta' ou 'Fechada'):")
# lbl_sensor_porta.grid(row=1, column=0, pady=30, padx=10)
# campo_sensor_porta = tk.Entry(app, font=("Arial", 12)) 
# campo_sensor_porta.grid(row=1, column=1, pady=10)

# lbl_botao_emergencia = tk.Label(app, text="Insira o estado do botão de emergência (insira apenas 'Ligado' ou 'Desligado'):")
# lbl_botao_emergencia.grid(row=2, column=0, pady=50, padx=10)
# campo_botao_emergencia = tk.Entry(app, font=("Arial", 12)) 
# campo_botao_emergencia.grid(row=2, column=1, pady=10)

# btn_verificar = tk.Button(app, text="Verficar Condições", command=verificar_status)
# btn_verificar.grid(row=4, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# 8. Cálculo de Descarte: Peça o total de peças produzidas e o total de defeituosas. Se
# o descarte for maior que 5% do total, exiba "Revisar Processo", caso contrário,
# "Processo Otimizado".

# app = tk.Tk()
# app.title("Tela de Cálculo de Descarte")
# app.geometry("650x300")

# def solicitar_informacao():

#     pecas_produzidas = int(campo_pecas_produzidas.get())
#     pecas_defeituosas = int(campo_pecas_defeituosas.get())

#     if pecas_produzidas == "" or pecas_produzidas < 0 or pecas_defeituosas == "" or pecas_defeituosas < 0:
#         messagebox.showwarning("Aviso", "Por favor insira ambas as quantidades de peças corretamente para a realização do cálculo!")
#     else:
#         calculo_descarte = (pecas_defeituosas/pecas_produzidas) *100
#         return calculo_descarte

# def verificar_status():

#     percentual_descarte = solicitar_informacao()

#     if percentual_descarte > 5:
#         messagebox.showwarning(f"Aviso", "Percentual de descarte em alto! Revisar Processo!")
#     else:
#         messagebox.showinfo("Percentual de descarte", "Percentual de descarte dentro das conformidades! Processo Otimizado!")

# lbl_pecas_produzidas = tk.Label(app, text="Insira o total de pecas produzidas:")
# lbl_pecas_produzidas.grid(row=1, column=0, pady=30, padx=10)
# campo_pecas_produzidas = tk.Entry(app, font=("Arial", 12)) 
# campo_pecas_produzidas.grid(row=1, column=1, pady=10)

# lbl_pecas_defeituosas = tk.Label(app, text="Insira o total de pecas defeituosas:")
# lbl_pecas_defeituosas.grid(row=2, column=0, pady=50, padx=10)
# campo_pecas_defeituosas = tk.Entry(app, font=("Arial", 12)) 
# campo_pecas_defeituosas.grid(row=2, column=1, pady=10)

# btn_verificar = tk.Button(app, text="Cálcular Descarte", command=verificar_status)
# btn_verificar.grid(row=4, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# 9. Validação de Medida: Uma peça deve ter entre 9.8mm e 10.2mm. Peça a medida e
# diga se está dentro da tolerância, acima ou abaixo.

# app = tk.Tk()
# app.title("Tela de Validação de Medida")
# app.geometry("350x200")

# def solicitar_informacao():

#     peca = float(campo_peca.get())

#     if peca == "" or peca < 0:
#         messagebox.showwarning("Aviso", "Por favor insira uma medida de peça válida para verificação!")
#     else:
#         return peca

# def verificar_temperatura():

#     peca = solicitar_informacao()

#     if peca < 9.8:
#         messagebox.showwarning("Aviso", "Peça abaixo da tolerância. Revise a peça!")
    
#     elif peca >= 9.8 and peca <= 10.2:
#         messagebox.showinfo("Informando", "Peça dentro da tolerância!")
    
#     else:
#          messagebox.showwarning("Aviso", "Peça acima da tolerância. Revise a peça!")

# lbl_peca = tk.Label(app, text="Insira a medida da peça:")
# lbl_peca.grid(row=1, column=0, pady=30, padx=10)
# campo_peca = tk.Entry(app, font=("Arial", 12)) 
# campo_peca.grid(row=1, column=1, pady=10)

# btn_conferir = tk.Button(app, text="Conferir", command=verificar_temperatura)
# btn_conferir.grid(row=4, column=0, pady=10)

# btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
# btn_fechar.grid(row=4, column= 1, pady=10)

# app.mainloop()

#############################################################################################################
# 10.Contagem Regressiva de Setup: Use um for para fazer uma contagem regressiva
# de 10 até 1 para o início de uma prensa, e finalize com "Prensa Ativada!".

app = tk.Tk()
app.title("Tela de Validação de Medida")
app.geometry("350x200")

from time import sleep

def contar():

    for i in range(1, 11):

        print(10-i)
        sleep(1)

lbl_inicio = tk.Label(app, text="Contagem até inicializar a prensa!")
lbl_inicio.grid(row=1, column=0, pady=30, padx=10)

btn_comecar = tk.Button(app, text="Começar Contagem", command=contar)
btn_comecar.grid(row=4, column=0, pady=10)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.grid(row=4, column= 1, pady=10)

app.mainloop()