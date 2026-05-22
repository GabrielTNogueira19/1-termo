# -Contexto
# O Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho
# (SESMT) precisa automatizar o controle de treinamentos obrigatórios (como CIPA,
# Brigada de Incêndio e NR-35) e a entrega de Equipamentos de Proteção Individual (EPIs).

# -Objetivo
# Desenvolva um programa em Python que gerencie o status de conformidade dos
# funcionários de uma empresa.

# Requisitos Funcionais:
# RF01 - O sistema deve armazenar o nome, setor e o status dos treinamentos (NR-10, NR-35 e Brigada).
# RF02 - Se o setor for "Elétrica", o sistema deve listar a obrigatoriedade de luvas de alta tensão e botas dielétricas.
# RF03 - Se o setor for "Trabalho em Altura", o sistema deve listar a obrigatoriedade de cinturão de segurança e talabarte.
# RF04 - Se o treinamento tiver mais de 2 anos, o sistema deve exibir a mensagem: "Treinamento Vencido! Encaminhar para reciclagem". Caso contrário, exiba: "Treinamento Válido."
# RF05 - O sistema deve exibir na tela um resumo com o total de funcionários cadastrados e quantos estão com treinamentos em dia.
quantidade_cadastros = 0
setor_eletrica = 0
setor_trabalho_altura = 0
setor_brigada = 0
funcionarios_validos = 0
funcionarios_nao_validos = 0
ano_atual = 2026


def verificando_treinamento():
        
        global funcionarios_validos, funcionarios_nao_validos

        print("Menu de Treinamentos")
        print("1 - NR-10")
        print("2 - NR-35")
        print("3 - Brigada")
        escolha_treinamento = input("Qual tipo de treinamento foi realizado: ")

        ano_treinamento = int(input("Digite em qual ano foi seu último treinamento: "))
        if ano_treinamento > ano_atual:
            print("Por favor, insira um ano váido!")
        else:
            tempo_treinamento = ano_atual - ano_treinamento
            if tempo_treinamento <= 2 and tempo_treinamento >= 0:
                status_treinamento = "Válido"
                funcionarios_validos += 1
            else:
                status_treinamento = "vencido"
                funcionarios_nao_validos += 1

            if status_treinamento == "Válido":
                if escolha_treinamento == "1":
                    treinamento = "NR-10"
                if escolha_treinamento == "2":
                    treinamento = "NR-35"
                if escolha_treinamento == "3":
                    treinamento = "Brigada"
                print("Treinamento encontra-se Válido.")
            else:
                print(f"Seu último treinamento de {treinamento} foi a {tempo_treinamento} anos. Treinamento encontra-se Vencido! Encaminhando para reciclagem.")

def cadastro_funcionário():

    global setor_eletrica, setor_trabalho_altura, setor_brigada

    nome_funcionario = input("Digite o nome do funcionário: ")
    if nome_funcionario == "":
        print("Por favor digite um nome para cadastrar")
    else:
        print("Menu de Setores")
        print("1 - Setor de Elétrica")
        print("2 - Setor de Trabalho em Altura")
        print("3 - Setor de Brigada")
        setor_epi = int(input("Digite o setor que o funcionário trabalha: "))
        if setor_epi == 1:
            setor_eletrica += 1
        elif setor_epi == 2:
            setor_trabalho_altura += 1
        elif setor_epi == 3:
            setor_brigada += 1
        else:
            print("Por favor digite um setor válido para cadastrar")

        # o status dos treinamentos (NR-10, NR-35 e Brigada).
        print("Menu de Treinamentos")
        print("1 - NR-10")
        print("2 - NR-35")
        print("3 - Brigada")
        treinamento = input("Qual tipo de treinamento será realizado: ")

        print("Cadastro Concluído")

print("Bem Vindo ao Sistema de Controle de Treinamentos do SESMT")
while True:
    
    print("=======================================")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar EPIs por Setor")
    print("3 - Verificar Status do Treinamento")
    print("4 - Resumo dos Funcionários")
    print("5 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        cadastro_funcionário()

    elif opcao == "2":
        print("Menu de Setores")
        print("1 - Setor de Elétrica")
        print("2 - Setor de Trabalho em Altura")

        setor_epi = input("Digite o setor que deseja consultar os EPIs: ")

        if setor_epi.lower() == "1":
            print("Lista de EPIs para o setor de 'Elétrica'")
            print("# Luvas de alta tensão")
            print("# Botas dielétricas.")

        elif setor_epi.lower() == "2":
            print("Lista de EPIs para o setor de 'Trabalho em Altura'")
            print("# Cinturão de segurança")
            print("# Talabarte")
        else:
            print("Por favor digite um setor válido para verificar")

    elif opcao == "3":
        verificando_treinamento()

    elif opcao == "4":
        print("Resumo Geral")
        print(f"Funcionários Cadastrados: {quantidade_cadastros}")
        print(f"Funcionários no setor de 'Elétrica': {setor_eletrica}")
        print(f"Funcionários no setor de 'Trabalho em Altura': {setor_trabalho_altura}")
        print(f"Funcionários no setor de 'Brigada': {setor_brigada}")
        print(f"Funcionários com treinamento válido: {funcionarios_validos}")
        print(f"Funcionários com treinamento não válido: {funcionarios_nao_validos}")

    elif opcao == "5":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")