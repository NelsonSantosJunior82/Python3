"""Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros."""

valor = float(input('Digite um valor em metros: '))
cm = valor * 100
mm = valor * 1000
print(f'O valor de {valor} metros corresponde a {cm} centímetros e {mm} milímetros.')
