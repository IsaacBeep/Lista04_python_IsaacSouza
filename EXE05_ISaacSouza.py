#Peça ao usuário  para inserir um numero que deseja tabuada e em seguida exibir a tabuada para esse numero
num = int(input('Digite um numero: '))

for i in range(1, 11):
    N = i * num
    print('Resultado da tabuada do numero {}: {} * {} = {}'.format(num, num, i, N))