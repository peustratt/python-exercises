"""
Escreva um programa que receba um número qualquer do usuário e calcule o fatorial
deste número.
"""

numero = int(input("Digite o numero: "))
fatorial = numero

for n in range(1, numero):
    fatorial = fatorial * n

print(fatorial)


