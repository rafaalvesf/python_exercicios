frase = str(input('Digite uma frase: ')).upper().strip()
print('Uual, em sua frase existe {} letras A'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra apareceu na posição {}'.format(frase.rfind('A')+1))