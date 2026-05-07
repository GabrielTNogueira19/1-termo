valor = int(input("Insira um valor que você queira descobrir seu antecesor ou sucessor: "))

posicao = input("Qual você quer descobrir, Antecessor ou Sucessor? ")

if posicao == "Sucessor":
    
    valorS = valor+1
    print("O sucessor de", valor, "é", valorS)

elif posicao == "Antecessor":

    valorA = valor-1
    print("O antecessor de", valor, "é", valorA)

else:
    print("Resposta não identificada, peço que responda apenas com 'Sucessor' ou 'Antecessor'")

