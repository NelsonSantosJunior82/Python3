'''Criar lista com os número selecionados e em seguida criar outra lista de seis números'''

import random

# Criar lista de 20 números (exemplo fixo, pode ser alterado)
"""numeros_selecionados = [2,8,16,17,18,19,20,22,24,25,27,28,38,42,43,44,45,47,48,49]"""
numeros_selecionados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
print("Números selecionados:", numeros_selecionados)

# Perguntar quantos jogos o usuário deseja gerar
qtd_jogos = int(input("Quantos jogos de 6 números você deseja gerar? "))

# Gerar as listas de jogos
jogos = []
for i in range(qtd_jogos):
    jogo = sorted(random.sample(numeros_selecionados, 6))
    jogos.append(jogo)

# Exibir os jogos gerados
for i, jogo in enumerate(jogos, 1):
    print(f"Jogo {i}: {jogo}")

