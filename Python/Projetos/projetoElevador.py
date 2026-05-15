# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térro o andar 0. O elevador pode se mover para cima ou para baixo, e tem capacidade para 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar de destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador e as ações realizadas (subindo, descendo, parando).
# O programa deve continuar rodando até que o usuário decida encerrar.
# 
# requisitos funcionais:
# 1. O programa deve permitir que o elevador contenha no máximo 5 pessoas.
# 2. O programa deve permitir que o usuário chame o elevador para um andar específico.
# 3. O programa deve permitir que o usuário escolha um andar de destino após entrar no elevador.
# 4. O programa deve exibir mensagens indicando o andar atual, o número de pessoas no elevador e as ações realizadas (subindo, descendo, parando).
# 5. O programa deve continuar rodando até que o usuário decida encerrar.
# 6. O elevado deve começar no andar 0.

# requisitos não funcionais:
# 1. O sistema deve impedir que o usuário digite um andar menor que 0 ou maior que 10.

# Código:
# =================================================================================================================================
from time import sleep
andar_desejado = 0
andar_atual = 0
quantidade_pessoas = 0

def subindo(andar_desejado):

    global andar_atual

    print(f"Elevadador saindo do andar {andar_atual} e subindo até o andar {andar_desejado}!")
    andares_andados = andar_desejado - andar_atual
    passando = andar_atual
    sleep(1)
    for i in range(andares_andados):
        passando += 1
        print(f"----- Andar {passando}")
        sleep(1)
    print(f"Você chegou ao andar {andar_desejado}")
    andar_atual = andar_desejado
    # return andar_atual
    
def descendo(andar_desejado):

    global andar_atual

    print(f"Elevadador saindo do andar {andar_atual} e descendo até o andar {andar_desejado}!")
    andares_andados =  andar_atual - andar_desejado
    passando = andar_atual
    sleep(1)
    for i in range(andares_andados):
        passando -= 1
        print(f"----- Andar {passando}")
        sleep(1)
    print(f"Você chegou ao andar {andar_desejado}")
    andar_atual = andar_desejado
    # return andar_atual

def contando_pessoas():
    global quantidade_pessoas

    saiu_pessoas = int(input("Insira a quantidade de pessoas que sairam: "))
    entrou_pessoas = int(input("Insira a quantidade de pessoas que entraram: "))
    
    if saiu_pessoas > 6:
        print("Insira um valor válido, o elevador não pode conter mais de 5 pessoas!")
    
    elif entrou_pessoas < 0 and saiu_pessoas < 0:
        print("Insira um valor válido, o número de pessoas que entraram não pode ser negativo!")

    else:
        quantidade_pessoas = quantidade_pessoas - saiu_pessoas
        quantidade_pessoas = quantidade_pessoas + entrou_pessoas

        if quantidade_pessoas > 5:
            
            pessoas_a_mais = quantidade_pessoas - 5
            print(f"Capacidade máxima exedida, será necessária a saida de {pessoas_a_mais} pessoas")
        else:
            pass


print("Você Está Entrando no Elevador!")
quantidade_pessoas = int(input("Insira a quantidade de pessoas no elevador: "))

while True:

    # quantidade_pessoas = int(input("Insira a quantidade de pessoas no elevador: "))
    if quantidade_pessoas > 5:
        print("Elevador com capacidade máxima atingida, por favor espere até que alguém desça do elevador! ")
        while quantidade_pessoas > 5:
            quantidade_pessoas = int(input("Insira a quantidade de pessoas no elevador: "))
    else:
        print("===================")
        print(f"Elevador com {quantidade_pessoas} pessoas!")
        print(f"Andar atual: {andar_atual}")
        print("Painel de andares:")
        print(" |T |1 |2 | \n |3 |4 |5 | \n |6 |7 |8 | \n |- |9 |- | ")
        # print("|4 |5 |6 |")
        # print("|7 |8 |9 |")
        # print("|- |10|- |")
        andar_desejado = input("Insira o andar que deseja se mover ou digite 'sair' para encerrar o sistema: ")


        if andar_desejado.lower() == "sair":
            print("Você está encerrando o sistema!")
            break
        elif andar_desejado.lower() == "t":
            andar_desejado = 0
        else:
            andar_desejado = int(andar_desejado)

        if andar_desejado > 9 or andar_desejado < 0:
            print("Insira um andar válido de acordo com o painel!")
        elif andar_desejado > andar_atual:

            subindo(andar_desejado)
            contando_pessoas()

        elif andar_desejado < andar_atual:

            descendo(andar_desejado)
            contando_pessoas()
        else:
            print("Você já está no andar desejado!")

# =================================================================================================================================