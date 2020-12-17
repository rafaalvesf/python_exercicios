larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print('A área da parede é de {}m²'.format(area))
tinta = area/2
print('Você gastará {}l de tinta para pintar a parede.'.format(tinta))