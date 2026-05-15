# Gerenciador de Combustível: 
# Comece com um tanque de 500 litros. 
# Crie um menu (while) onde o usuário pode:
# (1) Abastecer o tanque da base,
# (2) Retirar combustível para um caminhão 
# (3) Sair. 
# Se o tanque da base ficar abaixo de 50 litros, avise: "Reserva Crítica!".

print("GERENCIADOR DE COMBUSTÍVEL")
print("MENU")
print("(1) Abastecer o tanque da base")
print("(2) Retirar 105 litros de combustível para um caminhão")
print("(3) Sair")

opção = 0
tanque = 500

while opção != 3:

    opção = int(input("Insira a opção desejada: "))

    if opção == 1:
        tanque = 500
        print(f"O tanque possui {tanque} litros")

    elif opção == 2:
        tanque = tanque-55
        print(f"O tanque possui {tanque} litros")
        if tanque < 50:
            print("Reserva Crítica! Abasteça.")
            break

print("Sistema Encerrado")
        


