# Contagem de Embarque: 
# Use um for para fazer uma contagem regressiva de 5 até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

import time

contagem = [5, 4, 3, 2, 1]

for num in contagem:
    print(num)
    time.sleep(1)

print("Portão Trancado!")