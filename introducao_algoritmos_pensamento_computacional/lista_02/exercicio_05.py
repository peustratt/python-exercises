unitario = float(input("Digite o valor unitário: "))
quantidade = float(input("Digite a quantidade: "))
aliquota = float(input("Digite a aliquota de ICMS: "))

imposto = unitario * quantidade * aliquota / 100
total = (unitario * quantidade) + imposto

print(f'Valor total pago foi de: RS{total}, e deste valor os impostos foram: {imposto}')