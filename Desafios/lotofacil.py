'''Criar lista com os número selecionados e em seguida criar outra lista de seis números'''

import random

# Criar lista de 20 números (exemplo fixo, pode ser alterado)
numeros_selecionados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print("Números selecionados:", numeros_selecionados)

# Perguntar quantos jogos o usuário deseja gerar
qtd_jogos = int(input("Quantos jogos de 6 números você deseja gerar? "))

# Gerar as listas de jogos
jogos = []
for i in range(qtd_jogos):
    jogo = sorted(random.sample(numeros_selecionados, 15))
    jogos.append(jogo)

# Exibir os jogos gerados
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")

