"""
1) Declare e inicialize dois vetores do tipo String vetorA e vetorB de tamanho 5. Faça a troca
do conteúdo dos dois vetores e exiba na tela.
"""

vetor_a = ["Xand", "Dudu", "Nego", "Java", "Python"]
vetor_b = ["PHP", "Cobol", "JavaScript", "HTML", "CSS"]

for index, nome in enumerate(vetor_a):
    troca_b = vetor_b[index]
    vetor_a[index] = troca_b
    vetor_b[index] = nome


print(vetor_a)
print(vetor_b)