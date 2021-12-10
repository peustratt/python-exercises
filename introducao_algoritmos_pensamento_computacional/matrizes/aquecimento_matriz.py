matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in matriz:
    linha = []
    for j in i:
        linha.append(str(j))
    print(", ".join(linha))

