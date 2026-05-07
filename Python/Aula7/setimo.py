# Atividades de PRINT e INPUT

# atividade 1

modelo = input("Qual o modelo do seu veículo? ")
placa = input("Qual a placa do seu veículo? ")

print("Veículo", modelo,"de placa", placa, "registrado no sistema. Tenha uma boa viagem!")

# atividade 2

print("CÁLCULO DE AUTONOMIA")

capacidade_litros = float(input("Insira a capacidade máxima do seu tanque de combustível (em litros): "))
consumo_medio = float(input("Insira o consumo médio seu veículo (Km/L): "))

print("Com o tanque cheio seu veículo pode percorrer", consumo_medio*capacidade_litros, "Km")

#atividade 3

print("CONVERSOR DE MOEDA (USD - BRL)")

valor_frete = float(input("Digite o valor que deseja converter em real: "))
conversao_real = float(input("Valor da taxa em reais: "))
total_conversao = valor_frete*conversao_real

print(f"A conversão de {valor_frete:.2f} dolars, é igual a {total_conversao:.2f} reais" )

print("A conversão de", valor_frete, "dolars, é igual a", round(total_conversao), "reais")

# atividade 4

print("CALCULADOR DE MÉDIA DE ENTREGA")

rota1 = int(input("informe o tempo de entrega referente a 1ª rota (em horas): "))

rota2 = int(input("Informe o tempo de entrega referente a 2ª rota (em horas): "))

rota3 = int(input("Informe o tempo de entrega referente a 3ª rota (em horas): "))

media_rota = float((rota1+rota2+rota3)/3)

print(f"A média de entrega das 3 rotas foi de {media_rota:.2f} horas")

# atividades IF, ELIF e ELSE

# atividade 5

peso = float(input("Informe o peso em toneladas de seu veículo: "))

if peso <= 10:
    print("Veículo com Carga Leve")
elif peso > 10 and peso <= 25:
    print("Veículo com Carga Padrão")
elif peso > 25:
    print("ALERTA: Veículo com Excesso de Peso!")
else:
    print("Digite outro valor")

# atividade 6

print("CLASSIFICADOR DE DESTINO")

print("Menu de Destino")
print("Iníco com 'N' = Região Norte")
print("Iníco com 'S' = Região Sul")
print("Para qualquer outro início será definido como 'Região Internacional'")

codigo = input("Insira o início do código da carga: ").upper()

if codigo == "S":
    print("Carga com destino para a Região Sul")
elif codigo == "N":
    print("Carga com destino para a Região Norte")
else:
    print("carga com destino para Região Internacional")

# atividade 7

checklist = input("O checklist foi realizado (Concluído ou não concluído): ")

motorista = input("O motorista foi identificado (Sim ou Não): ")

if checklist == "Concluído" and motorista == "Sim":
    print("Liberado - Boa Viagem")

else:
    print("Realizar o checklist novamente")

# atividade 8

totalAgendadas = int(input("Informe o total de entregas agendadas: "))
totalRealizadas = int(input("Informe o total de entregas realizadas, porém atrazadas: "))

indice = (totalRealizadas/totalAgendadas)*100

print(f"Indice de atraso em um total de {indice:.2f} %")

if indice > 10:
    print("Necessário Otimizar Rotas")
else:
    print("Logística Eficiente")

# atividade 9

pressao = int(input("Insira a pressão do seu pneu de carga em PSI: "))

if pressao < 100:
    print("ALERTA! Pressão abaixo do recomendado.")

elif pressao >= 100 and pressao <= 110:
    print("Pressão dentro do recomendado!")

else:
    print("ALERTA! Pressão acima do recomendado.")

# Atividades de FOR e WHILE

# atividade 10

import time

for num in range(5,0,-1):
    print(num)
    time.sleep(1)

print("Portão Trancado!")
