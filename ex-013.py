dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
valor = dias * 60
valor = valor + (km * 0.15)
print('O valor a ser pago pelo aluguel é de R${:.2f}'.format(valor))