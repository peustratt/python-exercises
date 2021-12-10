pesos = [2, 3, 5]
notas = []

for n in range(1, 4):
    notas.append(float(input(f"Digite a sua {n}° nota: ")))

soma_dividendo = 0
soma_pesos = 0

for index, nota in enumerate(notas):
    soma_dividendo += nota * pesos[index]
    soma_pesos += pesos[index]

print(f"Sua média é: {soma_dividendo / soma_pesos}")

