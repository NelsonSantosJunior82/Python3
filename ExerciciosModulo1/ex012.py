preco = float(input('Qual é o preço do produto? R$ '))
desconto = (preco * 5)/100
preco_novo = preco - desconto

print(f'O preço do produto é R$ {preco:.2f} e com desconto de 5 por cento \no preço novo é de R$ {preco_novo:.2f}')