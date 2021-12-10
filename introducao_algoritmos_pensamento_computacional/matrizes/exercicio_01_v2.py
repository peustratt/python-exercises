"Some as matrizes"

matriz_01 = [
    [15, 52, 29],
    [47, 34, 85]
]
matriz_02 = [
    [5, 13, 11],
    [8, 7, -10]
]

for i in range(len(matriz_01)):
    for j in range(len(matriz_01[i])):
        matriz_01[i][j] += matriz_02[i][j]


for linha in matriz_01:
    print(linha)
