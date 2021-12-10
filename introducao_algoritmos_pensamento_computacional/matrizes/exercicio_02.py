"""Some a diagonal da matriz"""

matriz = [
    [1, 2, 3, 4],
    [5, 1, 7, 8],
    [9, 10, 1, 12],
    [13, 14, 15, 1]
]
soma_diag = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            soma_diag += matriz[i][j]

print(soma_diag)

