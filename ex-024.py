from random import randint
from time
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 à 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
if jogador == computador:
    print('Congratulations!! Você pensa igual a eu!!! ')
else:
    print('Eu ganhei!! Eu pensei no número {} e não no número {}... Você não consegue ler minha mente. :)'.format(computador,jogador))