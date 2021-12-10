preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

while True:
    cond_pag = int(input("""Digite o código de pagamento -
    1 - À vista em dinheiro ou cheque, receba com 10% de desconto.
    2 - À vista no cartão de crédito, receba com 5% de desconto.
    3 - Em duas vezes, preço normal sem juros.
    4 - Em três vezes, preço normal mais juros de 15%.
    --------
    : """))
    # Verifica se a condição de pagamento está incluida na lista [1, 2, 3, 4]
    if cond_pag in range(1, 5):
        break
    else:
        print("Opção inválida!")

valor_parcial = preco * quantidade

if cond_pag == 1:
    desconto = 0.9
elif cond_pag == 2:
    desconto = 0.95
elif cond_pag == 3:
    desconto = 1
else:
    desconto = 1.15


print("O custo do produto foi de R$: {:.2f}".format(valor_parcial*desconto))
