"""
7) Uma loja está levantando o preço total de todas as mercadorias em estoque. Escreva um
programa que pergunte ao usuário o número total no estoque. Para cada mercadoria no
estoque, o programa deve perguntar o preço ao usuário. Ao final imprimir o total em
estoque e a média de preço das mercadorias.
"""

quantidade_merc = int(input("Digite quantas mercadorias: "))
total = 0

for num in range(quantidade_merc):
    total += float(input(f"Digite o valor da °{num + 1} mercadoria: "))

print(f"O preço total de mercadoria é de R${total:.2f}, e a média dos preços é R${total/quantidade_merc:.2f}")