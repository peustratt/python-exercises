"""
8) O mesmo exercício anterior, mas agora não será informado o número total de
mercadorias no estoque. Então o funcionamento deverá ser da seguinte forma: ler o valor
da mercadoria e perguntar ‘MAIS MERCADORIAS (S/N)?’. Ao final, imprimir o total
em estoque e a média de preço das mercadorias.
"""

total = 0
qtd_de_mercadorias = 0
opcao = 0

while True:
    total = float(input("Digite o valor da mercadoria: "))
    qtd_de_mercadorias += 1

    while True:
        opcao = input("MAIS MERCADORIAS (S/N)?").upper()
        if opcao in ['S', 'N']:
            break
        else:
            print("Opção invalida!")

    if opcao == 'N':
        break

print(f"O preço total de mercadorias é de R${total:.2f}, e a média dos preços é de R${total/qtd_de_mercadorias:.2f}")
