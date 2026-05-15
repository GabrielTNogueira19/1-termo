# Sistema de Rastreio: 
# Crie um while que peça o código de acesso do rastreador ("track99").
# Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se esgotar, exiba "Rastreamento Bloqueado".

erros = 0
tentativas = 3

while erros != 3:

    codigo = input("Insira o código de acesso do rastreador: ")

    if codigo != "track99":
        erros = erros+1
        tentativas = tentativas-1
        print(f"Código incorreto. Tente novamente. Você tem mais {tentativas} tentativas")

    else:
        break

if erros == 3:
    print("Rastreamento Bloqueado. Usuário exedeu o máximo de 3 tentativas")

else:
    print("Codigo correto. Acesso Liberado")