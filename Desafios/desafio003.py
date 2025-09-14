'''Crie um script que leia dois
numeros e tente mostrar a
soma entre eles.'''

n1 = int(input("Digite um número: "))
n2 = int(input("Digie outro número: "))

sm = n1 + n2

print("A soma ente ",n1 ,"e",n2 ,"é igual a",sm)
print(f'A soma entre {n1} e {n2} é igual a {sm}')
print("A soma entre {} e {} é igual a {}".format(n1,n2,sm))