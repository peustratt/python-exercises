"Some as matrizes"

matriz_01 = [
    [15, 52, 29],
    [47, 34, 85]
]
matriz_02 = [
    [5, 13, 11],
    [8, 7, -10]
]

matriz_nova = []

for i, linha in enumerate(matriz_01):
    nova_linha = []

    for j, item in enumerate(linha):
        nova_linha.append(item+matriz_02[i][j])

    matriz_nova.append(nova_linha)

for linha in matriz_nova:
    print(linha)
