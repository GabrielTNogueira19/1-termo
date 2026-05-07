# Cálculo de Atrasos: 
# Peça o total de entregas agendadas e o total de entregas realizadas com atraso.
# Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar Rotas", caso contrário, "Logística Eficiente".

totalAgendadas = int(input("Informe o total de entregas agendadas: "))
totalRealizadas = int(input("Informe o total de entregas realizadas, porém atrazadas: "))

indice = (totalRealizadas/totalAgendadas)*100

print("Indice de atraso em um total de", indice, "%")

if indice > 10:
    print("Necessário Otimizar Rotas")
else:
    print("Logística Eficiente")
