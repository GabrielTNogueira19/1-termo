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