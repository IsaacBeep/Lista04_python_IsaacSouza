#Peça ao usuário para inserir o seu nome e um numero. Se o numero for menor que 10, exiba o nome dele esse numero de vezes caso contrario exiba a mensagem “numero muito alto” 3 vzs.
nome = input('Diga-nos seu nome: ')
num = int(input('Digite um numero da sua escolha: '))

for i in range(num):
    if num <= 10:
        print(nome)

for I in range(3):
    if num > 10:
        print('Numero muito alto')
print('IsaacSouza')