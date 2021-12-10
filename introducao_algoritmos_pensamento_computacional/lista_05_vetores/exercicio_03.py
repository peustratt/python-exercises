"""
Escreva um programa para ler e armazenar em um vetor a temperatura média dos últimos
X dias, onde a quantidade de dias a ser cadastrada será informada pelo usuário. Esta
quantidade será o tamanho do vetor. Calcule e escreva na tela:
a. Menor temperatura
b. Maior temperatura
c. Temperatura média
d. O número de dias em que a temperatura foi inferior à média
"""

qtd_de_dias = int(input('Digite a quantidade de dias: '))
dias = []
soma_temps = 0

for dia in range(qtd_de_dias):
    temperatura = float(input(f"Digite a temperatura do °{dia+1}: "))
    dias.append(temperatura)
    soma_temps += temperatura


menor_temp = dias[0]
maior_temp = dias[0]
media = soma_temps/qtd_de_dias
cont_inferior_media = 0

for temp in dias:
    if temp > maior_temp:
        maior_temp = temp
    elif temp < menor_temp:
        menor_temp = temp

    if temp < media:
        cont_inferior_media += 1

print(f"""A mínima foi {menor_temp}°C
A máxima foi {maior_temp}°C
A média foi {media}°C
e o numero de dias abaixo da média foi {cont_inferior_media}""")