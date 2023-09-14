cond = 'Sim'

# Upper transforma tudo em maiusculo 
# Lower transforma tudo em minúsculo
# Capitalize transforma a primeira em maiuscula

while cond.capitalize() == 'Sim':
    var = input('Digite seu nome para testarmos a interação: ')
    print(f'O nome digitado pelo usuário foi {var}')

    cond = input('Você deseja continuar? \nsim \nnao\nOpção: ')
print('Você saiu do sistema')