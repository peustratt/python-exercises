"""
Escreva um programa que exiba um menu como mostrado abaixo e solicite do usuário
uma opção de refeição que ao final será cobrado um valor do prato solicitado. O
programa encerra quando o usuário informar a opção "S" do menu que se refere a sair.
Obs.: use switch-case e do-while.

Opção do Menu, Produto Valor do Produto
A Açaí na Tigela R$ 15,75
B Bolo de Chocolate R$ 23,10
C CupCake de Nutela R$ 8,50
D Doce de Banana R$ 7,85
E Enroladinho de Frango R$ 5,00
S Sair -
"""

MENU = """A Açaí na Tigela R$ 15,75
B Bolo de Chocolate R$ 23,10
C CupCake de Nutela R$ 8,50
D Doce de Banana R$ 7,85
E Enroladinho de Frango R$ 5,00
S Sair -
"""
total = 0

while True:
    print(MENU)
    opcao = input("Digite sua opção: ").upper()

    if opcao == 'S':
        break

    match opcao:
        case 'A':
            print("Adicionado Açai na Tigela + R$15,75")
            total += 15.75
        case 'B':
            print("Adicionado Bolo de Chocolate+ R$23,10")
            total += 23.1
        case 'C':
            print("Adicionado CupCake de Nutela + R$8,50")
            total += 8.5
        case 'D':
            print("Adicionado Doce de Banada + R$7,85")
            total += 7.85
        case 'E':
            print("Adicionado Enroladinho de Frango + %$5,00")
            total += 5
        case _:
            print("Opção inválida!")
    print("-----------------------------\n")

print(f"O total a ser pago é R${total}")
