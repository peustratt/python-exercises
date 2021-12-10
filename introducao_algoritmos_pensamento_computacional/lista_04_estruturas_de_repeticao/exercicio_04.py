"""
 Escreva um programa que leia 10 valores e escreva na tela quantos desses valores lidos
estão no intervalo [10,20] (incluindo os valores 10 e 20 no intervalo) e quantos deles
estão fora deste intervalo.
"""

contador_dentro = 0
qtd_valores = 3

for n in range(1, qtd_valores + 1):
    numero = int(input(f"Digite o °{n} valor: "))

    if numero >= 10 and numero <= 20:
        contador_dentro += 1

print(f"Dos valores inseridos {contador_dentro} estão dentro e {abs(contador_dentro-qtd_valores)} estão fora do invervalo.")

