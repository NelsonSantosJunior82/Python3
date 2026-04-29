dias = int(input('Dias de locação: '))
valor_dias = dias * 60
km = float(input('Kilometros foram percorridos: '))
valor_km = km * 0.15
valor_total = valor_dias + valor_km

print(f'O valor da locação de {dias} dias é de R$ {valor_dias:.2f} \ne o valor de {km} km percorridos é de R$ {valor_km:.2f}, totalizando um valor de R$ {valor_total:.2f}')

