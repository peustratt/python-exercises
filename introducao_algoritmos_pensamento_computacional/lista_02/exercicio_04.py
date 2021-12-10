entradas = ["salario_bruto", "aliquota_inss", "aliquota_ir", "redutor_ir"]
dados = {}

for entrada in entradas:
    dados[entrada] = float(input(f"Digite {entrada}: "))

valor_inss = (dados["salario_bruto"] * dados["aliquota_inss"]) / 100
valor_ir = ((dados["salario_bruto"] - valor_inss) * dados["aliquota_ir"]) / 100 - dados["redutor_ir"]
liquido = dados["salario_bruto"] - valor_inss - valor_ir

print(f'Salário liquido: {liquido},\n Valor pago de IR: {valor_ir}, \n Valor pago de INSS: {valor_inss}"')

