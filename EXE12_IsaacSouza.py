#Você é um desenvolvedor de sistemas trabalhando em um projeto para um salão de beleza. O salão precisa de um sistema para gerenciar os horários de atendimento dos clientes. Primeiro, a dona do salão monta a grade horária da agenda. Depois, uma cliente deseja agendar um horário, e o sistema exibe os horários disponíveis. A dona do salão então agenda o horário escolhido pela cliente, e o horário escolhido não estará mais disponível. O sistema deve continuar permitindo agendamentos até que todos os horários disponíveis sejam preenchidos ou até que a dona do salão decida parar.
#Solicite à dona do salão para inserir os horários disponíveis na agenda.
#Exiba os horários disponíveis para a cliente
#Permita que a cliente escolha um horário para agendamento
#Atualize a agenda marcando o horário escolhido como ocupado
#Pergunte se deseja agendar mais um horário e continue até que todos os horários estejam preenchidos ou a dona do salão decida parar
horarios = int(input('Por favor digite quantos horarios você deseja: '))
GU_horarios = []

for i in range(horarios):
    GUA_horarios = input('Digite um horario: ')
    GU_horarios.append(GUA_horarios)

print('Horarios disponiveis: {}'.format(GU_horarios))

S_horarios = input('Agora escolha um horario disponivel: ')

if S_horarios in GU_horarios:
    i = GU_horarios.index(S_horarios)
    GU_horarios.remove(S_horarios)
    print('Agora o horario {} esta ocupado'.format(S_horarios))
    SE_horarios = input('Deseja agendar mais um horario? s/n: ')
    
    if SE_horarios == 's':
        print('Horarios disponiveis: {}'.format(GU_horarios))
        S_horarios = input('Agora escolha um horario disponivel: ')
        if S_horarios in GU_horarios:
            i = GU_horarios.index(S_horarios)
            GU_horarios.remove(S_horarios)
            print('Agora o horario {} esta ocupado'.format(S_horarios))
            SE_horarios = input('Deseja agendar mais um horario? s/n: ')

    





