horas_trab = int(input("Digite a quantidade de horas trabalhas: "))
salario_hora = float(input("Digite o seu salário por hora R$/h: "))
salario_extra = 0

if horas_trab > 160:
    horas_extras = horas_trab - 160
    salario_extra = (salario_hora * 0.5) * horas_extras

salario_mensal = (horas_trab*salario_hora) + salario_extra

print(f"Seu salário total é de R$ {salario_mensal}")



