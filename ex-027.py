distancia = float(input('Qual é a distância em KM da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(distancia))
if(distancia > 200):
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print('O preço da sua passagem será R${:.2f}'.format(preco))