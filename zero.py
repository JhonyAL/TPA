n = int(input('Digite a dimensão linha da matriz: '))
m = int(input('Digite a dimensão coluna da matriz: '))
matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        linha.append(0)
    matriz.append(linha)
print(matriz)
