"""
Faça um programa para ler 10 números e armazenar em um vetor. Após isto, o programa
deve ordenar os números no vetor em ordem crescente. Escreva na tela o vetor ordenado.
"""

vetor = [num for num in range(10, 0, -1)]
vetor_ordenado = []

min = vetor[0]

# Achando o menor valor
for num in vetor:
    if num < min:
        min = num

vetor_ordenado.append(min)

# Achando qualquer valor maior que min
for num in vetor:
    if num > min:
        mid = num
        break

for _ in range(len(vetor) - 1):
    #Achando os próx valores
    for num in vetor:
        if num > min and num < mid:
            mid = num

    vetor_ordenado.append(mid)
    min = mid

    #Achando qualquer valor maior que min
    for num in vetor:
        if num > mid:
            mid = num
            break


print(vetor)
print(vetor_ordenado)