while True:
    combustivel = input("Digite o tipo de combustível 'A' para álcool e 'G' para gasolina: ")
    if combustivel.upper() in ['A', 'G']:
        break
    print("Invalid option!")

qtd_litros = int((input("Digite quantos litros deseja: ")))
print(qtd_litros)

alcool = [0.97, 0.95]
gasolina = [0.96, 0.94]


if combustivel.upper() == 'A':
    preco = 4.90
    if qtd_litros <= 20:
        desconto = alcool[0]
    else:
        desconto = alcool[1]
else:
    preco = 5.90
    if qtd_litros <= 20:
        desconto = gasolina[0]
    else:
        desconto = gasolina[1]

total = qtd_litros * preco

print("Você pagou R${:.2f}".format(total*desconto))