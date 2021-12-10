"""
5) Escrever um programa para fazer a apuração dos votos de uma eleição onde há quatro
candidatos. Os votos serão obtidos através dos códigos de cada candidato de acordo com
a tabela abaixo. Ao informar o código “0” o programa encerra.

Código Descrição
1 José
2 Maria
3 Paulo
4 Carla
5 Branco
0 Encerrar programa

Como informações de saída informe:
a. O total de votos para cada candidato e seu percentual sobre o total;
b. O total de votos nulos e seu percentual sobre o total;
c. O total de votos em branco e seu percentual sobre o total.
"""

MENU = """Código Descrição
1 José
2 Maria
3 Paulo
4 Carla
5 Branco
0 Encerrar programa\n"""

cont_cod_01 = 0
cont_cod_02 = 0
cont_cod_03 = 0
cont_cod_04 = 0
cont_cod_05 = 0
cont_cod_06 = 0


while True:
    print(MENU)
    escolha = int(input("inserir código: "))
    print("-------------------------------")

    if escolha == 0:
        break

    if escolha == 1:
        cont_cod_01 += 1
    elif escolha == 2:
        cont_cod_02 += 1
    elif escolha == 3:
        cont_cod_03 += 1
    elif escolha == 4:
        cont_cod_04 += 1
    elif escolha == 5:
        cont_cod_05 += 1
    else:
        cont_cod_06 += 1

total = cont_cod_01 + cont_cod_02 + cont_cod_03 + cont_cod_04 + cont_cod_05 + cont_cod_06

print(f"""
José teve {cont_cod_01}({(cont_cod_01/total) * 100:.1f}%) votos
Maria teve {cont_cod_02}({(cont_cod_02/total) * 100:.1f}%) votos
Paulo teve {cont_cod_03}({(cont_cod_03/total) * 100:.1f}%) votos
Carla teve {cont_cod_04}({(cont_cod_04/total) * 100:.1f}%) votos
Votos em branco {cont_cod_05}({(cont_cod_05/total) * 100:.1f})
Votos em nulos {cont_cod_06}({(cont_cod_06/total) * 100:.1f})
""")
