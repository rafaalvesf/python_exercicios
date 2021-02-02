velatual = float(input('Qual a velocidade atual do veículo? '))
if velatual <= 80:
    print('Tenha uma boa viajem! Dirija com segurança!')
else:
    print('Você foi multado! O limite de velocidade é de 80km/h')
    multa = (velatual -80 ) * 7
    print('Você deverá pagar uma multa de R${:.2f}!'.format(multa))