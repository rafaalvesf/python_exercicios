money = float(input('Quanto de dinheiro você tem na carteira? R$'))
usd = 5.21
print('Com R${} na carteira, você consegue comprar USD${:.3}'.format(money,(money/usd)))
