from re import X

# Start Variables

filhos = []
filhoTot = 0
salarios = []
salTot = 0
menorSalario = 0
salario = 0
maiorSalario = 0
pessoas = 0

# Repeat for wage and childrens

while salario >= 0:
    salario = (float(input('Salário: ')))
    if salario < 0:
        pass
    else:
        salarios.append(salario)
        pessoas += 1
        if salario > maiorSalario:
            maiorSalario = salario
        if salario < 1500:
            menorSalario += 1
        filhos.append(int(input('Filhos: ')))

# Average for wage and childrens 

for filho in filhos:
    filhoTot += filho

for salario in salarios:
    salTot += salario

filhoTot = round((filhoTot / pessoas),2)
salTot = round((salTot / pessoas),2)
percentual = round((float((menorSalario * 100) / pessoas)),2)

print(
    'Média Salarial: R$ '
    + str(salTot) +
    '; Média de filhos: '
    + str(filhoTot) +
    '; Maior salário: R$ '
    + str(maiorSalario) +
    '; Percentual de pessoas com salário abaixo de R$ 1500,00: '
    + str(percentual)
    + '%.'
)

if str(input('Deseja ver o histórico de salários? ').upper()) == 'SIM':
    if input('E a quantidade de filhos? ').upper() == 'SIM':
        print('******FILHOS******')
        for filho in filhos:
            print(filho)
    print('*****HISTORICO DE SALARIOS******')
    for salario in salarios:
        print(salario)