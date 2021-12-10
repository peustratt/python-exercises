n1, n2, n3 = [float(n) for n in input("Digite N1,N2,N3 neste formato separados por vírgulas: ").split(",")]

media_de_aproveitamento = (n1 + (n2 * 2) + (n3 * 3) + ((n1+n2+n3)/3))/7

if media_de_aproveitamento >= 9:
    conceito = 'A'
elif media_de_aproveitamento >= 7.5:
    conceito = 'B'
elif media_de_aproveitamento >= 6:
    conceito = 'C'
else:
    conceito = 'C'

print("Sua média de aproveitamento foi de {:.2f} Conceito: {}".format(media_de_aproveitamento, conceito))
