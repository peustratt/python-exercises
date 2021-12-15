qtd_de_alunos = 10
notas = []
media = 0
cont_acima_media = 0

for i in range(qtd_de_alunos):
    notas.append(float(input(f"Digite a nota do {i + 1}° aluno: ")))

for nota in notas:
    media += nota
media /= qtd_de_alunos

for nota in notas:
    if nota > media:
        cont_acima_media += 1

print(f"A média da turma foi {media} e, {cont_acima_media} alunos ficaram acima da média")
