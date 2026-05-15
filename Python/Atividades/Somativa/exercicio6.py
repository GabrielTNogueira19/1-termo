# Classificador de Destino: 
# O usuário insere o código da carga.
# Se começar com "N", exiba "Região Norte". 
# Se começar com "S", "Região Sul". 
# Para qualquer outro, "Região Internacional".

print("CLASSIFICADOR DE DESTINO")

print("Menu de Destino")
print("Iníco com 'N' = Região Norte")
print("Iníco com 'S' = Região Sul")
print("Para qualquer outro início será definido como 'Região Internacional'")

codigo = input("Insira o início do código da carga: ").upper()

if codigo == "S":
    print("Carga com destino para a Região Sul")
elif codigo == "N":
    print("Carga com destino para a Região Norte")
else:
    print("carga com destino para Região Internacional")
