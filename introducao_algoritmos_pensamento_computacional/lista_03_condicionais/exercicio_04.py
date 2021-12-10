from datetime import date

today = date.today()
current_year = int(today.strftime("%Y"))

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_ingresso = int(input("Digite o ano que você ingressou na empresa: "))
idade = current_year - ano_nasc
tempo_de_trabalho = current_year - ano_ingresso

if idade >= 65:
    aposentar = True
elif tempo_de_trabalho >= 30:
    aposentar = True
elif idade >= 60 and tempo_de_trabalho >= 25:
    aposentar = True
else:
    aposentar = False

decisao = '' if aposentar else 'Não'

print(f"Idade: {idade}, tempo de trabalho: {tempo_de_trabalho}, situação: {decisao} Requer aposentadoria.")


