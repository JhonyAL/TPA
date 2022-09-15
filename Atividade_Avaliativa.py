from re import X

salario = 0
salarioTotal = 0
totalFilhos = 0
filhos = 0
pessoas = 0
maiorSal = 0
menorSal = 0

while salario >= 0:
    salarioTotal = salarioTotal + salario
    totalFilhos = totalFilhos + filhos
    salario = float(input("Informe o seu salário: "))
    if maiorSal < salario:
        maiorSal = salario
    if salario < 0:
        pass
    else:
        pessoas = 1 + pessoas
        filhos = int(input("Informe a quantidade de filhos: "))
        totalFilhos = filhos + totalFilhos
        if salario < 1500:
            menorSal = menorSal + 1

mediaSalario = salarioTotal / pessoas
mediaFilhos = totalFilhos / pessoas
mediaSalario = salarioTotal / pessoas
percentualMenor = float((menorSal * 100) / pessoas)

print(
    'Média Salarial: R$ '
    + str(round(mediaSalario, 2)) +
    '; Média de filhos: '
    + str(round(mediaFilhos, 2)) +
    '; Maior salário: R$ '
    + str(round(maiorSal, 2)) +
    '; Percentual de pessoas com salário abaixo de R$ 1500,00: '
    + str(round(percentualMenor, 2))
    + '%.'
)