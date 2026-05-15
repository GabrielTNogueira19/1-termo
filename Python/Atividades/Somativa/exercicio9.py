# Validação de Calibragem: 
# Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

pressao = int(input("Insira a pressão do seu pneu de carga em PSI: "))

if pressao < 100:
    print("ALERTA! Pressão abaixo do recomendado.")

elif pressao >= 100 and pressao <= 110:
    print("Pressão dentro do recomendado!")

else:
    print("ALERTA! Pressão acima do recomendado.")