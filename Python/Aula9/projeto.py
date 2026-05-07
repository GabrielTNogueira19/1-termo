total_vagas = 500
vagas_disponiveis = 500
vagas_ocupadas = total_vagas - vagas_disponiveis

posicao_ticket = 0
posicao_tag = 0
numero_ticket = []
numero_tag = []



from time import sleep

while True:

    print("=====================")
    print("Bem Vindo ao Shopping Center!")
    print("= Menu de Opções =")
    print("1- Entrar no estacionamento.")
    print("2- Sair do estacionamento")
    
    opcao_escolhida = int(input("Insira o número da opção que deseja realizar: "))

    if opcao_escolhida == 1:

        print("=====================")
        print(f"Temos um total de {vagas_disponiveis} vagas disponíveis!")
        print("= Menu de Acesso =")
        print("1- TAG (Sem Parar/ConectCar).")
        print("2- Via Ticket")
        opcao_acesso = input("Insira o método de acesso que deseja utilizar: ")

        if opcao_acesso == "1" or opcao_acesso.lower() == "TAG":
            estado_TAG = input("Informe se status da TAG está como ativo (sim/não): ")

            if estado_TAG.lower() == "sim":
                
                horario_entrada = float(input("Informe o horário de entrada do veículo: "))
                posicao_tag = int(input("Informe o código da TAG: "))
                print("Horário de entrada registrado! Ao sair o valor sera debitado automaticamente conforme o tempo permanecido.")
                print("Aproveite sua visita ao Shopping Center!")
                print("Abrindo Cancela!")
                vagas_disponiveis -= 1
                vagas_ocupadas += 1
                numero_tag.insert(posicao_tag, horario_entrada)
            
            elif estado_TAG.lower() == "não":

                print("TAG não ativa, por favor tente ativar a TAG e voltar outro horário!")
            
            else: 
                print("Digite uma opção válida")
        
        elif opcao_acesso == "2" or opcao_acesso.lower() == "ticket":
            
            if vagas_disponiveis > 0:
                horario_entrada = float(input("Informe o horário de entrada do veículo: "))
                print("Por favor pressione o botão para receber o ticket!")
                sleep(1)
                print("== Ticket Impresso ==")
                print(f"Número de emissão do ticket: {posicao_ticket}")
                print(f"Horário de entrada: {horario_entrada}")
                print("Ticket impresso!")
                print("ATENÇÂO! Caso ocorra a perda do Ticket, um valor de R$50,00 será cobrado!")
                print("Aproveite sua visita ao Shopping Center!")
                print("Abrindo Cancela!")
                vagas_disponiveis -= 1
                vagas_ocupadas += 1
                numero_ticket.insert(posicao_ticket, horario_entrada)
                posicao_ticket += 1
                
            if vagas_disponiveis == 0:

                print("Por favor aguarde até que uma vaga para ticket seja liberada!")

    elif opcao_escolhida == 2:

        if vagas_ocupadas > 0:

            print("=====================")
            print("= Menu de Acesso =")
            print("1- TAG (Sem Parar/ConectCar).")
            print("2- Via Ticket")
            opcao_saida = int(input("Insira o método de acesso utilizado na entrada: "))

            if opcao_saida == 1:
                valor_tag = int(input("Informe o código da TAG: "))
                horario_saida = float(input("Informe o horário de saida do veículo: "))
                emissao_tag = numero_tag[valor_tag]
                horas_permanecidas = horario_saida - emissao_tag 

                if horas_permanecidas <= 0.25:
                    valor_a_pagar = 0

                elif horas_permanecidas <= 3:
                    valor_a_pagar = 15
                else:
                    horario_adicional = horas_permanecidas - 3 
                    valor_a_pagar = 15 + (horario_adicional*3)
                
                print(f"Sua visita ficou em um total de R${valor_a_pagar}")
                print("O valor será debitado de sua fatura")
                print("Obrigado pela visita. Volte sempre!")
                                
            elif opcao_saida == 2:
                
                ticket_apresentado = input("Ainda possui o ticket? (sim/não) ")

                if ticket_apresentado.lower() == "sim":

                    valor_ticket = int(input("Apresente o número de emissão do seu ticket: "))
                    horario_saida = float(input("Informe o horário de saida do veículo: "))
                    emissao_ticket = numero_ticket[valor_ticket]
                    horas_permanecidas = horario_saida - emissao_ticket 

                    if horas_permanecidas <= 0.25:
                        valor_a_pagar = 0
                    elif horas_permanecidas <= 3:
                        valor_a_pagar = 15
                    else:
                        horario_adicional = horas_permanecidas - 3 
                        valor_a_pagar = 15 + (horario_adicional*3)

                    print(f"Sua visita ficou em um total de R${valor_a_pagar}")
                    print("Por favor fague o valor na cabina de saída.")
                    sleep(1)
                    ticket_pago = input("O ticket foi pago? (sim/não) ")
                    if ticket_pago.lower() == "sim":

                        print("Obrigado pela visita. Volte sempre!")
                    
                    else:
                        print("Por favor pague o ticket e tente sair novamente!")

        else:
            print("Nenhum carro estácionado. Tente novamente!")
