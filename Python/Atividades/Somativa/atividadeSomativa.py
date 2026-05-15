# 1. Registro de Veículo: Peça o modelo do veículo e a placa.
# Exiba: "Veículo [Modelo] de placa [Placa] registrado no sistema. Boa viagem!"

print("REGISTRO DE VEÍCULO")

modelo = input("Qual o modelo do seu veículo? ")
placa = input("Qual a placa do seu veículo? ")

print("Veículo", modelo,"de placa", placa, "registrado no sistema. Tenha uma boa viagem!")

# 2. Cálculo de Autonomia:
# Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l).
# Calcule e exiba a distância total que o veículo pode percorrer com o tanque cheio.

print("CÁLCULO DE AUTONOMIA")

litros = float(input("Insira a capacidade máxima do seu tanque de combustível (em litros): "))
consumo = float(input("Insira o consumo médio seu veículo (Km/L): "))

print("Com o tanque cheio seu veículo pode percorrer", consumo*litros, "Km")

# 3. O sistema lê o valor de um frete em Dólar (USD). 
# Converta para Real (BRL) considerando a taxa de $1,00~USD \approx 5,00~BRL$ e exiba com duas casas decimais.

print("CONVERSOR DE MOEDA (USD - BRL)")

valor = float(input("Digite o valor que deseja converter em real: "))

print(f"A conversão de {valor:.2f} dolars, é igual a {valor*5:.2f} reais" )

# 4. Média de Entrega: 
# Peça o tempo de entrega (em horas) de 3 rotas diferentes realizadas por um motorista. 
# Exiba a média aritmética simples do tempo dessas entregas.

print("CALCULADOR DE MÉDIA DE ENTREGA")

entrega1 = int(input("informe o tempo de entrega referente a 1ª rota (em horas): "))

entrega2 = int(input("Informe o tempo de entrega referente a 2ª rota (em horas): "))

entrega3 = int(input("Informe o tempo de entrega referente a 3ª rota (em horas): "))

media = float((entrega1+entrega2+entrega3)/3)

print("A média de entrega das 3 rotas foi de", media, "horas")

# 5. Monitor de Carga: 
# Peça o peso atual de um caminhão em toneladas.
# o Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão". 
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

peso = float(input("Informe o peso em toneladas de seu veículo: "))

if peso <= 10:
    print("Veículo com Carga Leve")
elif peso > 10 and peso <= 25:
    print("Veículo com Carga Padrão")
else:
    print("ALERTA: Veículo com Excesso de Peso!")

# 6. Classificador de Destino: 
# O usuário insere o código da carga.
# Se começar com "N", exiba "Região Norte". 
# Se começar com "S", "Região Sul". 
# Para qualquer outro, "Região Internacional".

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

# 7. Liberação de Saída: 
# O caminhão só pode sair se o checklist == "concluído" 
# E o motorista_identificado == "sim".
# Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

checklist = input("Informe qual o status do Checklist do motorista: ").lower()
motorista_identificado = input("O motorista foi identificado? ").lower()

if checklist == "concluído" and checklist == "concluido" and motorista_identificado == "sim":

    print("Saída Autorizada. Boa Viagem!")
    
else:
    print("Saída Não Autorizada!")

# 8. Cálculo de Atrasos: 
# Peça o total de entregas agendadas e o total de entregas realizadas com atraso.
# Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar Rotas", caso contrário, "Logística Eficiente".

totalAgendadas = int(input("Informe o total de entregas agendadas: "))
totalRealizadas = int(input("Informe o total de entregas realizadas, porém atrazadas: "))

indice = (totalRealizadas/totalAgendadas)*100

print("Indice de atraso em um total de", indice, "%")

if indice > 10:
    print("Necessário Otimizar Rotas")
else:
    print("Logística Eficiente")

# 9. Validação de Calibragem: 
# Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

pressao = int(input("Insira a pressão do seu pneu de carga em PSI: "))

