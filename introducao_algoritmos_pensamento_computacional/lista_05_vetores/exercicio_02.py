"""
Declare e inicialize um vetor A com 10 números inteiros, declare também um vetor B do
mesmo tamanho, sendo que cada elemento do vetor B será o elemento do vetor A * 2. Isto
é: B[i] = A[i] * 2;
"""

vetor_a = [num for num in range(1, 11)]
vetor_b =[]

for num in vetor_a:
    vetor_b.append(num * 2)

print(vetor_a)
print(vetor_b)
