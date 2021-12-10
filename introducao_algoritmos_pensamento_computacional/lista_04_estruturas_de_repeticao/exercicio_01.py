"""
Escreva um programa que leia 10 valores, calcule e escreva a média aritmética desses
valores lidos.
"""

soma = 0

for n in range(1, 11):
    soma += int(input(f"Digite o °{n}: "))

print(f"A média aritimética dos valores é {soma/10}")
