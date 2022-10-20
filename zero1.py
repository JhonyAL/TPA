n = int(input('Digite a dimensão de linhas da matriz: '))
m = int(input('Digite a dimensão de colunas da matriz: '))
matriz = []
for i in range(n):
    matriz.append([0]*m)
for i in range(n):
    print(matriz[i])
