# Cálculo de Autonomia:
# Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l).
# Calcule e exiba a distância total que o veículo pode percorrer com o tanque cheio.

print("CÁLCULO DE AUTONOMIA")

litros = float(input("Insira a capacidade máxima do seu tanque de combustível (em litros): "))
consumo = float(input("Insira o consumo médio seu veículo (Km/L): "))

print("Com o tanque cheio seu carro pode percorrer", consumo*litros, "Km")