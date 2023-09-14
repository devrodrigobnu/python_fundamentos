def sobrenome():
    sobrenome = input('Digite seu sobrenome: ')
    return sobrenome

def idade():
    idade = int(input('Digite sua idade: '))
    return idade

def nome():
    nome = input('Digite seu nome: ')
    return nome

def cpf():
    cpf = input('Digite seu cpf: ')
    return cpf

a = nome()
b = sobrenome()
c = idade()
d = cpf()

print(f'Nome: {a}\nSobrenome: {b}\nIdade: {c}\nCPF: {d}')