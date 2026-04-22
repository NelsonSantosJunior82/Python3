
qtd_vagas = 50
opcao = 0

while opcao != 3:
    print("=+"*20)
    print('''      [1] Entrada
      [2] Saída
      [3] Fim''')
    
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        qtd_vagas = qtd_vagas - 1  
        print(f'Vagas disponíveis: {qtd_vagas}')
        if qtd_vagas == 0:
            print('LIMITE ATINGIDO')
                
               
    elif opcao == 2:
        if qtd_vagas == 50:
            print('ESTACIONAMENTO VAZIO')
        else:
            qtd_vagas = qtd_vagas + 1
            print(f'Vagas disponíveis: {qtd_vagas}')
             
        
            
            
            
                    
    elif opcao == 3:
        print('FIM DA PROGRAMAÇÃO')
    else:
        print('Opção Inválida')
    print("+="*20)


