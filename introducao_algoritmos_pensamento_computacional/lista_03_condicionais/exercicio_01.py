repostas = []

for _ in range(5):

    x, y = input("Digite os valores de x,y separados por uma virgula: ").split(",")

    z = (int(x)*int(y)) + 5

    if z <= 0:
        resposta = 'A'
    elif z <= 100:
        resposta = 'B'
    else:
        resposta = 'C'

    repostas.append((z, resposta))

for resp in repostas:
    print(resp)

