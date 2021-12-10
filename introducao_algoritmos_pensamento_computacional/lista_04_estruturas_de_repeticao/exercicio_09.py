"""
9) A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. Faça um
programa para coletar dados sobre o salário e número de filhos de cada habitante e após
as leituras, escrever:
a. Média de salário da população
b. Média do número de filhos
c. Maior salário dos habitantes
d. Percentual de pessoas com salário menor que R$ 150,00
Obs.: Pergunte ao usuário a quantidade de habitantes que será cadatrada
"""

cont_salario_menor = 0
total_de_filhos = 0
salario_max = 0
soma_salario = 0

qtd_de_cadastros = int(input("Digite a quantidade de cadastros: "))

for i in range(qtd_de_cadastros):
    salario = float(input(f"Digite o salário do °{i + 1} cadastro: "))
    qtd_de_filhos = int(input(f"Digite a quantidade de filhos do °{i + 1} cadastro: "))

    total_de_filhos += qtd_de_filhos
    soma_salario += salario

    if salario < 150:
        cont_salario_menor += 1
    if salario > salario_max:
        salario_max = salario

print(f"""A média dos salarios é {soma_salario/qtd_de_cadastros:.2f}
A média de filhos é de {total_de_filhos/qtd_de_cadastros:.2f} filhos por pessoa.
O mario salário entre os cadastrados é de R${salario_max:.2f}
O percentual de pessoas com salário menor que R$150,00 é de {(cont_salario_menor/qtd_de_cadastros) * 100:.2f}%""")
