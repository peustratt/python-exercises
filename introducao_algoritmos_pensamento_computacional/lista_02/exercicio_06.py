entradas = ["Aceleração", "Posição inicial", "Posição final"]
entry = []

for entrada in entradas:
    entry.append(float(input(f'Digite a {entrada}: ')))

tempo = (2*(entry[2] - entry[1]) / entry[0]) ** (1/2)
print(f'O tempo decorrido foi de: {tempo} segundos.')
