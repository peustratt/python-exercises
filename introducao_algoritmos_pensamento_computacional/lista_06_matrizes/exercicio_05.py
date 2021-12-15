matriz_repostas = [
    ["a", 'b', 'c', 'd', 'e'],
    ["c", 'd', 'a', 'a,', 'e'],
    ["c", 'd', 'a', 'a,', 'c'],
    ["a", 'd', 'a', 'a,', 'c'],
    ["c", 'd', 'a', 'a,', 'e'],
    ["a", 'd', 'a', 'a,', 'e'],
    ["c", 'd', 'a', 'a,', 'e'],
    ["c", 'b', 'c', 'd,', 'c'],
    ["c", 'b', 'c', 'd,', 'e'],
    ["c", 'd', 'c', 'a,', 'e'],
]

lista_gabarito = ['a', 'b', 'c', 'd', 'e']

for i, repostas in enumerate(matriz_repostas):
    nota_aluno = 0
    for j, reposta in enumerate(repostas):
        if reposta == lista_gabarito[j]:
            nota_aluno += 2
    print(f"A nota {i+1}° aluno foi {nota_aluno}")
