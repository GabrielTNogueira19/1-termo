# Somatório de Fretes (Acumulador):
# Use um while para pedir o valor do frete de vários pedidos. 
# O loop para quando o usuário digitar 0. No fim, mostre o faturamento total acumulado.

frete = 1
soma = 0
while frete != 0:

    frete = float(input("Digite o valor do frete (insira 0 para encerrar): "))
    soma = soma + frete

print(f"O faturamento total foi de {soma} reais")