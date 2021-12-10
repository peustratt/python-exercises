salario = 1200
contas = [200, 120]
debito = 0

for conta in contas:
    debito += conta * 1.02

print(f'O restante do salario é de: {salario - debito}')