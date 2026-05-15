# Relatório de Inspeção de Pneus:
# Use um for para processar 5 pneus.
# Para cada um, peça a profundidade do sulco (em mm).
# Se o pneu for aprovado (maior ou igual a 1.6mm), conte-o.
# No final do loop, exiba o total de pneus aprovados e a porcentagem de conformidade da frota.

contagem = 0
total = 5

for pneu in range(1, 6):

    medida = float(input(f"Digite a medida do sulco do pneu {pneu} em mm: "))

    if medida >= 1.6:
        contagem = contagem+1
        print("Pneu aprovado e adicionado a contagem geral.")

    else:
        print("Pneu fora das medidas regulares, não foi adicionado a contagem.")
        pass

porcentagem = (contagem/total)*100
print(f"Tiveram {contagem} pneus aprovados hoje com uma porcentagem de {porcentagem}% de comformidade")