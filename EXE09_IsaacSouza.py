#Faça um programa que pergunte em qual direção o usuário deseja contar (para cima [ c/C] ou para baixo [a/A]). 	Se ele selecionar para cima, peça o número superior e conte de 1 até esse número. 	Se ele inserir algo diferente de cima ou baixo, exiba a mensagem “Direção Invalida!".
sentido = input('Digite c/C para cima ou a/A para baixo: ').lower()

for i in sentido:
    if sentido == 'c':
        numero = int(input('Digite um numero acima de 1: '))
        for I in range(numero):
            numR = numero - I
            print(numR)
    elif sentido == 'a':
        numero = int(input('Digite um numero abaixo de 20: '))
        for I in range(numero):
            print('')