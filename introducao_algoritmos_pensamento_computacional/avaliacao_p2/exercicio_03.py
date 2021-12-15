ma = [
    [15, 52, 29],
    [47, 34, 85]
]
mb = [
    [5, 13, 11],
    [8, 7, -10]
]
mc = []

for i, linha in enumerate(ma):
    linha_vazia = []
    for j, elemento_a in enumerate(linha):
        linha_vazia.append(elemento_a + mb[i][j])
    mc.append(linha_vazia)

for linha in mc:
    for elemento in linha:
        print(str(elemento) + ' ', end='')
    print()
