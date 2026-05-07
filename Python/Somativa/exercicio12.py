# Monitoramento de Frota: 
# Use um for para pedir a quilometragem de 5 veículos diferentes.
# Ao final, mostre qual foi a maior quilometragem registrada.

veiculos = ["veiculo1", "veiculo2", "veiculo3", "veiculo4", "veiculo5"]

maior = 0

for carro in veiculos:
    carro = float(input(f"Insira a quilometragem do {carro}: "))
    
    if carro > maior:
        maior = carro

print(f"A maior quilometragem registrada foi de {maior} Km")