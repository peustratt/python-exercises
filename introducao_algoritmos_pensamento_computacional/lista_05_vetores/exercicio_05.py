"""
Escreva um programa que permita o usuário informar dados para dois vetores de inteiros
de 5 posições cada um e apresente o conjunto união dos vetores em um terceiro vetor.
Conjunto união são todos os elementos que existem em ambos os vetores. (Considere que
não haverá números repetidos nos vetores).
"""

vetor_a = []
vetor_b = []
vetor_intersect = []

for i in range(1, 6):
    vetor_a.append(int(input(f"Digite o °{i} valor para o vetor A: ")))
    vetor_b.append(int(input(f"Digite o °{i} valor para o vetor B: ")))

for num_a in vetor_a:
    for num_b in vetor_b:
        if num_a == num_b:
            vetor_intersect.append(num_a)

print(vetor_a)
print(vetor_b)
print(vetor_intersect)