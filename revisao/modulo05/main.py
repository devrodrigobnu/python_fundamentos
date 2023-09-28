from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

cond = 0

while cond == 0:
    var = input('Digite pf para pessoa física e pj para pessoa jurídica: ')
    match var:
        case 'pf':
            pf = PessoaFisica(
                input('Digite o nome do titular: '),
                input('Digite o cpf do titular: '),
                float(input('Digite o saldo inicial: '))
                )  
            print(pf)

            var = input('Você deseja cadastrar segundo titular? \nSim \nNão \nOpção escolhida: ')
            if var.lower() == 'sim':
                pf.Segundo_Titular = input('Digite o segundo titular: ')
                print(pf)

        case 'pj':
            pj = PessoaJuridica(
                input('Digite o nome do titular: '),
                input('Digite o cnpj do titular: '),
                float(input('Digite o saldo inicial: '))
            )
            print(pj)
            var = input('Você deseja cadastrar segundo titular? \nSim \nNão \nOpção escolhida: ')
            if var.lower() == 'sim':
                pj.Segundo_Titular = input('Digite o segundo titular: ')
            print(pj)


    cond = int(input('Digite 0 para continuar ou 1 para sair: '))




