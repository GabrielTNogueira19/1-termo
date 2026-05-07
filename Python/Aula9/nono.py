# # 1. Problema da Idade

# # Errado

# idade = input("Digite sua idade:")

# if idade >= 18:
#     print("Você é maior de idade.")

# # Correção

# idade = int(input("Digite sua idade:"))

# if idade >= 18:
#     print("Você é maior de idade")

# # # Aprimorado

# idade = int(input("Digite sua idade:"))

# if idade >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# # ====================================================================

# # 2. A Escrita Fiel

# # Errado

# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# # Correção

# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# # Aprimorado

# nome = input("Qual é o seu nome? ")
# print(f"Seja bem-vindo, {nome}!")

# # ====================================================================

# # 3. Falta de Espaço

# # Errado

# numero = 10

# if numero > 5:
# print("O número é maior que cinco")
# else:
# print("O número é menor ou igual a cinco")

# # Corrigido

# numero = 10

# if numero > 5:
#     print("O número é maior que cinco")
# else:
#     print("O número é menor ou igual a cinco")

# # Aprimorado

# numero = int(input("Insira um número inteiro: "))

# if numero > 5:
#     print("O número é maior que cinco")
# else:
#     print("O número é menor ou igual a cinco")

# # ====================================================================

# # 4. Esquecimento Fatal

# # Errado 

# usuario = "aluno123"

# if usuario == "aluno123"
#     print("Login realizado com sucesso")

# # Correção

# usuario  = "aluno123"

# if usuario == "aluno123":
#     print("Login realizado com sucesso")

# # ====================================================================

# # 5. Atribuição vs. Comparação

# # Errado

# clima = "ensolarado"

# if clima = "chuvoso":
#     print("Leve um guarda-chuva!")

# # Correção

# clima = "ensolarado"

# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")

# # Aprimorado

# clima = input("O clima está chuvoso ou ensolarado? ")

# if clima == "chuvoso":
#     print("Leve um guarda-chuva!")
# elif clima == "ensolarado":
#     print("Aproveite o dia de sol e passe protetor solar!")
# else:
#     print("Aproveite seu dia sem preocupações!")

# # ====================================================================

# # 6. Misturando Alhos com Bugalhos

# # Errado

# pontos = 50
# print("Parabéns! Você fez" + pontos + "pontos")

# # Corrigido

# pontos = 50
# print(f"Parabéns! Você fez {pontos} pontos")

# # Aprimorado

# pontos = input("Insira a quantidade de pontos que você marcou: ")
# print(f"Parabéns! Você fez {pontos} pontos")

# # ====================================================================

# # 7. A Ordem dos Fatores

# # O sistema deve dar "Excelente" para notas 9 ou 10

# # Errado

# nota = 9.5

# if nota >= 7:
#     print("Aprovado")
# elif nota >= 9:
#     print("Excelente!")

# # Corrigido

# nota = 9.5

# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Aprovado")

# # Aprimorado

# nota = float(input("Digite a nota do aluno: "))

# if nota >= 9 and nota <= 10:
#     print("Excelente!")
# elif nota >= 7 and nota < 9:
#     print("Aprovado")
# elif nota < 7:
#     print("Reprovado")
# else:
#     print("Insira uma nota válida (de 0 a 10)")

# # ====================================================================

# # 8. O Contador de 1 a 5

# # Objetivo: Mostrar na tela os números 1,2,3,4 e 5.

# # Errado

# for i in range(5):
#     print(i)

# # Corrigido

# for i in range(1, 6):
#     print(i)

# # Aprimorado

# import time

# numero_contagem = int(input("Insira até qual número você deseja contar: "))

# for i in range(1, (numero_contagem + 1)):
#     time.sleep(1)
#     print(i)

# # ====================================================================

# # 9. O Loop Eterno

# # O código deveria parar após 3 tentativas

# # Errado

# tentativas = 1

# while tentativas <= 3:
#     print("Tentando conectar...")

# # Corrigido

# tentativas = 1

# while tentativas <= 3:
#     print("Tentando conectar...")
#     tentativas = tentativas + 1

# # Aprimorado

# tentativas = 1

# while tentativas <= 3:
#     print("Tentando conectar...")
#     verificação = input("A conexão foi estabelecida ('sim' ou 'não')? ")

#     if verificação == "sim":
#         print("Conexão Estabelecida...")
#         break
#     else:
#         print("Tentando Novamente")
#         tentativas = tentativas + 1

# if tentativas >= 3:        
#     print("Conexão não estabelecida")

# # ====================================================================

# # 10. A Senha Teimosa

# # O programa deve pedir a senha até que o usuário digite "python123"

# # Errado

# senha = ""

# while senha == "python123":
#     senha = input("Digite a senha secreta: ")

# print("Acesso concedido!")

# # Corrigido

# senha = ""

# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
# print("Acesso Concedido!")

# # Aprimorado

# definicao_senha = input("Defina sua senha de acesso: ")

# senha = ""

# while senha != definicao_senha:
#     senha = input("Digite a senha secreta: ")
# print("Acesso Concedido!")