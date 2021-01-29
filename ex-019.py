num = int(input('Digite um número inteiro: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Em relação ao número {} podemos concluir que: '.format(num))
print(' {} pertence a Unidade'.format(unidade))
print(' {} pertence a Dezena'.format(dezena))
print(' {} pertence a Centena'.format(centena))
print(' {} pertence a Unidade de Milhar'.format(milhar))