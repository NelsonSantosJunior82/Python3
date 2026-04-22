lg = float(input('Largura: '))
al = float(input('Altura: '))

area = (lg * al)
tinta = area / 2
print(f'Sua parede tem a dimensão de {lg:.2f} x {al:.2f} \ne sua área é de {area:.2f} m2.')
print(f'Para pintar essa parede, você precisará de {tinta:.2f} l de tinta.')