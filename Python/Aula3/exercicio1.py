# Exercício 1
# crie um algoritmo que simule uma calculadora q que por opção de escolha permita calcular os operadores

print("Bem vindo a minha calculadora!")

print("Escolha uma opção de cálculo dentre as abaixo: ")
print("+ = Soma")
print("- = Subtração")
print("/ = Divisão")
print("* = Multiplicação")

operador = input("Digite qual operação você deseja realizar: ")

if operador == "+" or "soma":
    v1Soma = float(input("Digite o primeiro valor para o calculo: "))
    v2Soma = float(input("Digite o segundo valor para o calculo: "))

    resultadoSoma = v1Soma+v2Soma

    print("O resultado foi: ", resultadoSoma)

elif operador == "-" or "subração":
    v1Subtração = float(input("Digite o primeiro valor para o calculo: "))
    v2Subtração = float(input("Digite o segundo valor para o calculo: "))

    resultadoSubtração = v1Subtração-v2Subtração

    print("O resultado foi: ", resultadoSubtração)

elif operador == "*" or "multiplicação":
    v1Multiplicação = float(input("Digite o primeiro valor para o calculo: "))
    v2Multiplicação = float(input("Digite o segundo valor para o calculo: "))

    resultadoMultiplicação = v1Multiplicação*v2Multiplicação

    print("O resultado foi: ", resultadoMultiplicação)

elif operador == "/" or "divisão":
    v1Divisão = float(input("Digite o primeiro valor para o calculo: "))
    v2Divisão = float(input("Digite o segundo valor para o calculo: "))

    resultadoDivisão = v1Divisão/v2Divisão

    print("O resultado foi: ", resultadoDivisão)

else:
    print("Você não escolheu nenhuma das opções. Escolha uma opção dentre as disponiveis. Tente novamente.")