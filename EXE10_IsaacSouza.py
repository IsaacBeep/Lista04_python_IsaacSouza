#Faça um programa que pergunte quantas pessoas o usuário deseja convidar para uma festa
#Se ele digitar um número abaixo de 10, peça os nomes e após cada nome exiba a mensagem: "[nome] está convidado para a festa". 
#Se ele inserir um número 10 ou superior, exiba a mensagem "Muitas pessoas".
pessoas = int(input('Quantas pessoas voce deseja convidar para a festa?: '))
if pessoas < 10:
    for i in range(pessoas):
        P_convidadas = input("Digite o nome da pessoa: ")
        print('{} Esta convidada para a festa'.format(P_convidadas))
else:
    print('Muitas pessoas')