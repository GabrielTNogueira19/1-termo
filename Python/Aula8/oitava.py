# print("Clean Code - Aula 8")
# aula = 8
# print(f"Estamos na aula {aula} de Clean Code")

# Exercicio 1

# frase_dia = input("Insira uma frase que deseja compartilhar: ")
# print(frase_dia.upper())
# print(frase_dia.count(""))

# Manipulação de Arquivos:

# Escrevendo Arquivo:

# with open ("arquivo.txt", "w") as example:
#     example.write("Exemplo de Clean Code - Aula 8\n")
#     example.write("Continuando a escrever no arquivo \n")

# with open ("arquivo.py","w") as python:
#     python.write('print("Escrevendo no arquivo")')

# # "w" = write - Escreve no arquivo, se o arquivo ja existir, ele irá sobrescrever o conteúdo.

# with open ("arquivo.txt", "r") as example:
#     conteudo_arquivo = example.read()
#     print(conteudo_arquivo)

# with open ("arquivo.py", "r") as python:
#     conteudo_python = python.read()
#     print(conteudo_python)

# # "r" = read - lê o conteúdo do arquivo.

# with open ("arquivo.txt", "a") as example:
#     example.write("\nEscrevendo mais no mesmo arquivo")

# with open ("arquivo.py", "a") as python:
#     python.write('\nprint("Estou escrevendo mais")')

# # "a" = append - Adiciona conteúdo ao final do arquivo.

# Manipulação do Sistema Operacional
import os # Biblioteca para manipulação de arquivos e diretórios.

# criar pasta
# os.mkdir("teste")

# renomear pasta
# os.rename("teste", "Aulas")

# excluir pasta
# os.rmdir("Aulas")

# criando arquivos
# os.touch("teste.txt")

# Listagem de diretórios

# print(os.listdir())
# print(os.listdir(".."))
# print(os.listdir("C:\\"))


# Exercicio 4

# print(os.listdir())
import time
# Exercicio 5


os.mkdir("Pasta_Teste")
print("Pasta criada")
time.sleep(5)
os.rename("Pasta_Teste", "Pasta_Renomeada")
print("pasta renomeada")
time.sleep(5)
os.rmdir("Pasta_Renomeada")
print("Parta excluida")