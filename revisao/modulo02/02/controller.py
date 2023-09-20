def create(cliente):
    with open('pessoas.txt', 'a') as arquivo:
        arquivo.write(f'{cliente}\n')

def read():
    nomes = []
    with open('pessoas.txt', 'r') as arquivo:
        for name in arquivo:
            name = name.strip()
            nomes.append(name)

    return nomes

def search(c):
    index = 0
    flag = 0
    arquivo = open('pessoas.txt', 'r')
    for line in arquivo:
        index += 1
        if c == eval(line)['Nome']:
            print(line)
            flag = 1

        if flag ==0:
            print('Cliente não encontrado!')

def update(cliente):
    flag = False

    with open('pessoas.txt', 'r') as arquivo:
        lines = arquivo.readlines()

    with open('pessoas.txt', 'w') as arquivo:
        for line in lines:
            if cliente in line:
                novo_nome = input('Digite o novo nome: ')
                nova_idade = input('Digite a nova idade: ')
                nova_linha = f'nome: {novo_nome} idade : {nova_idade}'
                arquivo.write(nova_linha)
                flag = True
            else:
                arquivo.write(line)
    if flag:
        print('Seu arquivo foi alterado com sucesso!')

    else:
        print('Cliente nao encontrado!')

def delete():
    with open('pessoas.txt', 'r') as arquivo:
        lines = arquivo.readlines()
        
    with open('pessoas.txt', 'w') as arquivo:
        for cliente in lines:
            novo_nome = ''
            nova_idade = ''
            cliente = cliente.strip()