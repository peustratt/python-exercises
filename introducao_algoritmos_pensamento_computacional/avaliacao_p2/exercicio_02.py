"""
Faça um programa para ler as 3 notas obtidas por um aluno nas 3 avaliações e a média dos exercícios que fazem parte da avaliação.
Faça um método para calcular e retornar a média de aproveitamento, recebendo os valores por parâmetro e usando a fórmula abaixo.
Faça outro método para receber a média (calculada no método anterior) por parâmetro e retornar o conceito do aluno de acordo com a tabela de conceitos exibida mais abaixo.
Exiba na tela a média e o conceito para este aluno.
"""


def calcular_media(n1: float, n2: float, n3: float, media_dos_exercicios: float) -> float:
    return (n1 + (n2 * 2) + (n3 * 3) + media_dos_exercicios) / 7


def conceito_aluno(media: float) -> str:
    if media >= 9:
        conceito = 'A'
    elif media >= 7.5 and media < 9:
        conceito = 'B'
    elif media >= 6 and media < 7.5:
        conceito = 'C'
    else:
        conceito = 'D'

    return conceito


notas = []
for i in range(3):
    notas.append(float(input(f"Digite a N{i + 1}: ")))

notas.append(float(input("Digite a média dos exercícios: ")))

media = calcular_media(*notas)


print(f"A média do aluno foi {media} e o seu conecito foi {conceito_aluno(media)}")