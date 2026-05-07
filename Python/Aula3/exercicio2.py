print("Bem vindo ao calculador de idade")

nome = input("Insira o seu nome: ")
curso = input("Insira o seu curo: ")
ano = int(input("Insira o seu ano de nascimento: "))
anoAtual = int(input("Em qual ano estamos: "))

idade = anoAtual-ano
print("Olá", nome, "do curso de", curso, "você tem ou fará", idade, "anos")