# # Tipos de dados
# # Int
# # Float

# x = 10
# y = 5.15

# # Números (int e float)
# print(10)
# print(5.15)

# # Texto (str ou string)
# print("Meu nome é Gabriel")

# # Concatenar
# print('eu gosto de programar \n' + 'Python')

# # Contas

# n1 = 10
# n2 = 5

# print('os valores são', n1 + n2)

# # Operadores Matemáticos

# # + = soma
# # - = subtração
# # * = multiplicação
# # / = divisão
# # ** = expoente

# # Exemplo 2

# n1 = 20
# n2 = 10

# print("os valores são", n1 * n2)

# # Exemplo 3
# n2 = input('Digite o seu primeiro número: ')
# print('Seu primeiro número foi: \n', n2)

# # Exemplo 4

nome  = input('Qual é seu nome? \n')
print('Seu nome é: \n', nome) #Aqui fica mais completo e explicativo
print(nome) #Aqui fica mais simples

# # Exemplo 5

# # responder 2 perguntas
# # 1º Qual seu é curso?
# # 2º Qual é sua idade?

curso = input('Qual é seu Curso? \n')
print('Seu curso é: \n', curso)

idade = input('Qual a sua idade? \n')
print('Sua idade é: \n', idade)

# # Exemplo 6A 

base = 10 
altura = 5
area = (base*altura)/2
print(area)

# # Exemplo 6B
# # Com informações

base = float(input('informe o valor da base \n'))
altura = float(input('informe o valor da altura \n'))
area = (base*altura)/2
print('Sua area é igual a: \n', area)

# Exercício 1
# Criar uma calculadora com os operadores

valor1 = float(input('insira o primeiro valor: \n')) 
valor2 = float(input('insira o segundo valor: \n'))
operação = input('insira o sinal da operação desejada: \n')

if operação == "+":
    resultado= valor1+valor2
elif operação == "-":
    resultado= valor1-valor2
    


print('O resultado da operação é: \n', resultado)

# Exercício 2
# Calculadora de IMC

peso = float(input('Qual o seu peso? \n'))
altura = float(input('Qual sua altura? \n'))

IMC = peso/(altura**2)
print('Este é seu IMC(indice de massa corporal):', IMC )

# Exercício 3
# O Crachá

nome= input('Insira seu nome: \n')
idade= int(input('Insira sua idade: \n'))
profissao= input('Insira sua profissão, ou se for o caso "Estudante": \n')

print('Olá, meu nome é', nome, 'tenho', idade, 'anos e sou', profissao)