if pressao < 100:
    print("ALERTA! Pressão abaixo do recomendado.")

elif pressao >= 100 and pressao <= 110:
    print("Pressão dentro do recomendado!")

else:
    print("ALERTA! Pressão acima do recomendado.")

#10. Contagem de Embarque: 
# Use um for para fazer uma contagem regressiva de 5 até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

import time

contagem = [5, 4, 3, 2, 1]

for num in contagem:
    print(num)
    time.sleep(1)

print("Portão Trancado!")

#11. Somatório de Fretes (Acumulador):
# Use um while para pedir o valor do frete de vários pedidos. 
# O loop para quando o usuário digitar 0. No fim, mostre o faturamento total acumulado.

frete = 1
soma = 0

while frete != 0:

    frete = float(input("Digite o valor do frete (insira 0 para encerrar): "))
    
    soma = soma + frete

print(f"O faturamento total foi de {soma} reais")

#12. Monitoramento de Frota: 
# Use um for para pedir a quilometragem de 5 veículos diferentes.
# Ao final, mostre qual foi a maior quilometragem registrada.

veiculos = ["veiculo1", "veiculo2", "veiculo3", "veiculo4", "veiculo5"]

maior = 0

for carro in veiculos:
    carro = float(input(f"Insira a quilometragem do {carro}: "))
    
    if carro > maior:
        maior = carro

print(f"A maior quilometragem registrada foi de {maior} Km")

# 13. Sistema de Rastreio: 
# Crie um while que peça o código de acesso do rastreador ("track99").
# Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se esgotar, exiba "Rastreamento Bloqueado".

erros = 0
tentativas = 3

while erros != 3:

    codigo = input("Insira o código de acesso do rastreador: ")

    if codigo != "track99":
        erros = erros+1
        tentativas = tentativas-1
        print(f"Código incorreto. Tente novamente. Você tem mais {tentativas} tentativas")

    else:
        break

if erros == 3:
    print("Rastreamento Bloqueado. Usuário exedeu o máximo de 3 tentativas")

else:
    print("Codigo correto. Acesso Liberado")

#14. Gerenciador de Combustível: 
# Comece com um tanque de 500 litros. 
# Crie um menu (while) onde o usuário pode:
# (1) Abastecer o tanque da base,
# (2) Retirar combustível para um caminhão 
# (3) Sair. 
# Se o tanque da base ficar abaixo de 50 litros, avise: "Reserva Crítica!".

print("GERENCIADOR DE COMBUSTÍVEL")
print("MENU")
print("(1) Abastecer o tanque da base")
print("(2) Retirar 105 litros de combustível para um caminhão")
print("(3) Sair")

opção = 0
tanque = 500

while opção != 3:

    opção = int(input("Insira a opção desejada: "))

    if opção == 1:
        tanque = 500
        print(f"O tanque possui {tanque} litros")

    elif opção == 2:
        tanque = tanque-55
        print(f"O tanque possui {tanque} litros")
        if tanque < 50:
            print("Reserva Crítica! Abasteça.")
            break

print("Sistema Encerrado")

# 15. Relatório de Inspeção de Pneus:
# Use um for para processar 5 pneus.
# Para cada um, peça a profundidade do sulco (em mm).
# Se o pneu for aprovado (maior ou igual a 1.6mm), conte-o.
# No final do loop, exiba o total de pneus aprovados e a porcentagem de conformidade da frota.

contagem = 0
total = 5

for i in range(1, 6):

    medida = float(input(f"Digite a medida do sulco do pneu {i} em mm: "))

    if medida >= 1.6:
        contagem = contagem+1
        print("Pneu aprovado e adicionado a contagem geral.")

    else:
        print("Pneu fora das medidas regulares, não foi adicionado a contagem.")
        pass

porcentagem = (contagem/total)*100

print(f"Tiveram {contagem} pneus aprovados hoje com uma porcentagem de {porcentagem}% de comformidade")