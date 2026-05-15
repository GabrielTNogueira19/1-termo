# Média de Entrega: 
# Peça o tempo de entrega (em horas) de 3 rotas diferentes realizadas por um motorista. 
# Exiba a média aritmética simples do tempo dessas entregas.

print("CALCULADOR DE MÉDIA DE ENTREGA")

entrega1 = int(input("informe o tempo de entrega referente a 1ª rota (em horas): "))

entrega2 = int(input("Informe o tempo de entrega referente a 2ª rota (em horas): "))

entrega3 = int(input("Informe o tempo de entrega referente a 3ª rota (em horas): "))

media = float((entrega1+entrega2+entrega3)/3)

print("A média de entrega das 3 rotas foi de", media, "horas")