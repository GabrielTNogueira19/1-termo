# Conversor de Moeda (Frete Internacional): 
# O sistema lê o valor de um frete em Dólar (USD). 
# Converta para Real (BRL) considerando a taxa de $1,00~USD \approx 5,00~BRL$ e exiba com duas casas decimais.

print("CONVERSOR DE MOEDA (USD - BRL)")

valor = float(input("Digite o valor que deseja converter em real: "))

print(f"A conversão de {valor:.2f} dolars, é igual a {valor*5:.2f} reais" )
