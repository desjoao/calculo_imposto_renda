#Lista 3 - Exercício 2

salario = float(input('Este é um programa para cálculo de imposto de renda. Informe seu salário bruto: '))
while salario <0:
    salario = float(input('Este é um programa para cálculo de imposto de renda. Informe seu salário bruto: '))
if salario < 1903.99:
    print('Isento de imposto de renda.')
elif salario < 2826.66:
    print(f'Para o salário de {salario} reais, será necessário pagar {salario*0.075} reais de imposto de renda.')
elif salario < 3751.06:
    print(f'Para o salário de {salario} reais, será necessário pagar {salario*0.15} reais de imposto de renda.')
elif salario < 4664.69:
    print(f'Para o salário de {salario} reais, será necessário pagar {salario*0.225} reais de imposto de renda.')
else:
    print(f'Para o salário de {salario} reais, será necessário pagar {salario*0.275} reais de imposto de renda.')
