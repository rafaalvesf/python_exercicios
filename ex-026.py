numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if(resultado == 1):
    print('O número {} é impar'.format(numero))
else:
    print('O número {} é par'.format(numero))