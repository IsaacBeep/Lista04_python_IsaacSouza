#Escreva um programa para pedir um numero e em seguida um nome. Exiba o nome (uma letra de cada vez em cada linha) e repita isso para o numero que ele escolheu
num = int(input('Digite um numero: '))
nome = str(input('Diga seu nome: '))
for I in range(num):
    for i in nome:
        print(i)