cont = 0
x = 0
y = 0
z = 0
branco = 0
nulo = 0
eleitores = []

def verifacationEleitor(eleitorU):
    for eleitor in eleitores:
        if eleitor == eleitorU:
            print("Título de eleitor inválido!")
            return True
    eleitores.append(eleitorU)    
    return False

while cont < 31:
    eleitorU = input(
        "Digite seu titulo de eleitor: "
    )
    if not verifacationEleitor(eleitorU):
        cont += 1
        candidato = input(
            'Digite o nome do seu candidato: X, Y ou Z.\n'
            'Para voto em branco, não digite nada, e para voto nulo, digite qualquer coisa diferente dos quatro valores anteriores.\n'
        ).upper()
        if candidato == "X":
            x += 1
        elif candidato == 'Y':
            y += 1
        elif candidato == 'Z':
            z += 1
        elif candidato == '':
            branco += 1
        else:
            nulo += 1

print("\nQuantidade de votos no candidato X: "+ str(x) +";\nQuantidade de votos no candidato Y: "+ str(y) + ";\nQuantidade de votos no candidato Z: "+ str(z) +";\nQuantidade de votos brancos: "+ str(branco) +";\nQuantidade de votos nulos: "+ str(nulo))