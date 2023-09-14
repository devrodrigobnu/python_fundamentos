from aula05 import soma,sub,multiplicacao,divisao

def menu():

    var = 1
    while var != 0:
        print('Digite qual operação matemática você deseja fazer: ')

        cond = int(input('\n1-Soma \n2-Subtração \n3-Multiplicação \n4-Divisão \nOpção: '))
        match(cond):
            case 1:
                n1 = int(input('Digite o primeiro número: '))
                n2 = int(input('Digite o segundo número: '))
                soma(n1,n2)
            case 2:
                n1 = int(input('Digite o primeiro número: '))
                n2 = int(input('Digite o segundo número: '))
                print(sub(n1,n2))
            case 3:
                n1 = int(input('Digite o primeiro número: '))
                n2 = int(input('Digite o segundo número: '))
                print(multiplicacao(n1,n2))
            case 4:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                print(divisao(n1,n2))
        var = input('Digite 1 para continuar: ')
