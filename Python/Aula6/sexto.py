# Lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 90, 85, 80, 55, 50, 52, 30, 20, 15, 10, 5]
# baixos = [55, 50, 52, 30, 20, 15, 10, 5]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}ºC detectado! Acionando parada de emergência!")
#         break
            
#     elif temp < 50 and temp > 10:
#         print("ALERTA! Temperatura está diminuindo. Cuidado!")
#     elif temp <= 10:
#         print(f"CRÍTICO: {temp}ºC detectado! Acionando parada de emergência!")
#         break

#     print(f"Temperatura está em {temp}ºC. Sistema operando.")

# print("Sistema desligado. Aguardando manutenção.")

# # segundo jeito:
# import time
# leituras = [70, 75, 82, 98, 90, 85, 80, 55, 50, 52, 30, 20, 15, 10, 5]

# for temp in leituras:
#     while temp < 100 and temp >= 10:
#         for temp in leituras:
#             if temp < 50 and temp > 10:
#                 print("ALERTA! Temperatura está diminuindo. Cuidado!")
#             else: 
#                 print(f"Temperatura está em {temp}ºC. Sistema operando.")

#             time.sleep(0.5)
#     break

# print(f"CRÍTICO: {temp}ºC detectado! Acionando parada de emergência!")

# ==================================================================================================

# Exemplo 2:
 
materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]

for peca in materiais:
    if peca != "metal":
        print(f"AVISO: Peça de {peca} detectada. Descartando")
        continue
    print(f"Processando peça de {peca}. Furando e polindo")

print("Fim do lote de produção")
# ==================================================================================================
# Exercício 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha no sensor específica no item 5)
# import time

# for i in range (1, 11):
#     time.sleep(0.5)
#     if i == 5:
#         print(f"Falha no sensor de número {i}")
#         continue
#     print(f"Sensor de número {i} funcionando corretamente")

# print("Fim dos testes")

# ==================================================================================================

# Exercício 2
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa
# import time

# for i in range (10):

#     time.sleep(0.5)
#     print("Verde")
# print("Siga em frente")

# for i in range (5):

#     time.sleep(0.5)
#     print("Amarelo")
# print("Cuidado")

# for i in range (8):

#     time.sleep(0.5)
#     print("Vermelho")
# print("Espere")

# Exercício 3 - Soma de Cargas de Energia (for)
# Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kWh de cada uma das 5 máquinas. 
# Ao final do loop, o programa deve exibir o consumo total da fábrica.

maquinas = ["Máquina1", "Máquina2", "Máquina3", "Máquina4", "Máquina5"]

kWh = 0

for i in maquinas:
    kWh = kWh + int(input(f"Insira a quantidade de kWh consumidos pela {i}:"))

print("O consumo total de kWh foi de", kWh)