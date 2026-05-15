# Monitor de Carga: 
# Peça o peso atual de um caminhão em toneladas.
# o Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão". 
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".

peso = float(input("Informe o peso em toneladas de seu veículo: "))

if peso <= 10:
    print("Veículo com Carga Leve")
elif peso > 10 and peso <= 25:
    print("Veículo com Carga Padrão")
else:
    print("ALERTA: Veículo com Excesso de Peso!")