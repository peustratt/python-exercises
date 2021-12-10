"""
Faça um programa para “remover” um número de um vetor. Inicialize um vetor com 6
números inteiros quaisquer e depois peça para o usuário digitar um número a ser removido
do vetor. O programa deve verificar se esse número digitado existe no vetor ou não. Se
existir, deve gerar um novo vetor com tamanho reduzido e sem esse número. (Considere
que não haverá números repetidos no vetor).
"""

vetor_original = [1, 2, 3, 4, 5, 6]
vetor_novo =[]

print(vetor_original)
num_escolhido = int(input("Digite o numero para ser deletado: "))

if num_escolhido in vetor_original:
    for num in vetor_original:
        if num == num_escolhido:
            pass
        else:
            vetor_novo.append(num)

    print(vetor_novo)

else:
    print(f"{num_escolhido} não está contido no vetor original!")