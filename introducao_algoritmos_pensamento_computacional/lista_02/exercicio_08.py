entradas_texto = ["Faturamento bruto", "Custos administrativos", "Alíquota de IPI",
            "Multiplicador de encargos", "Folha de pagamentos"]

chaves = ["fat_brut", "cust_adm", "aliq_ipi", "mult_encg", "folha_pag"]
data = {}

print("Digite os seguintes dados")

for index, chave in enumerate(chaves):
    data[chave] = float(input(f'{entradas_texto[index]}: '))

impostos_producao = ((data["fat_brut"] - data["cust_adm"]) * data["aliq_ipi"]) / 100
impostos_folha = data["folha_pag"] * data["mult_encg"]
total_impostos = impostos_producao + impostos_folha

print(f'''\nImpostos de produção: R${impostos_producao}
Impostos de folha: R${impostos_folha}
Total de impostos: R${total_impostos}''')