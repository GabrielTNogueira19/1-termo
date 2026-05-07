print("Bem vindo ao calculador de gorjetas!")

conta = float(input("Insira o valor da sua conta: "))

atendimento = input("O atendimento à mesa foi com um garçom?")

if atendimento == "sim":
    valor10 = conta*(10/100)
    total1 = valor10+conta
    print("Sua gorjeta será de", valor10, "reais, totalizando sua conta final com", total1, "reais")

elif atendimento == "não":
    valor5 = conta*(5/100)
    total2 = valor5+conta
    print("Sua gorjeta será de", valor5, "reais, totalizando sua conta final com", total2, "reais")

else:
    print("Resposta não identificada. Por favor responda apenas com 'sim' ou 'não'")