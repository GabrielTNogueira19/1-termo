# Condições Lógicas
# if: "Se" a condição for verdadeira.
# elif: "Senão, se" (usados para múltiplas condições).
# else: "Senão" (executa se nenhuma das anteriores for verdadeira).

# Exemplo 1
# ..........................................................................................................

print("Verificar Maioridade")
idade = int(input("Qual sua idade:"))

if idade >= 18:
    print("Você é Adulto")

elif idade >= 16:
    print("Você não é adulto mas pode votar")

else:
    print("Você é de Menor")


# Exemplo 2
# ........................................................................................................
print("Loja")
print("Bem vindo ao Sistema do Gabriel")
print("Opções:")
print("1 - Sapato")
print("2 - Roupas")
print("3 - Perfumes")

escolha = float(input("Digite sua escolha pelo número da opção: "))

if escolha == 1 :
    print("Você escolheu sapatos")
    valorSapatos = float(input("Digite o valor do Sapato: "))
    tamanhoSapatos = int(input("Digite a quantidade desejada: "))

    totalSapatos = valorSapatos*tamanhoSapatos

    print("Sua compra de sapatos ficou em um total de: ", totalSapatos)

elif escolha == 2:
    print("Você escolheu roupas")
    
    valorRoupas = float(input("Digite o valor da Roupa: "))
    tamanhoRoupas = int(input("Digite a quantidade desejada: "))

    totalRoupas = valorRoupas*tamanhoRoupas

    print("Sua compra de roupas ficou em um total de: ", totalRoupas)

elif escolha == 3:
    print("Você escolheu perfumes")

    valorPerfumes = float(input("Digite o valor do Perfume: "))
    tamanhoPerfumes = int(input("Digite a quantidade desejada: "))

    totalPerfumes = valorPerfumes*tamanhoPerfumes

    print("Sua compra de perfumes ficou em um total de: ", totalPerfumes)

else:
    print("Obrigado por usar meu sistema")
    print("Escolha um número disponivel destre as opções. Tente Novamente: ")

# Exemplo 3
# ......................................................................................................

print("Escolha uma opção para iniciar o sistema: ")
print("Séries = S")
print("Filmes = F")

categoria = input("Digite sua categoria: ")

if categoria == "S" or "s":
    print("Você optou por Séries")

elif categoria == "F" or "f":
    print("Você optou por Filmes")

else:
    print("Escolha uma opção disponivel destre as opções. Tente Novamente: ")

    print("Obrigado por usar meu sistema")