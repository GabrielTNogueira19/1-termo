#Atividade 1:
#Mensagem de Boas-Vindas
#Crie um script que use a função print() para exibir a mensagem "Bem-vindo ao mundo da
#programação em Python!".

print("Bem vindo ao mundo da programação em Python")

print(" =========================================================================================================")
# Atividade 2: 
# Informações Pessoais
# Escreva um programa que imprima seu nome completo em uma linha e sua idade em outra linha.
# -Exemplo de saída:
# -Fulano de Tal
# -30

nome  =  input("Qual o seu nome completo? ")
idade =  int(input("Qual a sua idade? "))

print(nome)
print(idade)

print(" =========================================================================================================")
# =========================================================================================================

# Atividade 3: 
# Calculadora de Soma e Subtração
# Crie um script que exiba o resultado da soma de 135 com 246 e o resultado da subtração de 512
# por 128. Cada resultado deve ser exibido em uma linha separada.
# ● Dica: Use o print() diretamente com os operadores (print(135 + 246)).
# ● Obs: Realize também a mesma situação com variáveis

print("O resultado da soma de 135 com 246 é:", 135 + 246)
print("O resultado da subtração de 512 por 128 é:", 512 - 128)

sinal = input("Digite o sinal da operação que deseja realizar ('+' ou '-')")

if sinal == "+":
        
    v1 = float(input("Digite o primeiro valor que você deseja somar: "))
    v2 = float(input("Digite o segundo valor que você deseja somar: "))

    soma = v1 + v2

    print("A soma de seus valores é igual a: ", soma)

elif sinal == "-":
        
    v1 = float(input("Digite o primeiro valor que você deseja subtrair: "))
    v2 = float(input("Digite o segundo valor que você deseja subtrair: "))

    subtração = v1 - v2

    print("A subtração de seus valores é igual a: ", subtração)

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 4: 
# Multiplicação e Divisão
# Escreva um programa que mostre o resultado da multiplicação de 15 por 8 e o resultado da
# divisão de 78 por 3.

print("O resultado da multiplicação de 15 por 8 é:", 15*8)
print("O resultado da divisão de 78 por 3 é:", 78/3)

sinal = input("Digite o sinal da operação que deseja realizar ('*' ou '/')")

if sinal == "*":
        
    v1 = float(input("Digite o primeiro valor que você deseja multiplicar: "))
    v2 = float(input("Digite o segundo valor que você deseja multiplicar: "))

    multiplicação = v1 * v2

    print("A multiplação de seus valores é igual a: ", multiplicação)

elif sinal == "/":
        
    v1 = float(input("Digite o primeiro valor que você deseja dividir: "))
    v2 = float(input("Digite o segundo valor que você deseja dividir: "))

    divisão = v1 / v2

    print("A soma de seus valores é igual a: ", divisão)

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 5:
# Potenciação
# Calcule e exiba o resultado de "5 elevado à 3a potência" (53).
# ● Dica: O operador de potenciação em Python é **.

print("O resultado de 5 elevado à 3ª potência é igual a:", 5**3)

v1 = float(input("Digite o valor que você deseja elevar: "))
v2 = float(input("Digite o valor do seu expoente: "))

print("O valor final de sua potenciação é", v1**v2)

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 6: 
# Concatenando Palavras
# Crie um script que declare o seu primeiro nome em uma string e seu sobrenome em outra. Use
# o operador + para concatenar (juntar) as duas strings e exibir seu nome completo.
# ● Exemplo: print("Maria" + " " + "Silva")

pNome = input("Digite o seu primeiro nome: ")
uNome = input("Digite o seu último sobrenome: ")

print("Seu nome é", pNome + " " + uNome)

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 7: 
# Cálculo de Eficiência (OEE)
# ● Peça a quantidade de peças produzidas e a quantidade de peças defeituosas. Calcule
# e exiba a taxa de aproveitamento (peças boas / total).

qPeca = int(input("Insira a quantidade de peças produzidas: "))
qDefeituosa = int(input("Insira a quantidade de peças defeituosas: "))

taxa = (qPeca - qDefeituosa) / qPeca

print("Sua taxa de aproveitamento convertida para porcentagem é de", taxa*100, "%")

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 8: 
# Descrição com Cálculos
# Crie um script que exiba a seguinte frase, substituindo os cálculos pelos seus resultados:
# "Eu tenho 25 anos e, em 10 anos, terei 35 anos."
# ● Dica: Use a vírgula dentro do print() para combinar strings e cálculos.
# ● Ex: print("Texto", 25 + 10).

idade = int(input("Digite sua idade: "))

print("Você tem", idade, "anos, em 10 anos você terá", idade+10)

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 9: 
# Orçamento de Viagem (Cálculo com float)
# Imagine que você está planejando uma viagem. O custo do hotel é de R$ 250.50 por noite e
# o custo da passagem é R$ 412.00. Calcule e exiba o custo total para uma viagem por noites.
# ● Ex: Fórmula: (custo_hotel * 3) + custo_passagem

valorNoite = float(input("Insira o custo do hotel por noite: "))
qDias = int(input("Insira quantos dias vai durar a sua viagem: "))
valorPassagem = float(input("Insira o valor de sua passagem: "))

total = (valorNoite*qDias) + valorPassagem

print("Seu orçamento ficou em um total de", total, "reais")

print(" =========================================================================================================")
# =========================================================================================================]

# Atividade 10: 
# Desafio - Mini Relatório
# Crie um script que imprima um pequeno relatório. Use print() várias vezes para formatar a
# saída de forma organizada.
# ● Exemplo de saída:

# ==========================
# Relatório de Vendas
# ==========================
# Produto: Notebook Gamer
# Quantidade vendida: 15
# Preço unitário: R$ 5499.50
# Total de vendas: R$ 82492.50
# ==========================

produto = input("Insira o nome do produto: ")
qVendida = int(input("Insira a quantidade de produtos vendidos: "))
preco = float(input("Insira o valor de cada unidade: "))
total = qVendida*preco

print("==========================")
print("Relátorio de Vendas")
print("==========================")
print("Produto:", produto)
print("Quantidade de Vendas:", qVendida)
print("Preço Unitário:", preco)
print("Total de Vendas:", total)
print("==========================")

    
