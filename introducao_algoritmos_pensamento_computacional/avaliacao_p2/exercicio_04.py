qtd_de_alunos = int(input("Informe a qtd de usuários: "))
cont_aprovado = 0

for i in range(qtd_de_alunos):
    aprovado = False
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    if media >= 7:
        aprovado = True
        cont_aprovado += 1

    if aprovado:
        print(f"Aluno Aprovado! média {media}")
    else:
        print(f"Aluno Reprovado! média {media}")


print(f"{cont_aprovado} alunos foram aprovados e, {qtd_de_alunos - cont_aprovado} foram reprovados")