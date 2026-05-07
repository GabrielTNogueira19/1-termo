# 1. O laço "for" (Repetições Determinadas)
# Use o "for" quando você sabe exatamente quantas vezes algo  deve acotecer (como ler 10 sensores ou processar uma lista de peças).

# ===========================================================================================================

# Exemplo: Relatório de Produção diária
# Imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um:
# Exemplo 1:

# for lote in range(1, 6):
#     print(f"Processando lote número {lote} ... ")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada")

# Imagine que você queira atingir uma meta de produção de 5 carros e numera-los

# for carros in range(1, 6):
#     print(f"produzindo carro número {carros}...")

# ===========================================================================================================

# Exemplo 2:

# for i in range(5):

#     print(i)

# ===========================================================================================================

# Exemplo 3:

# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tiposPecas = ["Barra Dentada", "Porca do Eixo", "Anél Externo", "Parafuso Phillips", "Martelo Cabeça Chata"]

# for item in pecas:

#     print(f"Item em estoque: {item} + {tiposPecas}")

# ===========================================================================================================

# # Exemplo 4:

# pecas = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tiposPecas = ["Barra Dentada", "Porca do Eixo", "Anél Externo", "Parafuso Phillips", "Martelo Cabeça Chata"]

# print("Loja de peças")
# print("Bem-Vindo")
# print("Escolha entre as opções:")
# print("1 - Peças")
# print("2 - Tipos de Peças")

# opcao = input("Digite uma das opções:" )

# if opcao == "1":
#     for itemP in pecas:

#         print(f"Item em estoque: {itemP}")
#     print("Fim da Lista")
# elif opcao == "2":
#     for item in tiposPecas:

#         print(f"Item em estoque: {item}")
#     print("Fim da Lista")
# else:
#     print("Por favor escolha dentre as opções disponiveis. Tente Novamente.")

# ===========================================================================================================

# Exercício 1:
# 1. Contador de produção
# Uma esteira processa 10 peças por ciclo. Crie um programa que use um 'for' para contar de 1 a 10 e, para cada número imprima:
# "Peça Nº X processada com Sucesso"
# No final, exiba: "Ciclo de produção conclído"

# print("Contador de produção")

# for ciclo in range(1, 11):
#     print(f"Peça Nº {ciclo} processada com Sucesso...")
# print("Ciclo de produção concluído")

# ===========================================================================================================

# Exercício 2:
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas Banana, Manga, Melancia, Abacaxi.
# Com quantidade de 10 bananas, 5 mangas, 10 melancias e 12 abacaxis.

# print("Selecione qual fruta deseja consultar:")
# print("1 - Banana")
# print("2 - Manga")
# print("3 - Melancia")
# print("4 - Abacaxi")


# fruta = input("Digite o número referente a qual fruta voce deseja consultar: ")

# if fruta == "1":

#     for banana in range(10):
#         print(f"{banana +1} Banana")
#     print("Quantidade total = 10")

# if fruta == "2":

#     for manga in range(5):
#         print(f"{manga +1} Manga")
#     print("Quantidade total = 5")

# if fruta == "3":

#     for melancia in range(10):
#         print(f"{melancia +1} Melancia")
#     print("Quantidade total = 10")

# if fruta == "4":

#     for abacaxi in range(13):
#         print(f"{abacaxi +1} Abacaxi")
#     print("Quantidade total = 13")

# ===========================================================================================================

# Exercício 3:

# tabuada = int(input("Digite qual tabuada você deseja consultar: "))
# print("A tabuada do", tabuada, "é: ")
# for numero in range(1, 11):
#     print(f"{tabuada}x{numero} = {tabuada*numero}")