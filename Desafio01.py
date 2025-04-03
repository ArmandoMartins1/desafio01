#Dados os valores de ghorarios abaixo, decifre a logica e faça um codigo para executar
"""entrada01 3:45  -- 24hrs
entrada02 14:20  -- 24hrs

saida 6:05 em formato 12hrs
"""
# entrada de dados

hora1 = int(input("Digite apenas a hora: "))
minuto1 = int(input(f"Digite os minutos da hora {hora1}:__ :"))
print("----------")

hora2 = int(input("Digite a hora da segunda entrada: "))
minuto2 = int(input(f"Digite os minutos da hora {hora2}:__ :"))


somaHora= hora1+hora2
if somaHora > 36:
    somaHora = somaHora -36
elif somaHora > 24:
    somaHora = somaHora -24
elif somaHora > 12:
    somaHora= somaHora - 12

somaMinuto = minuto1+minuto2
if somaMinuto >= 60:
    minutoExtra = somaMinuto - 60
    somaHora = somaHora + 1
    if somaHora >12:
        somaHora = somaHora-12
    print("saida em 12 horas\n")
    print(somaHora, ":",minutoExtra)
else:
    print("saida em 12 horas\n")
    print(somaHora,":",somaMinuto)

