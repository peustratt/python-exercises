"""
 Escreva um programa que receba diversos números inteiros e positivos do usuário e que
seja interrompido ao ser informado o número zero. Com os números recebidos,
determine o maior e o menor valor deste conjunto de números
"""

max = 0
print("Digite o valor ou, digite 0 para encerrar!")
numero = int(input("valor: "))
min = numero

while True:
    if numero > max:
        max = numero
    elif numero < min and numero != 0:
        min = numero

    if numero == 0:
        break

    numero = int(input("valor: "))

print(f"O maior valor inserido é {max}, e o menor valor inserido é {min}")
