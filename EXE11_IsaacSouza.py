#Você é um desenvolvedor de sistemas trabalhando em um projeto colaborativo com sua equipe. Para garantir que todas as tarefas do projeto sejam concluídas dentro do prazo, você decide criar um pequeno programa para controlar o status das tarefas. O programa deve permitir que você insira o nome de cada tarefa e indique se ela está concluída ou não. No final, o programa deve apresentar um resumo com o total de tarefas, quantas estão concluídas e quantas ainda estão pendentes
#Solicite ao usuário o número de tarefas a serem inseridas.
#Para cada tarefa, solicite o nome da tarefa e se ela está concluída (aceitando "sim", "s", "não" ou "n").
#Conte e exiba o número de tarefas concluídas e não concluídas

tarefas = int(input('Quantas tarefas voce deseja?: '))
for i in range(tarefas):

    numN = input('Qual o nome da tarefa?: ')
    numR = input('A tarefa esta concluida? "sim", "s", "nao, ou "n": ').lower()

    if numR == 'sim' or 's':
        Tconcluida = + numR

    if numR == 'nao' or 'n':
        TNconcluida =  + numR
    
print('o total de {} foram concluidas e o total de {} nao foram concluidas'.format(Tconcluida, TNconcluida))
