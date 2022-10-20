# Desafio:
# Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:
# a. De quem foi a melhor volta da prova, e em que volta?
# b. Classificação final em ordem decrescente (1º. o campeão)
# c. Qual foi o piloto com a melhor média?

corredores = 0
voltas = 0
melhor_volta = ['', 0, 0]
media_tempo = 0
melhor_media = ['', 0]
inicio = True
inicio2 = True
list_corredores = []
list_tempo = []

while corredores < 3:
    corredores += 1
    nome = input("Nome do corredor: ")
    while voltas < 10:
        voltas += 1
        tempo = int(input(f"Tempo em segundos da {voltas}° volta: "))
        media_tempo += tempo
        if tempo < melhor_volta[2]:
            melhor_volta[0] = nome
            melhor_volta[1] = voltas
            melhor_volta[2] = tempo
        list_tempo.append(tempo)
        if inicio:
            melhor_volta[0] = nome
            melhor_volta[1] = voltas
            melhor_volta[2] = tempo
            inicio = False
    media_tempo = media_tempo / 10
    if inicio2:
        melhor_media[0] = nome
        melhor_media[1] = media_tempo
        inicio2 = False
    if media_tempo < melhor_media[1]:
        melhor_media[1] = media_tempo
    list_corredores.append([nome, list_tempo])
    list_tempo = []
    voltas = 0
    print(melhor_media)
    print(melhor_volta)
    print(list_corredores)


print(f'A melhor volta foi corrida pelo corredor {melhor_volta[0]} executada na {melhor_volta[1]}° corrida durante {melhor_volta[2]} segundos.')
print(f'A melhor média de voltas foi feita pelo corredor {melhor_media[0]} com a média de {melhor_media[1]} segundos em 10 voltas.')

numeros.sort(key=int, reverse=True)
for e in list_corredores:
    e += 1
    print(f'Corredo: {i}')
    for b in range(voltas):
        b += 1
        print(f'Volta: {b}')