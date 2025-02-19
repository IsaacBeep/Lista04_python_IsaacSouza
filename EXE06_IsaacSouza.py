#Peça um numero a baixo de 50 e em seguida faça uma contagem regressiva , certificando-se de mostrar o numero que ele escolheu na saída
num = int(input('Digite um numero abaixo de 50: '))

for i in range(50, - 1):
    for i in range(50,num ,-1):
        print(i)

print('Numero que o usuario escolheu: {}'.format(num))

if num > 50:
    print("Numero muito alto")

if num < -1:
    print('Numero muito baixo')