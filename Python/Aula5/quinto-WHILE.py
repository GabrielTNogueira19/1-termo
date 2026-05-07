# 2. O Laço 'while' (Repetições Indeterminadas)
# Use o whle quando  você não sabe quando vai parar, Ele depende de uma condição (como um sensor de segurança ou um botão de emergêcia)

# ===========================================================================================================

# Exemplo 1: Monitor de Temperatura
# Repete enquanto a temperatra estiver segura
# import time

# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura Atual: {temperatura} ºC. Sistema operando...")
#     time.sleep(1)
#     temperatura += 3 #Simulando o aumento de temperatura do sistema
# print("ALERTA! Temperatura atingiu o limite. Desligando o motor...")

# ===========================================================================================================

# Exemplo 2: Menu de Interação

# lower  = Minúsculo
# upper = Maiúsculo

# opcao = ""

# while opcao != "sair" and "SAIR":
    
#     opcao = input("Digite a leitura do sensor ou 'sair' para fechar: ").upper() .lower()

#     if opcao != "sair" and "SAIR":
#         print(f"Dado '{opcao}' registrado no Banco de Dados.")

# print("Sistema Encerrado.")

# ===========================================================================================================

# Exercício 1:
# Monitor de Pressao Crítica

# pressao = 0

# while pressao < 100:
    
#     pressao = int(input("Digite a pressão atual do compressor: "))
#     print(f"PSI atual: {pressaoo} ºC. Compressor segue atuando...")

# print("ALERTA! Pressão crítica atingida. Desligando o Sistema.")

# ===========================================================================================================

# Exercício 2:

serie = ""

print("Menu de Series: ")
print("Opção 1 - Serie fulano")
print("Opção 2 - Serie fulano d tal")
print("Opção 3 - Serie ciclano")
print("Opção 4 - Serie Ciclano e flunano")
print("Opção 5 - SAIR")

while serie == "1" or "2" or "3" or "4":

    serie = input("Escolha uma dentre as series acima: ").lower()

    if serie == "1":

        print("Você escolheu 'Serie Fulano' para assistir.")
    elif serie == "2":
        print("Você escolheu 'Serie Fulano d tal' para assistir.")
    elif serie == "3":
        print("Você escolheu 'Serie ciclano' para assistir.")
    elif serie == "4":
        print("Você escolheu 'Serie ciclano e fulano' para assistir.")
    else:
        break
print("Sistema Encerrado.")