# Crie um algoritimo para a criação de um arquivo que irá desligar o computador

with open ("Desligar.bat", "w") as executar:
    executar.write('shutdown /s /t 10 /c "Desligando PC, SEXTOU RAPA"' )

with open ("Cancelar Desligamento.bat", "w") as executar:
    executar.write('Shutdown /a')