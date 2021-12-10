"""Some a diagonal da matriz"""

matriz = [
    [1, 2, 3, 4],
    [5, 1, 7, 8],
    [9, 10, 1, 12],
    [13, 14, 15, 1]
]
soma_diag = 0

for i, linha in enumerate(matriz):
    for j, item in enumerate(linha):
        if i == j:
            soma_diag += item

print(soma_diag)

