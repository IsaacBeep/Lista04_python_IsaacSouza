#Defina uma variável chamada total como 0 (Zero). Peça ao usuário para inserir cinco números e, após cada entrada, pergunte se ele deseja que esse número seja incluído (S ou s, N ou n). Se ele desejar, adicione o número ao total. Se ele não quiser incluí-lo, não o adicione ao total. Depois de inserir todos os cinco números, exiba o total.
total = 0

for i in range(0, 5):
    numR = int(input('Digite seu numero: '))
    num = input('Deseja adicionar um numero? S/s ou N/n: ').lower()

    if num == 's':
        total += numR

print(total)
print('IsaacSouza')