# Liberação de Saída: 
# O caminhão só pode sair se o checklist == "concluído" 
# E o motorista_identificado == "sim".
# Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

checklist = input("Informe qual o status do Checklist do motorista: ").lower()
motorista_identificado = input("O motorista foi identificado? ").lower()

if checklist == "concluído" or checklist == "concluido" and motorista_identificado == "sim":

    print("Saída Autorizada. Boa Viagem!")
    
else:
    print("Saída Não Autorizada!")